#!/usr/bin/env python3
# Hotica — Ad C2: The Room You Want To Be In (v3)
# 10s · 1080x1920 (9:16) + 1080x1080 (1:1)
# Clips: AlishaBell_03 · EvaWilliamsX_09 · OliviaRimes_04 · GiaBell_02
# Music: Giveon — Heartbreak Anniversary

from hotica_engine import *

DUR        = 10.0
MUSIC_PATH = AUDIO / "Giveon - Heartbreak Anniversary (Official Music Video).mp3"

# ── per-clip grades ───────────────────────────────────────────────────
def grade_neon_warm(raw):
    """AlishaBell_03 — neon warmed toward gold, not cold cyan."""
    f = raw.astype(np.float32) / 255.0
    f *= 0.70
    f[:, :, 0] = np.clip(f[:, :, 0] * 1.15, 0, 1)
    f[:, :, 1] = np.clip(f[:, :, 1] * 1.10, 0, 1)
    f[:, :, 2] = np.clip(f[:, :, 2] * 0.95, 0, 1)
    return f

def grade_golden(raw):
    """EvaWilliamsX_09 — golden cinematic: warm highlights, rich shadows."""
    f = raw.astype(np.float32) / 255.0
    f *= 0.62
    f[:, :, 0] = np.clip(f[:, :, 0] * 1.18, 0, 1)
    f[:, :, 1] = np.clip(f[:, :, 1] * 1.05, 0, 1)
    f[:, :, 2] = np.clip(f[:, :, 2] * 0.76, 0, 1)
    return f

def grade_scarlet(raw):
    """OliviaRimes_04 — rich red-warm, two-model energy."""
    f = raw.astype(np.float32) / 255.0
    f *= 0.67
    f[:, :, 0] = np.clip(f[:, :, 0] * 1.20, 0, 1)
    f[:, :, 1] = np.clip(f[:, :, 1] * 0.93, 0, 1)
    f[:, :, 2] = np.clip(f[:, :, 2] * 0.82, 0, 1)
    return f

def grade_dark_warm(raw):
    """GiaBell_02 — deep, warm, mysterious: room in shadow."""
    f = raw.astype(np.float32) / 255.0
    f *= 0.50
    f[:, :, 0] = np.clip(f[:, :, 0] * 1.16, 0, 1)
    f[:, :, 2] = np.clip(f[:, :, 2] * 0.78, 0, 1)
    return np.where(f < 0.06, f * 0.60 + 0.004, f)   # lift near-blacks

GRADE_FNS = [grade_neon_warm, grade_golden, grade_scarlet, grade_dark_warm]
VIG_STR   = [0.25, 0.35, 0.28, 0.45]
GRAIN_AMP = [14,   15,   13,   18  ]

# ── segments ──────────────────────────────────────────────────────────
print("Loading clips...")
SEGS = [
    load_seg(GRADED / "AlishaBell_03.mp4",   7.0, 10.5),
    load_seg(GRADED / "EvaWilliamsX_09.mp4", 0.0,  2.5),
    load_seg(GRADED / "OliviaRimes_04.mp4",  0.0,  1.5),
    load_seg(GRADED / "GiaBell_02.mp4",      2.0,  4.0),
]
CUM = [0.0]
for s in SEGS:
    CUM.append(CUM[-1] + s.duration)

# ── overlays ──────────────────────────────────────────────────────────
print("Building overlays...")
T_LINE1 = text_rgba(["Not everyone gets in."], FONT_XB, SZ_SUBHD, TEXT_C,
                     tracking=TRK_SUBHD, y_center=H // 2 - 60)
T_LINE2 = text_rgba(["You can."],              FONT_XB, SZ_HEAD,  ACCENT,
                     tracking=20, y_center=H // 2 + 80)

LOGO_RGBA, URL_RGBA, CTA_RGBA = build_end_card("Join the room", cta_size=56)

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

    # "Not everyone gets in." — over golden face (t ≈ 3.8–6.8s)
    a1 = fade_a(t, 3.8, 6.8, fi=0.45, fo=0.4)
    if a1 > 0:
        f = blend(f, T_LINE1, a1 * 0.92)

    # "You can." — the turn, over dark room (t ≈ 7.8–9.8s)
    a2 = fade_a(t, 7.8, 9.8, fi=0.4, fo=0.35)
    if a2 > 0:
        f = blend(f, T_LINE2, a2)

    f = apply_end_card(f, t, 8.8, LOGO_RGBA, URL_RGBA, CTA_RGBA)

    return f.clip(0, 255).astype(np.uint8)

# ── render ────────────────────────────────────────────────────────────
print("\nRendering C2 — The Room You Want To Be In v3...")
render_ad(make_frame, DUR, OUT / "ad_c2_the_room", MUSIC_PATH)
