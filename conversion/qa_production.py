# Hotica — QA + Launch Pack
# Generated: 2026-04-22
# Source: qa_only.xml + master.xml (sections 10–12)

EXECUTIVE_QA_VERDICT = """
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
EXECUTIVE QA VERDICT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

OVERALL: LAUNCH-READY PENDING EXECUTION QUALITY

The campaign is strategically sound and premium in positioning. The 6-ad system covers
the funnel correctly. The landing page architecture matches the emotional logic of each
ad entry point. No safety violations in the spec.

PRIMARY RISK AREAS
1. Execution quality on UI elements — the Hotica UI mockups must be real, not placeholder
2. Creator copy specificity — B1/B2 copy risks feeling generic
3. Social proof numbers — must be real at launch or removed
4. B2 income counter animation — high fidelity required, not a CSS ticker
5. C1 execution — the Before/After contrast must be dramatic or the ad underperforms

VERDICT BY BUCKET
Bucket A:  Strategically strong. Execution-dependent. A1 is the purest brand expression.
Bucket B:  Copy needs one revision pass for Hotica-specificity. Structure is correct.
Bucket C:  C2 is the strongest awareness ad. C1 depends entirely on execution quality.
Landing:   Architecture and copy are sound. Blurred grid is make-or-break.
"""

WHAT_IS_STRONG = """
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
WHAT IS STRONG
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. The withholding mechanic is consistent across all 6 ads — this is the campaign's
   single most important strategic strength. Never explained, always implied.

2. Bucket A (A1, A2) is strategically sharp. A1's single-camera-move structure is
   the right call — restraint IS the ad.

3. C2's copywriting — "Not everyone gets in." → "You can." — is the best two-line
   turn in the campaign. Protect it.

4. CTA language across all 6 ads is access-oriented and premium: enter, unlock, join,
   claim. Not a command among them.

5. Landing page architecture correctly segments consumer vs creator traffic with
   different CTAs (#FE9FB7 vs #CBFB05), different anchors, different copy tone.

6. The color system is distinctive and premium. Darkest Desire backgrounds are
   recognizable and non-generic.

7. The FAQ section addresses the 6 highest-friction objections. Entry 4 (safety) and
   entry 6 (creator selectivity) are particularly strong.

8. Audio direction: specifying CUT-ON-BREATH and targeting LUFS -14 shows production
   maturity. The silence guidelines prevent cheap music choices.

9. The "For now." line on the final CTA is the best soft-urgency mechanism in the
   campaign — premium, ambiguous, effective.

10. Safety guidance is explicit and implementable. No guesswork for editors.
"""

WHAT_IS_WEAK = """
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
WHAT IS WEAK
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. CREATOR COPY SPECIFICITY (B1, B2)
   "Your audience. Your platform." has been said by every creator platform in 2023–2025.
   It is not wrong — it is just not distinctly Hotica. The positioning line
   "For creators who don't wait." is stronger. Reorder: lead with that line, support
   with the declarative copy.

2. C1 EXECUTION DEPENDENCY
   Before. After. is the most conventional ad in the campaign. If the Before/After
   color contrast is subtle or the Before doesn't feel genuinely flat, the ad
   underperforms. This ad has the highest execution risk.

3. SOCIAL PROOF NUMBERS ARE PLACEHOLDER
   "12,847 subscribers" and "340+ creators" are invented. Fake-looking specificity
   is worse than no social proof. Either launch with real numbers or remove the strip
   entirely and add it later.

4. BLURRED GRID IS UNDESIGNED
   The most important conversion element on the landing page has no design yet.
   It cannot be a placeholder. This blocks the landing page launch.

5. B2 INCOME COUNTER ANIMATION
   If this is built as a CSS counter or jQuery ticker, it will look cheap and destroy
   the ad's premium positioning. It requires requestAnimationFrame, smooth easing,
   and pixel-perfect UI design before shooting.

6. [PRICE] IN FAQ ENTRY 3
   The FAQ has a literal placeholder. This must be filled before launch.
   A landing page with "[PRICE]" visible to users loses all credibility instantly.

7. CREATOR PORTAL LINK IN FOOTER
   "Creator Portal" is listed in the footer — this portal must exist before launch,
   or the link must be replaced with a waitlist form.
"""

