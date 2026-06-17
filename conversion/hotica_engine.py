"""
hotica_engine.py — shared rendering pipeline for all Hotica conversion ads.

Usage in each ad script:
    from hotica_engine import *

Grade functions defined in ad scripts must:
  - Accept raw (uint8 H×W×3)
  - Return float32 H×W×3 in [0.0, 1.0]   ← pure color transform only
  - NOT apply vignette or grain (engine handles both dynamically)

Then in make_frame, call:
    f = dynamic_grade(raw, grade_fn, t, BEATS, vig_strength=0.28)
"""

import io
import re
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFont
import PIL
PIL.Image.ANTIALIAS = PIL.Image.LANCZOS
from moviepy.editor import VideoFileClip, VideoClip, AudioFileClip

# ── paths (all relative to this file's location) ─────────────────────
_HERE  = Path(__file__).parent          # .../hotica/conversion/
BASE   = _HERE.parent                   # .../hotica/
GRADED = BASE / "social" / "graded"
BRAND  = BASE / "Hotica Brand Guide"
AUDIO  = BASE / "media" / "audio"
OUT    = _HERE

# ── canvas ────────────────────────────────────────────────────────────
W, H, FPS = 1080, 1920, 30

# ── brand palette ─────────────────────────────────────────────────────
BG     = np.array([20,  16,  30],  dtype=np.uint8)   # #14101E  deep plum-black
ACCENT = np.array([254, 159, 183], dtype=np.uint8)   # #FE9FB7  dusty rose
TEXT_C = np.array([250, 249, 246], dtype=np.uint8)   # #FAF9F6  warm white
MUTED  = np.array([135, 127, 152], dtype=np.uint8)   # #877F98  cool grey

# ── brand fonts ───────────────────────────────────────────────────────
FONT_XB = str(BRAND / "Funnel_Display" / "ttf" / "FunnelDisplay-ExtraBold.ttf")
FONT_BD = str(BRAND / "Funnel_Display" / "ttf" / "FunnelDisplay-Bold.ttf")
FONT_LT = str(BRAND / "Funnel_Display" / "ttf" / "FunnelDisplay-Light.ttf")
FONT_MD = str(BRAND / "Funnel_Sans"    / "ttf" / "FunnelSans-Medium.ttf")
FONT_SB = str(BRAND / "Funnel_Sans"    / "ttf" / "FunnelSans-Bold.ttf")
SVG     = str(BRAND / "Hotica Logos"   / "SVG"  / "Hotica_Logo1.svg")

# Standard type sizes (px at 1080 canvas width)
SZ_HERO  = 164   # single impact word
SZ_TITLE = 108   # 2–3 word title
SZ_HEAD  = 100   # headline
SZ_SUBHD = 76    # subheading / supporting line
SZ_CTA   = 52    # call to action
SZ_URL   = 38    # hotica.com
SZ_LABEL = 36    # muted micro-labels

# Standard letter-spacing (px)
TRK_HERO  = 44
TRK_TITLE = 12
TRK_HEAD  = 18
TRK_SUBHD = 10
TRK_CTA   = 6
TRK_URL   = 4

