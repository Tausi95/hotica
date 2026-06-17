#!/usr/bin/env python3
# Hotica — Ad A2: Unlock (v3)
# 12s · 1080x1920 (9:16) + 1080x1080 (1:1)
# Clips: AmyClaire_01 · AlishaBell_03 · OliviaRimes_04 · EvaWilliamsX_09
# Music: Kali Uchis — Moonlight

from hotica_engine import *

DUR        = 12.0
MUSIC_PATH = AUDIO / "Kali Uchis - Moonlight (Official Music Video).mp3"

# ── per-clip grades (pure color, float32 [0,1]; no vignette or grain) ─
def grade_tease(raw):
    """AmyClaire_01 — slightly cool, desaturated: the 'before' state."""
    f = raw.astype(np.float32) / 255.0
    f *= 0.72
    f[:, :, 2] = np.clip(f[:, :, 2] * 1.06, 0, 1)
    f[:, :, 0] = np.clip(f[:, :, 0] * 0.95, 0, 1)
    return f

def grade_neon(raw):
    """AlishaBell_03 — punchy cyan neon, darkened BG."""
    f = raw.astype(np.float32) / 255.0
    f *= 0.68
    f[:, :, 1] = np.clip(f[:, :, 1] * 1.20, 0, 1)
    f[:, :, 2] = np.clip(f[:, :, 2] * 1.25, 0, 1)
    f[:, :, 0] = np.clip(f[:, :, 0] * 0.90, 0, 1)
    return f

def grade_red(raw):
    """OliviaRimes_04 — warm red, sensual."""
    f = raw.astype(np.float32) / 255.0
    f *= 0.65
    f[:, :, 0] = np.clip(f[:, :, 0] * 1.22, 0, 1)
    f[:, :, 1] = np.clip(f[:, :, 1] * 0.94, 0, 1)
    f[:, :, 2] = np.clip(f[:, :, 2] * 0.80, 0, 1)
    return f

def grade_face(raw):
    """EvaWilliamsX_09 — dark cinematic, face contrast."""
    f = raw.astype(np.float32) / 255.0
    f *= 0.58
    f[:, :, 0] = np.clip(f[:, :, 0] * 1.12, 0, 1)
    f[:, :, 2] = np.clip(f[:, :, 2] * 0.80, 0, 1)
    return f

GRADE_FNS = [grade_tease, grade_neon, grade_red, grade_face]

# Vignette strength and grain amplitude per clip
VIG_STR   = [0.25, 0.22, 0.30, 0.45]
GRAIN_AMP = [12,   14,   14,   16  ]

# ── segments ──────────────────────────────────────────────────────────
print("Loading clips...")
SEGS = [
    load_seg(GRADED / "AmyClaire_01.mp4",    0.0,  2.5),
    load_seg(GRADED / "AlishaBell_03.mp4",   7.0, 11.0),
    load_seg(GRADED / "OliviaRimes_04.mp4",  0.0,  2.5),
    load_seg(GRADED / "EvaWilliamsX_09.mp4", 0.0,  2.5),
]
CUM = [0.0]
for s in SEGS:
    CUM.append(CUM[-1] + s.duration)

# ── overlays ──────────────────────────────────────────────────────────
print("Building overlays...")
T_UNLOCK = text_rgba(["UNLOCK"],            FONT_XB, SZ_HERO,  TEXT_C, tracking=TRK_HERO)
T_SUB    = text_rgba(["exclusive access"],  FONT_MD, SZ_LABEL, MUTED,
                     tracking=TRK_CTA, y_center=H // 2 + 115)

LOGO_RGBA, URL_RGBA, CTA_RGBA = build_end_card("Unlock now →")

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

    # UNLOCK — over clips 2+3, alpha pulses on beats
    a_ul = fade_a(t, 3.2, 9.0, fi=0.5, fo=0.5)
    if a_ul > 0:
        energy = beat_energy(t, BEATS)
        pulse  = 0.80 + 0.15 * (energy - 1.0)
        f = blend(f, T_UNLOCK, a_ul * pulse)

    # "exclusive access" sub-label — over face close-up
    a_sub = fade_a(t, 9.2, 11.4, fi=0.4, fo=0.3)
    if a_sub > 0:
        f = blend(f, T_SUB, a_sub)

    # End card
    f = apply_end_card(f, t, 10.6, LOGO_RGBA, URL_RGBA, CTA_RGBA)

    return f.clip(0, 255).astype(np.uint8)

# ── render ────────────────────────────────────────────────────────────
print("\nRendering A2 — Unlock v3 (beat-synced dynamic grade)...")
render_ad(make_frame, DUR, OUT / "ad_a2_unlock", MUSIC_PATH)