HIGH_PRIORITY_FIXES = """
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
HIGH-PRIORITY FIXES (ORDERED BY SEVERITY)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

P0 — BLOCKS LAUNCH
──────────────────
1. Fill [PRICE] in FAQ entry 3 before any page goes live.
2. Design the blurred preview grid to pixel-perfect spec — real UI, not boxes.
3. Confirm social proof numbers are real, or remove the strip entirely.
4. Ensure creator portal link resolves — live portal or waitlist form.

P1 — HIGH IMPACT, FIX BEFORE ADS GO LIVE
──────────────────────────────────────────
5. Commission Hotica UI design before shooting A2 and B2.
   The UI elements (lock tiles, creator dashboard, notification UI) must exist as
   designed assets before any compositing happens in post.

6. B2 income counter: specify requestAnimationFrame implementation to the dev team.
   Test on low-end Android before locking the edit.

7. Revise B1/B2 creator copy to be more Hotica-specific.
   Suggested revision for B1:
     Current: "Your audience. Your platform."
     Revised: "For creators who don't wait." (lead) → "Your audience. Yours."
   This anchors the ad to a Hotica-specific claim before the generic platform statement.

P2 — IMPROVE BEFORE SCALE
──────────────────────────
8. C1 Before/After: commission the color grade plan before shooting. The Before must
   be dramatically flat — not just slightly desaturated. The After must be undeniably
   premium. Test the contrast on a phone screen before locking.

9. A1 source clip quality: if the lighting in the source clip isn't already dark and
   editorial, the whole ad fails. Grade this ad in post before anything else goes wide.
"""

AD_BY_AD_QA = """
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
AD-BY-AD QA NOTES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

A1 — BEHIND THE DARK
Status:  Strong. The single-camera-move structure is correct.
Risk:    Lighting quality of the source clip determines whether this reads premium or muddy.
         Grade the shadows carefully — crushed but not blocked up, especially in the hair.
Watch:   The blurred UI tile flash at 6.0s must read as a real app, not a mockup screenshot.
         If it looks fake, cut it entirely — the ad still works without it.
Slop check: Passes. No cheap effects, no text overload, no explicit risk.

A2 — UNLOCK
Status:  Strong mechanic. High execution dependency.
Risk:    The Hotica UI MUST look like a real premium app. A fake or placeholder UI
         destroys the ad's entire premise. Do not shoot until the UI design is complete.
Watch:   The hand must be elegant. Brief the talent/styling specifically on this.
         A cheap-looking hand holding a phone = instant trust collapse.
         The unlock progress animation at 3.5–5.0s must feel like real app behavior.
Slop check: Passes. No explicit content risk. Lock icon must look premium, not stock.

B1 — MAKE IT YOURS
Status:  Conceptually sound. Copy needs one pass.
Risk:    If "Your audience. Your platform." leads, the ad sounds like every other creator
         platform. "For creators who don't wait." is the stronger hook — move it up.
Watch:   The UI dashboard at 5.0–7.0s needs real design. Same requirement as A2.
         The model's "confidence" must be directed specifically — avoid hollow posing.
Slop check: Passes. No explicit content risk.

B2 — YOUR PAGE. YOUR RULES.
Status:  Good structure. Conversion-oriented. Income counter is the make-or-break.
Risk:    The income counter animation must be premium-quality — smooth, real physics.
         If it looks like a template counter, it undercuts everything.
Watch:   "You decide what they see." at 6.0–8.0s is the emotional core.
         Do not rush it. Do not put effects on it. Let it breathe on black.
         The notification UI at 8.5s must feel like a real app notification, not an overlay.
Slop check: Passes. Keep income framing confident, not desperate.

C1 — BEFORE. AFTER.
Status:  Execution-dependent. Highest risk ad in the campaign.
Risk:    If the Before/After contrast is subtle, the ad is invisible.
         The Before must feel genuinely flat — not just slightly desaturated.
         The After must feel unmistakably premium and warm.
Watch:   The hard cut at 2.5s IS the whole ad. If the cut is weak, there is no ad.
         Test the color contrast on a phone screen in a bright room before locking.
Slop check: Passes. Before/After is not inherently cheap if executed with restraint.

C2 — THE ROOM YOU WANT TO BE IN
Status:  Strongest awareness ad in the campaign.
Risk:    Over-production. This ad works because of restraint — do not add effects to it.
         The 3 opening editorial cuts must be genuinely beautiful, not just dark.
Watch:   "Not everyone gets in." → "You can." is the best copy turn in the campaign.
         Protect the pause between them. Do not crush it. Do not add a transition.
         The model silhouette at 4.5s must be fully back-to-camera — zero explicit risk.
Slop check: Passes. Keep the montage graceful — if any cut feels stock, replace the clip.
"""

