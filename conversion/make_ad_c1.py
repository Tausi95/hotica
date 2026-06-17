#!/usr/bin/env python3
# Hotica — Ad C1: Before. After. (v2)
# 10s · 1080x1920 (9:16) + 1080x1080 (1:1)
# Clips: AmyClaire_01 (before) · EvaWilliamsX_05 (after)
# Music: Lizzie Berchie — Love Deep ft. Filah Lah Lah
# X-only — lifestyle consideration, hard cut as pattern interrupt

from hotica_engine import *

DUR        = 10.0
MUSIC_PATH = AUDIO / "Lizzie Berchie - Love Deep ft. Filah Lah Lah (Official Video).mp3"

# ── per-clip grades ───────────────────────────────────────────────────
def grade_before(raw):
    """AmyClaire_01 — flat, desaturated: the 'before' state."""
    f = raw.astype(np.float32) / 255.0
    f *= 0.85
    grey = f[:, :, 0] * 0.299 + f[:, :, 1] * 0.587 + f[:, :, 2] * 0.114
    mix  = 0.55
    f[:, :, 0] = f[:, :, 0] * (1 - mix) + grey * mix
    f[:, :, 1] = f[:, :, 1] * (1 - mix) + grey * mix
    f[:, :, 2] = f[:, :, 2] * (1 - mix) + grey * mix
    return f

def grade_after(raw):
    """EvaWilliamsX_05 — full Hotica grade: dark, warm, cinematic."""
    f = raw.astype(np.float32) / 255.0
    f *= 0.58
    f[:, :, 0] = np.clip(f[:, :, 0] * 1.18, 0, 1)
    f[:, :, 1] = np.clip(f[:, :, 1] * 1.06, 0, 1)
    f[:, :, 2] = np.clip(f[:, :, 2] * 0.82, 0, 1)
    return f

GRADE_FNS = [grade_before, grade_after]
VIG_STR   = [0.15, 0.38]
GRAIN_AMP = [8,    14  ]

# ── segments ──────────────────────────────────────────────────────────
print("Loading clips...")
SEGS = [
    load_seg(GRADED / "AmyClaire_01.mp4",    0.0, 2.5),   # BEFORE
    load_seg(GRADED / "EvaWilliamsX_05.mp4", 0.0, 7.5),   # AFTER
]
CUM = [0.0]
for s in SEGS:
    CUM.append(CUM[-1] + s.duration)

# ── overlays ──────────────────────────────────────────────────────────
print("Building overlays...")
T_BEFORE   = text_rgba(["Before."],       FONT_MD, 52,      MUTED,  tracking=10,      y_center=H // 2 - 80)
T_SAME_YOU = text_rgba(["Same you."],     FONT_XB, SZ_HEAD, TEXT_C, tracking=TRK_HEAD)
T_BETTER   = text_rgba(["Better access."],FONT_XB, SZ_SUBHD + 12, ACCENT, tracking=TRK_SUBHD)

LOGO_RGBA, URL_RGBA, CTA_RGBA = build_end_card("Upgrade your access", cta_size=48)

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

    # "Before." label — over flat clip (t ≈ 0.3–2.2s)
    a0 = fade_a(t, 0.3, 2.2, fi=0.25, fo=0.3)
    if a0 > 0:
        f = blend(f, T_BEFORE, a0 * 0.75)

    # "Same you." — builds after hard cut (t ≈ 4.0–6.5s)
    a1 = fade_a(t, 4.0, 6.5, fi=0.4, fo=0.35)
    if a1 > 0:
        f = blend(f, T_SAME_YOU, a1)

    # "Better access." — accent, overlaps (t ≈ 5.5–8.0s)
    a2 = fade_a(t, 5.5, 8.0, fi=0.4, fo=0.4)
    if a2 > 0:
        f = blend(f, T_BETTER, a2)

    f = apply_end_card(f, t, 8.6, LOGO_RGBA, URL_RGBA, CTA_RGBA)

    return f.clip(0, 255).astype(np.uint8)

# ── render ────────────────────────────────────────────────────────────
print("\nRendering C1 — Before. After. v2...")
render_ad(make_frame, DUR, OUT / "ad_c1_before_after", MUSIC_PATH)
