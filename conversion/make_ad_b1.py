#!/usr/bin/env python3
# Hotica — Ad B1: Make It Yours (v2)
# 12s · 1080x1920 (9:16) + 1080x1080 (1:1)
# Clips: AnastasiaDeep_01 · AlishaBell_02 · SweetNicole_02 · CaliMoon_05
# Music: James Vickery — Until Morning
# X-only — creator acquisition angle

from hotica_engine import *

DUR        = 12.0
MUSIC_PATH = AUDIO / "James Vickery - Until Morning A COLORS SHOW.mp3"

# ── per-clip grades ───────────────────────────────────────────────────
def grade_warm_open(raw):
    """AnastasiaDeep_01 — warm atmospheric opener."""
    f = raw.astype(np.float32) / 255.0
    f *= 0.65
    f[:, :, 0] = np.clip(f[:, :, 0] * 1.14, 0, 1)
    f[:, :, 1] = np.clip(f[:, :, 1] * 1.06, 0, 1)
    f[:, :, 2] = np.clip(f[:, :, 2] * 0.86, 0, 1)
    return f

def grade_neon_creator(raw):
    """AlishaBell_02 — neon energy: this is YOUR platform."""
    f = raw.astype(np.float32) / 255.0
    f *= 0.68
    f[:, :, 1] = np.clip(f[:, :, 1] * 1.18, 0, 1)
    f[:, :, 2] = np.clip(f[:, :, 2] * 1.22, 0, 1)
    f[:, :, 0] = np.clip(f[:, :, 0] * 0.92, 0, 1)
    return f

def grade_fresh(raw):
    """SweetNicole_02 — clean warm: the audience."""
    f = raw.astype(np.float32) / 255.0
    f *= 0.70
    f[:, :, 0] = np.clip(f[:, :, 0] * 1.10, 0, 1)
    f[:, :, 1] = np.clip(f[:, :, 1] * 1.04, 0, 1)
    return f

def grade_close(raw):
    """CaliMoon_05 — cinematic close: the decision moment."""
    f = raw.astype(np.float32) / 255.0
    f *= 0.58
    f[:, :, 0] = np.clip(f[:, :, 0] * 1.16, 0, 1)
    f[:, :, 2] = np.clip(f[:, :, 2] * 0.80, 0, 1)
    return f

GRADE_FNS = [grade_warm_open, grade_neon_creator, grade_fresh, grade_close]
VIG_STR   = [0.28, 0.22, 0.20, 0.40]
GRAIN_AMP = [11,   12,   10,   14  ]

# ── segments ──────────────────────────────────────────────────────────
print("Loading clips...")
SEGS = [
    load_seg(GRADED / "AnastasiaDeep_01.mp4", 0.0,  2.0),
    load_seg(GRADED / "AlishaBell_02.mp4",    8.0, 13.0),
    load_seg(GRADED / "SweetNicole_02.mp4",   0.0,  2.5),
    load_seg(GRADED / "CaliMoon_05.mp4",      0.0,  2.5),
]
CUM = [0.0]
for s in SEGS:
    CUM.append(CUM[-1] + s.duration)

# ── overlays ──────────────────────────────────────────────────────────
print("Building overlays...")
T_YOUR_AUD  = text_rgba(["Your audience."],  FONT_XB, SZ_HEAD,  TEXT_C, tracking=TRK_HEAD)
T_YOUR_PLAT = text_rgba(["Your platform."],  FONT_XB, SZ_HEAD,  ACCENT, tracking=TRK_HEAD)
T_DONT_WAIT = text_rgba(["For creators who", "don't wait."],
                         FONT_MD, 42, MUTED, tracking=TRK_CTA, y_center=H // 2 + 140)

LOGO_RGBA, URL_RGBA, CTA_RGBA = build_end_card("Create on Hotica", cta_size=52)

# ── beat analysis ──────────────────────────────────────────────────────
BEATS = analyze_beats(MUSIC_PATH, DUR)

# ── frame function ────────────────────────────────────────────────────
def make_frame(t):
    idx, local_t = get_seg_idx(t, CUM)
    local_t = min(local_t, SEGS[idx].duration - 1.0 / FPS)
    raw = SEGS[idx].get_frame(local_t)

    f = dynamic_grade(raw, GRADE_FNS[idx], t, BEATS,
                      vig_strength=VIG_STR[idx],
                      grain_base=GRAIN_AMP[idx]).astype(np.float32)

    # "Your audience." — over neon clip (t ≈ 2.5–6.5s)
    a1 = fade_a(t, 2.5, 6.5, fi=0.4, fo=0.35)
    if a1 > 0:
        f = blend(f, T_YOUR_AUD, a1 * 0.88)

    # "Your platform." — builds as above fades (t ≈ 5.5–9.5s)
    a2 = fade_a(t, 5.5, 9.5, fi=0.4, fo=0.4)
    if a2 > 0:
        f = blend(f, T_YOUR_PLAT, a2)

    # "For creators who don't wait." — muted close (t ≈ 9.5–11.5s)
    a3 = fade_a(t, 9.5, 11.5, fi=0.3, fo=0.3)
    if a3 > 0:
        f = blend(f, T_DONT_WAIT, a3)

    f = apply_end_card(f, t, 10.6, LOGO_RGBA, URL_RGBA, CTA_RGBA)

    return f.clip(0, 255).astype(np.uint8)

# ── render ────────────────────────────────────────────────────────────
print("\nRendering B1 — Make It Yours v2...")
render_ad(make_frame, DUR, OUT / "ad_b1_make_it_yours", MUSIC_PATH)