LANDING_PAGE_QA = """
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
LANDING PAGE QA NOTES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

HERO
Status:     Strong. Copy is tight. CTA language is correct.
Risk:       If background video loop is used, it must be motion-optimized for mobile.
            Unoptimized autoplay video tanks load time and kills conversion before it starts.
            Recommended: serve a static image to mobile, video to desktop (via media query).
Watch:      The subheadline "Hotica is private. Premium. Built for people who want more."
            is slightly long. If A/B testing, test against: "Private. Premium. Exclusive."

SOCIAL PROOF STRIP
Status:     Placeholder — cannot launch with fake numbers.
Fix:        Use real numbers at launch, or remove and add post-launch.
            Do not invent specific numbers (e.g. "12,847") — this reads as fake
            and damages trust faster than having no strip.

PRIVATE ACCESS BLOCK
Status:     Most important section. Not yet designed.
Risk:       If this looks like placeholder boxes, it kills conversion.
Fix:        This must be designed to pixel-perfect spec before any traffic hits the page.
            The blur must be consistent across all screen sizes — test on mobile before launch.
            Tap-to-modal behavior must be tested on iOS Safari specifically.

PREMIUM EXPERIENCE SECTION
Status:     Strong. 3-card layout is correct. Copy is clear.
Watch:      Icons must be designed — do not use stock icon libraries that feel generic.
            Commission or design the 3 feature icons to match the Hotica visual language.

CREATOR SECTION
Status:     Strong. UV Green CTA differentiates cleanly.
Watch:      "Real subscribers, real income" risks reading as income projection.
            Ensure the body copy says "subscribers pay directly. You earn." not a specific number.

FAQ
Status:     5 of 6 entries are launch-ready. Entry 3 ([PRICE]) blocks launch.
Fix:        Fill the price. This is P0.
Watch:      Test accordion on iOS Safari and Android Chrome — accordions commonly break
            on mobile browsers due to height: auto transition issues.

FINAL CTA BLOCK
Status:     Strong. "The door is open. / For now." is the best soft-urgency copy on the page.
Risk:       Email capture form must connect to a real email list before launch.
            Collect and do nothing = lost subscribers and potential GDPR issue.
Watch:      Privacy note is required — "We respect your privacy. No spam." must be present.
            Without it, email capture conversion drops significantly.

MOBILE (GENERAL)
Status:     Spec is correct. Must be tested before launch.
Fix:        Test on iPhone SE (375px), iPhone 14 Pro (393px), Samsung Galaxy S22 (360px).
            Sticky bottom CTA bar must clear the iOS home indicator (12px safe area).
            FAQ touch targets must be 48px minimum — check this on the smallest device.

PERFORMANCE
Target:     Page load under 3 seconds on 4G mobile (LCP under 2.5s)
Risk areas: Autoplay hero video, un-optimized images, font loading (Funnel Display + Funnel Sans)
Fix:        Preload fonts. Use WebP/AVIF for all images. Lazy-load everything below fold.
            If video is used in hero: serve compressed MP4 (under 2MB), poster image first.
"""

