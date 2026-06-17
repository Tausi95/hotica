# /qa-ad

Run QA on a rendered Hotica ad or the full campaign.

## Usage

```
/qa-ad A1              — QA a specific ad
/qa-ad all             — QA all rendered ads
/qa-ad landing         — QA the landing page spec
/qa-ad launch          — Full pre-launch checklist audit
```

## What this does

Reads the QA spec from `conversion/qa_production.py` and applies it to the rendered
output or the production spec for the requested ad/section.

## QA checks applied (per ad)

- Safety: no explicit content in any frame, blur on UI tiles 40px minimum
- Platform: text in center 80% of frame, readable at zero sound
- Brand: dark grade, film grain, vignette consistent with spec
- Copy: no typos, no weak phrasing, CTA is access language not command
- Edit: rhythm break present, restraint moment present, no glitch effects
- Technical: CRF 18 export, yuv420p, correct duration (within 0.1s of spec)

## Steps when invoked

1. Read `conversion/qa_production.py` → load the relevant section
2. If checking a rendered file: use ffprobe to verify technical specs
3. Apply QA checklist from the spec
4. Report: pass / fail / warnings for each check
5. Flag anything that blocks launch (P0 issues)

## Quick ffprobe check command

```bash
ffprobe -v quiet -print_format json -show_streams \
  /home/mage107/Documents/projects/hotica/conversion/ad_a1_behind_the_dark_9x16.mp4
```

## Safety check reminder

Before any ad is uploaded:
- Review all source frames at 1x speed
- Confirm no accidental explicit frame (even 1 frame = IG ban risk)
- All model UI thumbnails: 40px+ blur confirmed
- Manual cover thumbnail selected (not IG auto-selected)
