# /run-production

Run the full Hotica ad campaign production workflow — strategy through export.

## What this does

Orchestrates the complete campaign production in the correct order:
1. Load specs from the three production files
2. Generate/run ad scripts
3. Track which ads are done vs pending
4. Provide QA checklist status

## Production file index

| File                              | Contents                                      |
|-----------------------------------|-----------------------------------------------|
| `conversion/ads_production.py`    | Strategy, 6 ad specs, style guide, audio dir  |
| `conversion/landing_pg_production.py` | Landing page wireframe, UI system, copy    |
| `conversion/qa_production.py`     | QA audit, launch checklist, master summary    |

## Recommended launch order (from master summary)

1. A1 — Behind The Dark (cold awareness, broad) → builds retarget pool
2. C2 — The Room You Want To Be In (lifestyle awareness) → concurrent with A1
3. A2 — Unlock (consideration, retarget A1 engagers) → after 5–7 days
4. B1 — Make It Yours (creator consideration) → concurrent with A2
5. C1 — Before. After. (lifestyle consideration) → week 3, post A/B data
6. B2 — Your Page. Your Rules. (creator conversion) → after B1 runs 7+ days

## Script locations

| Ad | Script                              | Status         |
|----|-------------------------------------|----------------|
| A1 | `conversion/make_ad_a1.py`          | Written        |
| A2 | `conversion/make_ad_a2.py`          | Not yet written|
| B1 | `conversion/make_ad_b1.py`          | Not yet written|
| B2 | `conversion/make_ad_b2.py`          | Not yet written|
| C1 | `conversion/make_ad_c1.py`          | Not yet written|
| C2 | `conversion/make_ad_c2.py`          | Not yet written|

## How to run an ad

```bash
cd /home/mage107/Documents/projects/hotica/conversion
python3 make_ad_a1.py
```

Output: `conversion/ad_a1_behind_the_dark_9x16.mp4` + `_1x1.mp4`

## Steps when invoked

1. Read `conversion/qa_production.py` → `FINAL_LAUNCH_CHECKLIST` for current status
2. Identify which ads are rendered vs pending
3. For each pending ad: use `/make-ad <ID>` workflow
4. After all 6 ads: run QA checklist from `qa_production.py`
5. Report: what's done, what's blocked, what's next

## P0 blockers (must resolve before launch)

- [ ] Fill [PRICE] in landing page FAQ entry 3
- [ ] Design blurred preview grid to pixel-perfect spec (not placeholder)
- [ ] Confirm social proof numbers are real, or remove the strip
- [ ] Creator portal link must resolve (live portal or waitlist form)
- [ ] All ad source frames reviewed frame-by-frame for explicit content
- [ ] Manual cover thumbnail set for each ad before IG upload