SAFETY_QA = """
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SAFETY QA NOTES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

OVERALL: SPEC IS INSTAGRAM-SAFE. EXECUTION MUST BE VERIFIED.

AD SAFETY BY AD
A1:  Collarbone/shoulder/hair framing. Safe. Verify source clip frame-by-frame before edit.
A2:  Blurred UI tiles — safe IF blur is 40px minimum at all sizes. Verify on export.
     Verify hand shot has no unintended explicit frame in the clip.
B1:  Creator framing — no explicit risk. Creator dashboard must not show explicit thumbnails.
B2:  Creator framing — no explicit risk. Notification UI must not show explicit content preview.
C1:  Before/After — no explicit risk in spec. Verify source clips used for both sides.
C2:  Back silhouette — safe. Verify no frame in the montage clips drifts into explicit territory.

LANDING PAGE SAFETY
- Blurred grid: 40px minimum blur must be preserved at all viewport sizes.
  Test on: mobile 375px, tablet 768px, desktop 1440px.
  CSS filter: blur(40px) can render differently across browsers — test in Safari.
- No visible explicit content should be accessible anywhere on the page without payment.

CRITICAL EXECUTION RULE
Before any ad is exported for upload:
  □ Review ALL source frames used in the edit at 1x speed
  □ Confirm no accidental explicit frame appears, even at 1 frame, even at low opacity
  □ Instagram moderation catches single-frame explicit content in video
  □ A single frame violation can result in account ban — not just ad rejection

INSTAGRAM MODERATION RISK FLAGS
Risk level: LOW (if spec is followed)
Risk level: HIGH (if these happen during execution):
  - Any frame with visible nipple, genital, or explicit sexual act
  - Blurred tile that renders at under 40px on export (check compression artifacts)
  - Text in-ad that references explicit content ("nude", "naked", "XXX", "18+")
  - Thumbnail selected by IG's auto-thumbnail that lands on an unfavorable frame
    → Solution: always upload with a manually selected cover image

COMPLIANCE
  - GDPR: email capture requires privacy notice + confirmation email
  - CCPA: add "Do Not Sell My Information" link to footer if US-targeted
  - Age gating: verify platform's age verification requirements before launch
  - Payment: confirm Paylolly integration is PCI-DSS compliant before accepting payments
"""

BRAND_PREMIUM_AUDIT = """
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
BRAND PREMIUM-FEEL AUDIT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

COLOR SYSTEM         PASS
Darkest Desire backgrounds are distinctive. Pink Bubblegum accent is unusual in the space
— it reads as fashion, not adult affiliate. UV Green for creator CTA is a strong split.

TYPOGRAPHY           PASS (pending font rendering test)
Funnel Display / Funnel Sans is the correct call. Clean, confident, fashion-adjacent.
Risk: if Funnel Display doesn't load (slow connection, ad blocker), the fallback font
will look generic. Ensure font is preloaded and cached correctly.

MOTION LANGUAGE      PASS (spec) / TBD (execution)
The motion spec is premium — slow push-ins, no glitch, dip-to-black between sections.
This will succeed or fail based on editor discipline. Brief editors specifically on the
"no unnecessary cuts" rule.

COPY OVERALL         MOSTLY PASSES
Consumer copy is strong. Creator copy needs the revision noted in High-Priority Fixes.
The best single line in the campaign: "Not everyone gets in. You can."
The weakest line: "Your audience. Your platform." — too generic.

CTA LANGUAGE         PASS
"Enter Hotica", "Unlock Access", "Join the room", "Claim Your Page" — all feel like
invitations to cross a threshold. Not one sounds desperate or corporate.

OVERALL SLOP RISK    MEDIUM
Execution is where this campaign wins or loses its premium feel. The spec is tight.
If editors, motion designers, and developers follow the spec: the campaign is premium.
If they substitute stock elements, template animations, or generic UI: it looks cheap.
"""