# ── vignette (precomputed, reused across all ads) ─────────────────────
_Y, _X = np.ogrid[:H, :W]
_r = np.sqrt((_X - W // 2) ** 2 + (_Y - H // 2) ** 2) / np.sqrt((W // 2) ** 2 + (H // 2) ** 2)
VIG = np.clip(_r ** 2.0 * 1.0, 0, 1).astype(np.float32)[:, :, None]  # raw mask; scaled per grade


# ── easing & animation ────────────────────────────────────────────────
def ease(t):
    t = max(0.0, min(1.0, t))
    return t * t * (3 - 2 * t)


def fade_a(t, t0, t1, fi=0.25, fo=0.25):
    """Smooth fade in/out window. Returns alpha in [0, 1]."""
    dur = t1 - t0
    rel = t - t0
    if rel <= 0 or rel >= dur:
        return 0.0
    if rel < fi:
        return ease(rel / fi)
    if rel > dur - fo:
        return ease((dur - rel) / fo)
    return 1.0


# ── compositing ───────────────────────────────────────────────────────
def blend(f32, rgba, alpha=1.0):
    """Alpha-composite an RGBA overlay onto float32 frame f32."""
    a = (rgba[:, :, 3] / 255.0) * alpha
    return f32 * (1 - a[:, :, None]) + rgba[:, :, :3].astype(np.float32) * a[:, :, None]


# ── text rendering (with safe-area auto-fit) ──────────────────────────
def text_rgba(lines, font_path, size, color, tracking=0, y_center=None,
              line_height=1.3, safe_margin=60):
    """
    Render text lines onto a transparent H×W RGBA canvas.
    Auto-reduces font size until every line fits within W - 2*safe_margin.
    Guarantees no text is cut or clipped at canvas edges.
    """
    max_w = W - 2 * safe_margin
    font  = ImageFont.truetype(font_path, size)

    # Shrink until every line fits the safe area
    while size > 10:
        widths = []
        for ln in lines:
            chars = list(ln)
            w = (sum(font.getbbox(c)[2] - font.getbbox(c)[0] for c in chars)
                 + tracking * max(0, len(chars) - 1))
            widths.append(w)
        if max(widths) <= max_w:
            break
        size = max(10, int(size * 0.93))
        font = ImageFont.truetype(font_path, size)

    img  = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    lh   = int(size * line_height)
    total_h = lh * len(lines)
    y0 = (H - total_h) // 2 if y_center is None else int(y_center - total_h // 2)

    for i, line in enumerate(lines):
        chars = list(line)
        ws    = [font.getbbox(c)[2] - font.getbbox(c)[0] for c in chars]
        tw    = sum(ws) + tracking * max(0, len(chars) - 1)
        x     = (W - tw) // 2
        y     = y0 + i * lh
        for ch, cw in zip(chars, ws):
            draw.text((x, y), ch, font=font, fill=(*color.tolist(), 255))
            x += cw + tracking

    return np.array(img)


# ── clip loading ──────────────────────────────────────────────────────
def load_seg(path, t0, t1):
    """Load, scale-to-fill, and centre-crop a video segment to W×H."""
    raw   = VideoFileClip(str(path)).subclip(t0, t1)
    scale = max(W / raw.w, H / raw.h)
    nw, nh = int(raw.w * scale), int(raw.h * scale)
    clip  = raw.resize((nw, nh))
    cx, cy = (nw - W) // 2, (nh - H) // 2
    return clip.crop(x1=cx, y1=cy, x2=cx + W, y2=cy + H)


# ── logo ──────────────────────────────────────────────────────────────
def load_logo(target_w=300):
    try:
        import cairosvg
        svg_text = open(SVG).read()
        svg_text = re.sub(r'<rect[^>]+class=["\']c["\'][^/]*/>', '', svg_text)
        png = cairosvg.svg2png(bytestring=svg_text.encode(), output_width=target_w)
        return Image.open(io.BytesIO(png)).convert("RGBA")
    except Exception as e:
        print(f"  logo load failed: {e}")
        return None


def build_logo_rgba(target_w=300, y_offset=-60):
    """Return logo composited onto a transparent H×W canvas, centred."""
    logo = load_logo(target_w)
    if logo is None:
        return None
    canvas = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    lw, lh = logo.size
    x = (W - lw) // 2
    y = H // 2 - lh // 2 + y_offset
    canvas.paste(logo, (x, y), mask=logo.split()[3])
    return np.array(canvas)


# ── standard end card ─────────────────────────────────────────────────
def build_end_card(cta_text, cta_font=None, cta_size=SZ_CTA, cta_color=None,
                   cta_tracking=TRK_CTA):
    """
    Returns (logo_rgba, url_rgba, cta_rgba) — call apply_end_card() each frame.
    cta_text: e.g. "Unlock now →", "Create on Hotica", "Join the room"
    """
    if cta_color is None:
        cta_color = ACCENT
    if cta_font is None:
        cta_font = FONT_BD
    logo_rgba = build_logo_rgba(300)
    url_rgba  = text_rgba(["hotica.com"], FONT_MD, SZ_URL, MUTED,
                          tracking=TRK_URL, y_center=H // 2 + 55)
    cta_rgba  = text_rgba([cta_text], cta_font, cta_size, cta_color,
                          tracking=cta_tracking, y_center=H // 2 + 150)
    return logo_rgba, url_rgba, cta_rgba


def apply_end_card(f, t, end_start, logo_rgba, url_rgba, cta_rgba, dip_dur=0.5):
    """Blend dark BG + logo/URL/CTA into frame f starting at end_start."""
    rel = t - end_start
    if rel <= 0:
        return f
    dip = ease(min(1.0, rel / dip_dur))
    bg  = np.full((H, W, 3), BG, dtype=np.float32)
    f   = f * (1 - dip) + bg * dip
    a_l = ease(max(0.0, min(1.0, (rel - dip_dur)         / 0.40)))
    a_u = ease(max(0.0, min(1.0, (rel - dip_dur - 0.40)  / 0.35)))
    a_c = ease(max(0.0, min(1.0, (rel - dip_dur - 0.80)  / 0.35)))
    if logo_rgba is not None and a_l > 0:
        f = blend(f, logo_rgba, a_l)
    if a_u > 0:
        f = blend(f, url_rgba, a_u)
    if a_c > 0:
        f = blend(f, cta_rgba, a_c)
    return f


# ── beat analysis ─────────────────────────────────────────────────────
def analyze_beats(audio_path, duration):
    """
    Analyze music for beat times. Returns a beat_data dict used by
    beat_energy() and beat_phase(). Gracefully degrades without librosa.
    """
    try:
        import librosa
        import librosa.beat
        print(f"  Analyzing beats: {Path(audio_path).name}...")
        y, sr = librosa.load(str(audio_path), duration=float(duration), sr=22050)
        tempo_arr, beat_frames = librosa.beat.beat_track(
            y=y, sr=sr, start_bpm=100, units='time')
        tempo = float(np.atleast_1d(tempo_arr)[0])
        beat_times = np.asarray(beat_frames, dtype=np.float32)
        print(f"  {len(beat_times)} beats @ {tempo:.1f} BPM")
        return {'beat_times': beat_times, 'tempo': tempo}
    except ImportError:
        print("  librosa not found — beat sync disabled (pip install librosa)")
        return {'beat_times': np.array([], dtype=np.float32), 'tempo': 120.0}
    except Exception as e:
        print(f"  beat analysis failed ({e}) — continuing without sync")
        return {'beat_times': np.array([], dtype=np.float32), 'tempo': 120.0}


def beat_energy(t, beat_data):
    """
    Returns an energy multiplier at time t:
      1.6  — on a beat (within 120 ms)
      1.25 — near a beat (within 350 ms)
      1.0  — between beats
    """
    bts = beat_data['beat_times']
    if len(bts) == 0:
        return 1.0
    d = np.abs(bts - t)
    if d.min() < 0.12:
        return 1.6
    if d.min() < 0.35:
        return 1.25
    return 1.0


def beat_phase(t, beat_data):
    """Returns phase in [0, 2π] relative to the beat grid."""
    tempo = beat_data.get('tempo', 120.0)
    if tempo <= 0:
        return 0.0
    period = 60.0 / tempo
    return (t % period) / period * 2.0 * np.pi


# ── dynamic grade ─────────────────────────────────────────────────────
def dynamic_grade(raw, grade_fn, t, beat_data,
                  vig_strength=0.28, grain_base=14):
    """
    Apply grade_fn (returns float32 [0,1]) then layer beat-driven effects:
      - Breathing luminance pulse (slow sine, scaled by beat energy)
      - Dynamic vignette (intensifies on beats)
      - Beat-reactive film grain
    Returns uint8 H×W×3.

    grade_fn contract: accepts uint8 raw, returns float32 [0,1] — color only.
    """
    f      = grade_fn(raw)                        # float32 [0,1]
    energy = beat_energy(t, beat_data)
    phase  = beat_phase(t, beat_data)
    breath = 0.5 + 0.5 * np.sin(2.0 * np.pi * t * 0.55 + phase)

    # Breathing: luminance pulse tied to energy and beat phase
    lum = 1.0 + 0.045 * breath * (energy - 0.85)
    f   = np.clip(f * lum, 0.0, 1.0)

    # Dynamic vignette — intensifies on beats
    vig_scale = vig_strength * (1.0 + 0.5 * (energy - 1.0) * (0.5 + 0.5 * breath))
    f = f * (1.0 - VIG * vig_scale)

    # Beat-reactive grain
    amp   = grain_base * (0.75 + 0.5 * energy)
    grain = np.random.normal(0.0, amp, (H, W, 3)).astype(np.float32)
    return np.clip(f * 255.0 + grain, 0, 255).astype(np.uint8)


# ── segment selector ──────────────────────────────────────────────────
def get_seg_idx(t, cum_times):
    """Return (idx, local_t) for time t given cumulative segment time array."""
    for i in range(len(cum_times) - 1):
        if t < cum_times[i + 1]:
            return i, t - cum_times[i]
    idx = len(cum_times) - 2
    return idx, cum_times[idx + 1] - cum_times[idx] - 1.0 / FPS


# ── renderer ──────────────────────────────────────────────────────────
_RENDER_P = dict(
    codec='libx264',
    preset='slow',
    ffmpeg_params=['-crf', '18', '-pix_fmt', 'yuv420p'],
    threads=4,
    logger='bar',
)


def render_ad(make_frame, duration, out_slug, audio_path):
    """
    Write 4 output files from make_frame:
      {out_slug}_9x16.mp4
      {out_slug}_1x1.mp4
      {out_slug}_9x16_music.mp4
      {out_slug}_1x1_music.mp4

    out_slug: full path without extension, e.g. OUT / 'ad_a2_unlock'
    """
    slug   = str(out_slug)
    crop_y = (H - W) // 2
    vid    = VideoClip(make_frame, duration=float(duration))

    print("  9:16  silent...")
    vid.write_videofile(f"{slug}_9x16.mp4", fps=FPS, audio=False, **_RENDER_P)

    print("  1:1   silent...")
    vid.crop(x1=0, y1=crop_y, x2=W, y2=crop_y + W).write_videofile(
        f"{slug}_1x1.mp4", fps=FPS, audio=False, **_RENDER_P)

    music = AudioFileClip(str(audio_path)).subclip(0, float(duration))
    vid_m = vid.set_audio(music)

    print("  9:16  music...")
    vid_m.write_videofile(f"{slug}_9x16_music.mp4", fps=FPS, **_RENDER_P)

    print("  1:1   music...")
    vid_m.crop(x1=0, y1=crop_y, x2=W, y2=crop_y + W).write_videofile(
        f"{slug}_1x1_music.mp4", fps=FPS, **_RENDER_P)

    print(f"\n  ✓  {Path(slug).name} — 4 files written")
