#!/usr/bin/env python3
# Hotica — Ad A1: Behind The Dark (v3)
# 10s · 1080x1920 (9:16) + 1080x1080 (1:1)
# Clips: GiaBell_02 · EvaWilliamsX_09 · Angellblack_01 · AlishaBell_01
# Music: Taylor Belle — MAGIC

from hotica_engine import *

DUR        = 10.0
MUSIC_PATH = AUDIO / "Taylor Belle - MAGIC (Official Audio)(1).mp3"

# ── grade (single mood across all clips: deep, warm, crushed) ─────────
def grade_dark(raw):
    """Very dark, crushed shadows, warm skin — the signature A1 look."""
    f = raw.astype(np.float32) / 255.0
    f *= 0.52
    f[:, :, 0] = np.clip(f[:, :, 0] * 1.14, 0, 1)
    f[:, :, 2] = np.clip(f[:, :, 2] * 0.78, 0, 1)
    return np.where(f < 0.07, f * 0.65 + 0.005, f)   # lift blacks slightly

GRADE_FNS = [grade_dark] * 4
VIG_STR   = [0.42, 0.42, 0.42, 0.42]
GRAIN_AMP = [16,   16,   16,   16  ]

# ── segments ──────────────────────────────────────────────────────────
print("Loading clips...")
SEGS = [
    load_seg(GRADED / "GiaBell_02.mp4",      0.0,  2.5),
    load_seg(GRADED / "EvaWilliamsX_09.mp4", 0.0,  2.5),
    load_seg(GRADED / "Angellblack_01.mp4",  8.0, 10.5),
    load_seg(GRADED / "AlishaBell_01.mp4",   0.0,  2.5),
]
CUM = [0.0]
for s in SEGS:
    CUM.append(CUM[-1] + s.duration)

# ── overlays ──────────────────────────────────────────────────────────
print("Building overlays...")
T_LINE1 = text_rgba(["Some things"],          FONT_XB, SZ_HEAD,  TEXT_C, tracking=22)
T_LINE2 = text_rgba(["aren't for everyone."], FONT_XB, SZ_SUBHD, TEXT_C, tracking=14)

LOGO_RGBA, URL_RGBA, CTA_RGBA = build_end_card("See what's inside →", cta_size=54)

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

    # Text across clips 3+4 (t ≈ 5–9.8s)
    a1 = fade_a(t, 5.0, 7.5, fi=0.4, fo=0.35)
    a2 = fade_a(t, 6.4, 9.8, fi=0.4, fo=0.35)
    if a1 > 0:
        f = blend(f, T_LINE1, a1)
    if a2 > 0:
        f = blend(f, T_LINE2, a2)

    f = apply_end_card(f, t, 8.5, LOGO_RGBA, URL_RGBA, CTA_RGBA)

    return f.clip(0, 255).astype(np.uint8)

# ── render ────────────────────────────────────────────────────────────
print("\nRendering A1 — Behind The Dark v3...")
render_ad(make_frame, DUR, OUT / "ad_a1_behind_the_dark", MUSIC_PATH)