CONVERSION_AUDIT = """
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CONVERSION AUDIT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

FUNNEL COVERAGE      COMPLETE
Awareness (A1, C2) → Consideration (A2, B1, C1) → Conversion (B2, A2 retarget)
Both consumer and creator paths are covered end-to-end.

LANDING PAGE CTA DENSITY   APPROPRIATE
- Hero: primary CTA + secondary text link
- Sticky mobile bar: primary CTA (appears at 30% scroll)
- Private access block: "Unlock Access" CTA
- Creator section: "Claim Your Page" CTA
- Final CTA block: "Enter Hotica" + email capture
Total: 5 touchpoints. Not overloaded. Not under-represented.

EMAIL CAPTURE        STRONG IF WIRED CORRECTLY
The email capture on the final CTA block is correct — it catches undecided users before
they bounce. Requires:
  □ Connected to real email service (Mailchimp, ConvertKit, Klaviyo)
  □ Automated welcome email within 5 minutes of signup
  □ Privacy notice displayed (required for compliance)

CREATOR CONVERSION PATH    CLEAN
B1 → creator section → "Claim Your Page" → creator portal. No dead ends if portal exists.
Risk: if creator portal is not live at launch, this path dead-ends. Use a waitlist form
as a bridge until the portal is ready.

PRICE REVEAL TIMING  CORRECT
Price is withheld until FAQ entry 3 — after desire is established. This is the right
sequencing. Do not move price to hero on first launch.

FRICTION ASSESSMENT
High friction points:
  1. Payment wall — mitigated by email capture for undecided users
  2. Unknown price until FAQ — intentional, but may frustrate some users
  3. Creator portal not live — mitigated by waitlist form
Low friction: no signup required to browse, no pop-up on load, no forced registration

CONVERSION BOTTLENECK WATCH
If conversion is low after launch, investigate in this order:
  1. Is the blurred preview grid loading correctly on mobile?
  2. Is the sticky CTA bar appearing on mobile?
  3. Is the price in FAQ entry 3 filled in?
  4. Is the payment flow working end-to-end?
  5. Is the email capture form connected and confirming?
"""

FINAL_LAUNCH_CHECKLIST = """
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
FINAL LAUNCH CHECKLIST
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

CREATIVE — ADS
  □ All 6 ads shot with editorial lighting (test frame before full shoot)
  □ Hotica UI design completed before any UI compositing begins
  □ All 6 ads color graded to spec (deep blacks, warm skin, restrained saturation)
  □ Film grain overlays applied per spec (10–15% depending on ad)
  □ All ads exported 9:16 (1080×1920) and 1:1 (1080×1080) at CRF 18 or better
  □ All ads tested at zero sound — confirm readable and emotionally clear without audio
  □ All ads reviewed frame-by-frame for accidental explicit content
  □ All ads reviewed in Instagram preview (upload as draft, check thumbnail + playback)
  □ Manually select cover thumbnail for each ad — do not use IG's auto-selected frame
  □ Audio: master to -14 LUFS, -1dBTP true peak — verify in audio editor before export

LANDING PAGE
  □ Mobile-first build tested on: iPhone SE (375px), iPhone 14 Pro (393px), Galaxy S22 (360px)
  □ Blurred preview grid designed to pixel-perfect spec — real UI, not placeholder
  □ Blur confirmed at 40px minimum on all viewport sizes and in all browsers
  □ FAQ accordion tested on iOS Safari and Android Chrome
  □ Sticky CTA bar tested — appears at 30% scroll, clears iOS home indicator (12px safe area)
  □ [PRICE] filled in FAQ entry 3
  □ Email capture form connected to email service (Mailchimp / ConvertKit / Klaviyo)
  □ Welcome email automation confirmed — triggers within 5 minutes of signup
  □ Privacy notice displayed adjacent to email capture
  □ Creator portal link resolves — live portal OR waitlist form as bridge
  □ GDPR: privacy policy linked in footer, compliant with data collection practices
  □ CCPA: "Do Not Sell" link in footer if US audience is targeted
  □ Page load tested: LCP under 2.5s on 4G mobile
  □ Fonts preloaded: Funnel Display + Funnel Sans (woff2)
  □ All images in WebP/AVIF format with proper lazy loading
  □ Hero video (if used): compressed under 2MB MP4, poster image served first
  □ UTM parameters functional on all ad links — test attribution before launch

CAMPAIGN SETUP
  □ A/B test structure in place: A1 vs C2 for awareness, B1 vs B2 for creator
  □ UTM parameters: utm_source, utm_medium, utm_campaign, utm_content on all ads
  □ Retarget audiences created:
      - A1 engagers → retarget with A2
      - B1 engagers → retarget with B2
      - Landing page visitors → retarget with A2
  □ Frequency cap set: max 3 impressions per user per week per ad
  □ Budget allocated by funnel stage (awareness:consideration:conversion = 40:35:25)
  □ Campaign naming convention documented for reporting consistency

COPY
  □ All in-ad copy spell-checked
  □ All landing page copy spell-checked
  □ B1/B2 creator copy revised for Hotica-specificity
  □ Social proof numbers confirmed real (or section removed)
  □ FAQ entry 3 price confirmed and filled
  □ No placeholder text ([PRICE], [TBD], etc.) remains anywhere on the page

SAFETY
  □ All ad source frames reviewed frame-by-frame for accidental explicit content
  □ Blurred grid thumbnails confirmed at 40px+ blur across all viewport sizes
  □ All ad thumbnails manually set in IG before launch
  □ Payment integration confirmed PCI-DSS compliant
"""

