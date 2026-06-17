# /make-ad

Build and render a Hotica Instagram ad from the production spec.

## What this does

Generates or runs the Python render script for one of the 6 campaign ads (A1–C2).
All specs live in `conversion/ads_production.py`. All scripts output to `conversion/`.

## Usage

```
/make-ad A1
/make-ad A2
/make-ad B1
/make-ad B2
/make-ad C1
/make-ad C2
```

## Ad index

| ID | Title                        | Duration | Primary clip pool       |
|----|------------------------------|----------|-------------------------|
| A1 | Behind The Dark              | 10s      | GiaBell_02 (confirmed)  |
| A2 | Unlock                       | 12s      | Needs clip selection    |
| B1 | Make It Yours                | 12s      | Needs clip selection    |
| B2 | Your Page. Your Rules.       | 15s      | Needs clip selection    |
| C1 | Before. After.               | 10s      | Needs clip selection    |
| C2 | The Room You Want To Be In   | 10s      | Needs clip selection    |

## Asset paths

- Clips (graded):   `social/graded/`
- Clips (cinematic): `social/cinematic/`
- Fonts:            `Hotica Brand Guide/Funnel_Display/ttf/`
                    `Hotica Brand Guide/Funnel_Sans/ttf/`
- Logo SVGs:        `Hotica Brand Guide/Hotica Logos/SVG/`
- Scripts:          `conversion/make_ad_a1.py`, etc.
- Output:           `conversion/ad_<id>_<title>_9x16.mp4` + `_1x1.mp4`

## Clip assignment rules (from session memory)

**Already assigned to social films — do not reuse:**
- film3-v2: DashaFlame_01/02/03, ChloeSug_01/02, ShopieSkyes_01/02, SweetNicole_01
- film5-editorial-v2: JenniferReys_01/02, EvellyneReys_01, KelsiCarter_01, LilithReys_01, IrisAdams_02
- film5-bartier-v2: CarlaReysX_03, EvaWilliamsX_04, MiaMuse_03, OliviaRimes_03, SarahLust_03, AmberXoo_02

**Fresh / available for ads:**
AmenaVans_01, AmyClaire_01, Angellblack_01/02, CaliMoon_05, CarlaReysX_04,
EvaWilliamsX_05–11, GiaBell_02 (A1 confirmed), IrisAdams_01, MichelleReys_02,
OliviaRimes_04/05/06, RebeccaBlackX_01, SarahLust_04, SweetNicole_02,
AlishaBell_01/02/03, AnastasiaDeep_01/02

## Technical constants (apply to all ads)

- Output resolution: 1080×1920 (9:16 primary), 1080×1080 (1:1 secondary)
- FPS: 30
- Codec: libx264, CRF 18, yuv420p
- No audio — music added in post, target -14 LUFS / -1dBTP
- moviepy 1.0.3 + Pillow 10+ patch: `PIL.Image.ANTIALIAS = PIL.Image.LANCZOS`
- Film grain: 15% (A1, C2), 12% (A2, C1), 10% (B1, B2)

## Hard constraints (every ad)

- Never show nipples, genitals, or explicit framing — even in source frames
- Blur on any model UI thumbnail: 40px minimum
- All text in center 80% of frame (IG UI eats top/bottom 10%)
- Review all source frames at 1x before export

## Steps when invoked

1. Read the full ad spec from `conversion/ads_production.py` (the relevant AD_XX constant)
2. Check if a script already exists (`conversion/make_ad_XX.py`)
3. If not: write the script using the same pattern as `make_ad_a1.py`
4. Select clips from the available pool — confirm with user if uncertain
5. Run the script: `cd /home/mage107/Documents/projects/hotica/conversion && python3 make_ad_XX.py`
6. Report output file paths and any issues
