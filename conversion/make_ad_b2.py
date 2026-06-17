#!/usr/bin/env python3
# Hotica — Ad B2: Your Page. Your Rules. (v2)
# 15s · 1080x1920 (9:16) + 1080x1080 (1:1)
# Clips: RebeccaBlackX_01 · MichelleReys_02 · IrisAdams_01 · SarahLust_04
# Music: Offset — Clout ft. Cardi B
# X-only — creator conversion, ownership angle

from hotica_engine import *

DUR        = 15.0
MUSIC_PATH = AUDIO / "Offset - Clout ft. Cardi B (Official Video).mp3"

# ── per-clip grades ───────────────────────────────────────────────────
def grade_intro(raw):
    """RebeccaBlackX_01 — clean opener, neutral confidence."""
    f = raw.astype(np.float32) / 255.0
    f *= 0.68
    f[:, :, 0] = np.clip(f[:, :, 0] * 1.10, 0, 1)
    f[:, :, 1] = np.clip(f[:, :, 1] * 1.04, 0, 1)
    return f

def grade_ownership(raw):
    """MichelleReys_02 — warm cinematic: the ownership moment."""
    f = raw.astype(np.float32) / 255.0
    f *= 0.62
    f[:, :, 0] = np.clip(f[:, :, 0] * 1.20, 0, 1)
    f[:, :, 1] = np.clip(f[:, :, 1] * 1.08, 0, 1)
    f[:, :, 2] = np.clip(f[:, :, 2] * 0.84, 0, 1)
    return f

def grade_power(raw):
    """IrisAdams_01 — editorial, direct, powerful."""
    f = raw.astype(np.float32) / 255.0
    f *= 0.65
    f[:, :, 0] = np.clip(f[:, :, 0] * 1.14, 0, 1)
    f[:, :, 2] = np.clip(f[:, :, 2] * 0.88, 0, 1)
    return f

def grade_close(raw):
    """SarahLust_04 — cinematic close: decisive."""
    f = raw.astype(np.float32) / 255.0
    f *= 0.58
    f[:, :, 0] = np.clip(f[:, :, 0] * 1.16, 0, 1)
    f[:, :, 2] = np.clip(f[:, :, 2] * 0.80, 0, 1)
    return f

GRADE_FNS = [grade_intro, grade_ownership, grade_power, grade_close]
VIG_STR   = [0.20, 0.32, 0.26, 0.40]
GRAIN_AMP = [10,   13,   12,   14  ]

# ── segments ──────────────────────────────────────────────────────────
print("Loading clips...")
SEGS = [
    load_seg(GRADED / "RebeccaBlackX_01.mp4", 0.0,  2.5),
    load_seg(GRADED / "MichelleReys_02.mp4",  0.0,  4.5),
    load_seg(GRADED / "IrisAdams_01.mp4",     0.0,  3.0),
    load_seg(GRADED / "SarahLust_04.mp4",     0.0,  4.0),
]
CUM = [0.0]
for s in SEGS:
    CUM.append(CUM[-1] + s.duration)

# ── overlays ──────────────────────────────────────────────────────────
print("Building overlays...")
T_DECIDE = text_rgba(["You decide", "what they see."], FONT_XB, SZ_TITLE, TEXT_C, tracking=TRK_TITLE)
T_OWN    = text_rgba(["Own your space."],              FONT_XB, SZ_SUBHD, MUTED,  tracking=TRK_SUBHD)
T_SIGNAL = text_rgba(["Real subscribers. Real income."],
                      FONT_MD, SZ_LABEL, MUTED, tracking=TRK_URL, y_center=H // 2 + 160)

LOGO_RGBA, URL_RGBA, CTA_RGBA = build_end_card("Start earning →", cta_size=52)

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

    # "You decide what they see." — emotional core (t ≈ 6.0–9.0s)
    a1 = fade_a(t, 6.0, 9.0, fi=0.45, fo=0.4)
    if a1 > 0:
        f = blend(f, T_DECIDE, a1)

    # "Own your space." — builds as above fades (t ≈ 9.5–13.0s)
    a2 = fade_a(t, 9.5, 13.0, fi=0.4, fo=0.4)
    if a2 > 0:
        f = blend(f, T_OWN, a2)

    # Income signal — subtle, late (t ≈ 10.5–13.0s)
    a3 = fade_a(t, 10.5, 13.0, fi=0.4, fo=0.35)
    if a3 > 0:
        f = blend(f, T_SIGNAL, a3 * 0.80)

    f = apply_end_card(f, t, 13.5, LOGO_RGBA, URL_RGBA, CTA_RGBA)

    return f.clip(0, 255).astype(np.uint8)

# ── render ────────────────────────────────────────────────────────────
print("\nRendering B2 — Your Page. Your Rules. v2...")
render_ad(make_frame, DUR, OUT / "ad_b2_your_page_your_rules", MUSIC_PATH)