MASTER_SUMMARY = """
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
MASTER SUMMARY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

RECOMMENDED LAUNCH ORDER
Week 1:   A1 (Behind The Dark) — cold awareness, broad — build retarget pool
          C2 (The Room You Want To Be In) — cold awareness, lifestyle — concurrent
Week 2:   A2 (Unlock) — consideration, retarget A1 engagers
          B1 (Make It Yours) — creator consideration, cold interest — concurrent
Week 3:   C1 (Before. After.) — lifestyle consideration — launch after A/B data informs
Week 4:   B2 (Your Page. Your Rules.) — creator conversion, retarget B1 engagers

FIRST AD TO TEST: A1
A1 is the purest expression of the Hotica brand. Its performance reveals the core
audience's response to the mystery/withholding positioning before more tactical ads run.
If A1 underperforms, the campaign has a brand positioning problem.
If A1 over-performs, the positioning is confirmed — scale aggressively.

AD-TO-LANDING-PAGE MAPPING
Ad  | Landing Page Entry                    | Anchor
A1  | Hero — "Enter Hotica"                 | #enter
A2  | Private access block — "Unlock Access"| #unlock
B1  | Creator section — "Build Your Presence"| #create
B2  | Creator CTA — "Claim Your Page"       | #create (scroll to CTA)
C1  | Features block — "Get Full Access"    | #access
C2  | Hero — "Join the room"                | #enter

FIRST A/B TEST
Test A1 headline on landing page:
  Variant A: "Some things aren't for everyone." (matches ad copy — continuity approach)
  Variant B: "Not everything is public." (curiosity/FOMO approach)
Metric: email capture rate + scroll depth to private access block.
Run for minimum 500 sessions per variant before calling.

SECOND A/B TEST (after first concludes)
Test consumer CTA text:
  Variant A: "Enter Hotica" (access language)
  Variant B: "Unlock Access" (action language)
Metric: click-through rate on hero CTA.

MOST IMPORTANT METRICS
1. CTR (click-through rate) — primary signal of hook quality by ad
2. Cost per click (CPC) — efficiency signal, benchmark by bucket
3. Landing page → email capture rate — top of conversion funnel health
4. Landing page → paid signup rate — bottom-line conversion signal
5. Creator application rate — B-side funnel health
6. Ad frequency fatigue curve — track CTR by frequency band (1-2x, 3-4x, 5x+)
   When CTR drops >30% from peak: rotate creative or pause that ad.

WHAT TO A/B TEST FIRST (PRIORITY ORDER)
Priority 1: A1 headline variant (see above)
Priority 2: Consumer CTA text (see above)
Priority 3: Hero background: video loop vs static editorial still
Priority 4: Social proof strip: with numbers vs removed
Priority 5: FAQ entry 3 framing: price-first ("$X/month") vs value-first ("Less than a dinner")

SCALING RULES
- Do not scale any ad until it has run for 7+ days with at least 1,000 impressions
- Scale winning ads by 20% budget increase every 48 hours — not 2x overnight
- If an ad's CTR drops 30%+ from launch peak: pause and replace with fresh creative
- Lookalike audiences (1-3% LAL off email list) should activate at 500+ email signups
"""
