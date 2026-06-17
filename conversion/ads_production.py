# Hotica — Ads Production Pack
# Generated: 2026-04-22
# Source: ads_only.xml + master.xml (sections 1–5)

EXECUTIVE_STRATEGY = """
CAMPAIGN THESIS
Hotica is sold as a portal, not a product. Every ad operates on the same psychological
mechanism: withholding. The viewer is shown enough to trigger desire and denied enough
to trigger action. The platform is never explained — it is implied through atmosphere,
access language, and the visual treatment of models as something worth paying to see more
of. This is the luxury-tech equivalent of a velvet rope campaign. The brand does not
chase — it selects.

FUNNEL STRATEGY
Two entry points, one destination. Curiosity-led traffic (Bucket A) enters through mystery
and FOMO. Creator-led traffic (Bucket B) enters through identity and aspiration. Lifestyle
traffic (Bucket C) enters through contrast and upgrade logic. All three streams land on
the same page but anchor to different sections based on ad origin.

WHY THE 6 ADS WORK AS A SYSTEM
Each ad hits a different psychological trigger — FOMO, identity, income, status, curiosity,
aspiration — but all share the same visual grammar: dark backgrounds, controlled revelation,
premium typography, restrained motion. The viewer who sees A1 on Monday and C2 on Thursday
feels continuity without repetition. The campaign builds a world, not six disconnected spots.

LANDING PAGE PSYCHOLOGY
The page mirrors the ad language. It withholds full access behind a CTA gate. Same color
system, same typographic restraint, same emotional logic: you are not on the outside
looking in — but you could be on the inside.
"""

FUNNEL_STRATEGY = """
STAGE         | FUNCTION                                    | ADS
Awareness     | Introduce brand atmosphere, no explanation  | A1, C2
Consideration | Introduce access, identity, creator angle   | A2, B1, C1
Conversion    | Drive immediate click and signup            | B2, A2 (retarget)

- Top of funnel: A1 and C2 run broad cold audiences. Pure mood. No explanation.
- Mid funnel: A2, B1, C1 run retargeting or interest-targeted cold segments.
- Bottom of funnel: B2 and second-rotation A2 run against warm, engaged traffic.
"""

CAMPAIGN_MATRIX = """
#  | TITLE                          | BUCKET    | STAGE         | AUDIENCE              | HOOK              | DUR | CTA                    | EMOTION MECHANISM    | VISUAL STYLE         | LP ANCHOR
A1 | Behind The Dark                | Curiosity | Awareness     | Broad cold F 25-34    | Mood / mystery    | 10s | "See what's inside"    | FOMO + desire        | Dark editorial       | Hero
A2 | Unlock                         | Curiosity | Consideration | Warm retarget         | UI tension/access | 12s | "Unlock now"           | Anticipation+denial  | UI overlay, lock/blur| Private access block
B1 | Make It Yours                  | Creator   | Consideration | Creator interest      | Identity/empow.   | 12s | "Create on Hotica"     | Pride + belonging    | Clean tech-luxury    | Creator section
B2 | Your Page. Your Rules.         | Creator   | Conversion    | Creator warm          | Ownership/income  | 15s | "Start earning"        | Control + security   | Bold UI, income frame| Creator CTA
C1 | Before. After.                 | Lifestyle | Consideration | Lifestyle cold F 22-32| Contrast/upgrade  | 10s | "Upgrade your access"  | Inadequacy resolved  | Split visual         | Features block
C2 | The Room You Want To Be In     | Lifestyle | Awareness     | Broad lifestyle cold  | Aspiration        | 10s | "Join the room"        | FOMO + aspiration    | Editorial montage    | Hero / lifestyle
"""

AUDIENCE_SEGMENTATION = """
SEGMENT              | DESCRIPTION                                              | BUCKET | TARGETING
Luxury Consumer      | F 25-34, fashion-adjacent, high aspirational engagement  | A, C   | Interest: fashion, luxury, nightlife; Behavioral: premium app installs
Creator-Aspiring     | F/M 20-30, content creators on IG/TikTok                 | B      | Interest: content creation, photography, monetization
Lifestyle-Upgrade    | F 22-32, status and self-image motivated                  | C      | Behavioral: higher-spend apps; Interest: lifestyle, wellness premium
Warm Retarget        | Engaged with prior ads or visited landing page            | A2, B2 | Custom audience: IG engagement, landing page visitors
Lookalike            | Modeled on early converters and email signups             | A1, C2 | 1-3% LAL off email list or high-intent visitors
"""

CTA_STRATEGY = """
PRINCIPLES
- CTAs must feel like invitations, not commands.
- Never desperate. No "Don't miss out", "Click now", "Limited time".
- Use access language: unlock, join, enter, see, discover.
- The CTA should feel like crossing a threshold, not completing a transaction.

AD  | IN-AD CTA               | POST-CLICK INTENT        | LANDING PAGE CTA MATCH
A1  | "See what's inside →"   | Curiosity → hero         | "Enter Hotica"
A2  | "Unlock now"            | Access → private block   | "Unlock Access"
B1  | "Create on Hotica"      | Identity → creator sect. | "Build Your Presence"
B2  | "Start earning →"       | Income → creator CTA     | "Claim Your Page"
C1  | "Upgrade your access"   | Upgrade → features block | "Get Full Access"
C2  | "Join the room"         | Aspiration → hero        | "Enter Hotica"

CTA DESIGN RULES
- Font: Funnel Display Bold, tracked +20, white on dark
- Duration on screen: last 1.5–2 seconds of ad, static — no animation
- Never: arrow clutter, countdown pressure, ALL CAPS desperation
"""

LANDING_PAGE_CONTINUITY = """
AD → EMOTIONAL STATE       | LP ENTRY            | PAGE MUST DO
A1 → curiosity, desire     | Hero above fold     | Maintain mystery, withhold full reveal, immediate gated CTA
A2 → anticipation, denial  | Private access block| Blurred preview grid, unlock CTA
B1 → identity, pride       | Creator section     | Lead with creator identity language, not income
B2 → ownership, income     | Creator CTA block   | Income framing, platform credibility, creator page mockup
C1 → upgrade resolved      | Features block      | Before/after logic in UI, list what access unlocks
C2 → aspiration, proof     | Hero                | Premium mood open, social proof numbers, exclusive CTA

CONTINUITY RULES
- Same dark palette on page as in ads — Darkest Desire / Sunset Purple surfaces
- Same type family: Funnel Display for headlines, Funnel Sans for body
- Blur treatment on preview content mirrors the locked state in A2
- Zero tonal whiplash between ad and landing page
"""

MASTER_STYLE_STANDARDS = """
COLOR SYSTEM
Token              | Hex     | Usage
Primary BG         | #14101E | Ad backgrounds, page primary surface
Secondary BG       | #1D182C | Cards, elevated surfaces
Primary Accent     | #FE9FB7 | CTAs, highlights, active UI states
Muted Text         | #877F98 | Secondary copy, captions, labels
Primary Text       | #FAF9F6 | Headlines, CTA text
Creator Accent     | #CBFB05 | Creator earnings — use sparingly
Warm Highlight     | #FFB534 | Premium moments only

TYPOGRAPHY
- Headlines: Funnel Display ExtraBold — tracking +15 to +20, tight leading
- Body/support: Funnel Sans Medium — normal tracking, 1.5 line-height
- UI overlays: Funnel Sans Regular — small, precise, restrained
- No decorative fonts. No script. No serif.

MOTION LANGUAGE
- Default camera: slow push-in. Never handheld chaos.
- Flash cuts: maximum 2 per ad, pattern interrupts only
- Dip-to-black: preferred over hard cuts between major sections
- Glitch: PROHIBITED — cheap and dated
- Parallax: text elements only, subtle
- Speed ramps: one per ad, at tension peak
- Motion blur: natural from clip, not added filter

COLOR GRADE
- Deep crushed shadows. Controlled highlight rolloff — never blown.
- Skin tones: warm, never orange, never cool-shifted
- Saturation: restrained, +10 max from neutral
- Grain: subtle, 15% max opacity
- No LUT presets that read as social media filter
- Target: luxury fashion film, not lifestyle reel

EDIT RHYTHM
- Average shot: 1.2–2.0s in build sections, up to 3–4s on holds
- One deliberate rhythm break per ad
- One long hold per ad — hold the viewer in the discomfort of wanting more
- Match cuts wherever visual continuity allows
- No jump cuts
"""

QUALITY_BAR = """
QUALITY BAR
- Every frame must hold as a still from a luxury fashion editorial
- Every line of copy is copy-edited before output — no typos, no weak phrasing
- Every CTA earns its click — no desperation, no generic action verbs
- Every ad functions at zero sound — 85% of viewers watch muted
- The six ads form a coherent world, not six random executions

ANTI-SLOP CHECKLIST
Category | Prohibited
Copy     | "Don't miss out", "Click now", "Hot girls", "Exclusive content waiting", any affiliate-adult phrasing
Visual   | Over-saturation, obvious stock energy, text on every frame, neon strobing
Edit     | Random fast cuts, whip pans, TikTok zoom reactions, CapCut template transitions
Audio    | Viral audio that dates the ad within weeks, over-compressed bass, low-budget lo-fi
Motion   | Glitch, VHS filter, film burn overuse, cheap particle overlays
Safety   | Any angle revealing nipples, genitals, or explicit framing — even implied
Tone     | Salacious, desperate, horny-brained — this is private-access luxury, not adult-affiliate spam

SELF-CHECK BEFORE ANY OUTPUT
1. Does it feel expensive?
2. Does it withhold more than it reveals?
3. Does the CTA feel like an invitation, not a command?
4. Is it unambiguously Instagram-safe?
5. Would it survive in a premium fashion-tech ad break?
"""

# ─────────────────────────────────────────────────────────────
# THE 6 ADS IN FULL DETAIL
# Each ad: A (Identity), B (Concept), C (Timeline), D (Beat Map),
#          E (Edit Language), F (Safe Asset), G (Copy), H (Captions), I (Tech)
# ─────────────────────────────────────────────────────────────

AD_A1 = """
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
AD A1 — BEHIND THE DARK
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

A. AD IDENTITY
Ad number:       A1
Title:           Behind The Dark
Purpose:         Cold awareness — introduce brand atmosphere, generate desire without explanation
Audience:        F 25-34, luxury/fashion interest, broad cold
Platform:        Instagram Feed + Reels
Duration:        10 seconds

B. CREATIVE CONCEPT
Concept: A slow camera pass through shadow and light reveals only the suggestion of a
         woman — never the full image — as text confirms what the viewer already suspects:
         this is not for everyone.
Rationale: The ad's power is entirely in what it refuses to show. The model becomes an
           icon, not a person. The brand becomes a locked room. The viewer's imagination
           does the conversion work.
Emotion:  Desire, curiosity, exclusionary FOMO
Action:   Profile visit → link click → hero landing page

C. EXACT TIMELINE
0.0–1.5   Black screen. Silence for 0.3s. Deep atmospheric pad fades in. Camera begins
           a slow right-to-left slide across a model in very low-key lighting. Edge of a
           collarbone, the curve of a shoulder blade in shadow. Frame cropped above clavicle.
           Editorial. Film grain at 15%. Background: #14101E.

1.5–3.0   Camera continues. Hair in motion — slight breeze or post effect. Jaw line caught
           in a narrow strip of warm light (#FFB534 reference). Still no face context.

3.0–4.5   Text fades in over frame — Funnel Display ExtraBold, #FAF9F6, tracked +20, center:
           "Some things"
           Hold 0.8s.

4.5–6.0   Text cuts to second line:
           "aren't for everyone."
           Camera slows to near-stop. Model at peak of frame — still editorial, no full reveal.

6.0–7.5   Dip to black (0.3s). Brief flash (0.5s max): blurred Hotica UI preview tile with
           lock icon — subliminal access signal. 40px+ blur minimum.

7.5–9.0   Hotica logo in #FAF9F6, centered on #14101E. Holds. After 0.5s, Funnel Sans fades:
           "hotica.com"

9.0–10.0  CTA in #FE9FB7 fades in below URL:
           "See what's inside →"
           Hold. End.

D. BEAT MAP
0.0–3.0   Intro beats — atmospheric, slow reveal, pure mood, no text
3.0–4.5   First interrupt — text arrives, changes register from visual to linguistic tension
4.5–6.0   Tension build — camera slows, exclusion statement completes
6.0–7.0   Pattern interrupt — dip-to-black + blurred UI flash, access signal
7.0–9.0   Hold — logo, premium pause
9.0–10.0  CTA lands
Loop:     Opens and closes on black — seamless loop for Reels

E. EDIT LANGUAGE
Pace:             Very slow — effectively one shot across the full ad
Average shot:     N/A — single continuous camera move with one cut at 6.0s
Pattern interrupt: 1 — dip-to-black/UI flash at 6.0s
Restraint moment: The full 6-second camera pass — no cut, no flash, no text interrupt
Flash cuts:       1 — blurred UI tile at 6.5s
Dip-to-black:     Yes, at 6.0s
Glitch:           PROHIBITED
Slow zoom:        No — lateral slide only
Parallax:         Text elements — subtle depth on enter
Motion blur:      Natural from camera slide only
Film grain:       15% overlay across full ad
Sharpening:       Moderate — preserve skin detail, avoid clinical sharpness
Light leak:       One subtle warm edge leak at right frame, 2.0–4.0 corridor, 20% opacity max
Vignette:         30% at edges, constant

F. SAFE ASSET GUIDANCE
- Frame stays above the bust at all times — collarbone, shoulder, jaw, hair only
- Never show: nipples, chest below collarbone, any explicit skin below the shoulder line
- Blur tile flash at 6.0s: 40px minimum blur — unreadable explicitly, readable contextually
- No suggestive pose implied through framing — model is an aesthetic object, not a voyeur target
- If source clip contains nudity: re-crop aggressively, use only the safest editorial frame

G. ON-SCREEN COPY
Line 1:   "Some things"
Line 2:   "aren't for everyone."
Domain:   "hotica.com"
CTA:      "See what's inside →"
No hashtags in-ad. No subtitles.

H. VOICE / SUBTITLES / CAPTIONS
Voiceover:       None — silence except for music
Subtitles:       None
IG caption:      "Some things aren't for everyone. 🔒 hotica.com"
Short variant:   "Not for everyone. hotica.com"
CTA line:        "Link in bio."
Hashtags:        #Hotica #PrivateAccess #ExclusiveContent #LuxuryCreator #UnlockNow

I. TECHNICAL EXECUTION NOTES
Aspect ratio:    9:16 primary (Reels/Stories), 1:1 secondary (Feed) — crop both from 9:16 master
Safe area:       All text in center 80% of frame — IG UI eats top/bottom 10%
Type sizes:      Headline ~72px at 1080p | URL ~28px | CTA ~32px
Export:          H.264, 1080x1920 (Reels), 1080x1080 (Feed), 30fps
Compression:     CRF 18 or equivalent — dark footage compresses poorly, do not over-compress
Brightness:      Master slightly bright for mobile — target black at IRE 5, not crushed to 0
Loop strategy:   Opens and closes on black — seamless
"""

AD_A2 = """
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
AD A2 — UNLOCK
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

A. AD IDENTITY
Ad number:       A2
Title:           Unlock
Purpose:         Mid-funnel consideration — warm retarget of A1 viewers and profile visitors
Audience:        Warm retarget (engaged A1, visited profile); cold interest: premium apps
Platform:        Instagram Feed + Reels + Stories
Duration:        12 seconds

B. CREATIVE CONCEPT
Concept: The viewer watches someone else reach for the unlock button and fail to see the
         full picture — the denial is the conversion mechanic.
Rationale: A2 is the tension ad. Where A1 creates desire, A2 creates the specific frustration
           of access denied. The UI element makes the platform tangible while keeping content
           hidden. The viewer's frustration is productized into a click.
Emotion:  Anticipation, denial, compulsion to unlock
Action:   Tap to unlock → link click → private access block

C. EXACT TIMELINE
0.0–1.0   Close-up: phone screen — Hotica UI. Profile grid visible. 3 tiles: 2 full-resolution
           (shoulder, back silhouette — safe), 1 blurred with centered gold lock icon. UI is real,
           premium-looking. Dark bg, clean typography.

1.0–2.5   An elegant hand enters frame from bottom (rings, good lighting). Reaches toward the
           blurred tile. Fingertip near screen. Text fade in (small, Funnel Sans, corner):
           "Subscriber only"

2.5–3.5   Cut to: model — editorial framing (shoulder, hair, edge of jaw). Warm light. 1.0s hold.
           No text. This is the reward that's being locked.

3.5–5.0   Cut back to: phone screen. Hand on the tile now. Progress indicator appears:
           "Unlocking..." — runs to 80% then... pauses.

5.0–6.0   Progress indicator stops. Tile stays blurred. Text below in #FE9FB7:
           "Unlock with Hotica"
           Hand pulls back slightly.

6.0–8.0   Quick cut sequence (3 cuts, each 0.6s):
           Shot 1 — another blurred tile, different profile
           Shot 2 — lock icon at 2x scale, centered on dark bg, subtle slow push-in
           Shot 3 — model again, different frame (collarbone, fabric movement)

8.0–9.5   Single beat of silence. Dip to near-black. Hotica logo fades in. Clean. Centered.

9.5–11.0  CTA in #FE9FB7 below logo:
           "Unlock now"
           Subtle pulse: 1.0x → 1.02x → 1.0x, once. Barely visible. Not gimmicky.

11.0–12.0 Logo + CTA + domain hold. End.

D. BEAT MAP
0.0–2.5   Intro — UI world established, hand introduces the access mechanic
2.5–3.5   First interrupt — model flash, the reward signal
3.5–6.0   Tension build — the unlock attempt, the stall, the denial
6.0–8.0   Fast cut sequence — rapid access signals, lock icon, model flash
8.0–9.5   Slow-down — near-black pause, logo reveal
9.5–12.0  CTA lands — unlock language, domain, hold

E. EDIT LANGUAGE
Pace:             Mixed — slow establishing, then 3-beat fast sequence
Average shot:     1.5s in cut sequence, 2.5s on longer holds
Pattern interrupt: Model flash at 2.5s, 3-beat sequence at 6.0s
Restraint moment: 1.0s near-silence + near-black at 8.0s
Match cut:        Hand approaching screen → model clip → hand on screen
Flash cuts:       3 in the 6.0–8.0 sequence
Dip-to-black:     Yes, at 8.0s
Glitch:           PROHIBITED
Slow zoom:        Subtle push-in on lock icon (Shot 2 only)
Motion blur:      Light — fast cuts benefit from minimal blur for rhythm
Film grain:       12% — slightly less than A1 to differentiate mood
Vignette:         Yes, consistent with A1

F. SAFE ASSET GUIDANCE
- All model clips: shoulder, jaw, hair, collarbone only — same crop rules as A1
- Blurred tiles: 40px+ minimum blur — unreadable explicitly, readable contextually
- Lock icon must read as platform UI — clean and minimal, not novelty graphic
- The hand must be elegant — no cheap voyeur energy in how the finger approaches screen
- No implied sexual framing in UI interaction — premium platform, not voyeur site

G. ON-SCREEN COPY
UI label:         "Subscriber only"
Progress text:    "Unlocking..."
Denial CTA:       "Unlock with Hotica" (in #FE9FB7)
End card:         Hotica logo
CTA:              "Unlock now"
Domain:           "hotica.com"

H. VOICE / SUBTITLES / CAPTIONS
Voiceover:        None
Subtitles:        None
IG caption:       "Some things stay locked. Unless you unlock them. 🔐 hotica.com"
Short variant:    "Behind the lock. hotica.com"
CTA line:         "Link in bio to unlock."
Hashtags:         #Hotica #UnlockAccess #ExclusiveContent #PrivateAccess #PremiumCreator

I. TECHNICAL EXECUTION NOTES
Aspect ratio:     9:16 primary (Stories + Reels), 1:1 secondary (Feed)
UI requirement:   Must look like a real app — real dark UI, proper typography, premium spacing
Phone frame:      No visible phone bezel — crop to screen only
Export:           H.264, CRF 18, 30fps
Loop:             A2 loops less cleanly than A1 — accept 0.3s dip to black as loop join
Safe area:        All text in center 80% vertically and horizontally
"""

AD_B1 = """
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
AD B1 — MAKE IT YOURS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

A. AD IDENTITY
Ad number:       B1
Title:           Make It Yours
Purpose:         Creator consideration — cold interest targeting of aspiring creators
Audience:        F/M 20-30, content creators, interest: photography, content monetization
Platform:        Instagram Feed + Reels
Duration:        12 seconds

B. CREATIVE CONCEPT
Concept: The camera belongs to the creator — Hotica is the platform that finally matches
         their ambition.
Rationale: This ad speaks entirely to identity. The creator doesn't see a product — they
           see themselves elevated. Visual treatment is cleaner and more architectural than
           Bucket A, signaling platform quality and seriousness. Copy is declarative, not
           promotional.
Emotion:  Pride, identity, sense of belonging to something premium
Action:   Creator landing page → "Build Your Presence"

C. EXACT TIMELINE
0.0–1.5   Close-up: a camera phone lens, catching light. Premium device. Hand holding it is
           confident. No hesitation. Music comes in clean — beat entry.

1.5–3.0   Cut to: the model/creator adjusting the phone angle. Deliberate. Confident. Someone
           who knows what they're doing. Face partially visible — camera partially blocks lower
           face. This is identity, not modeling.

3.0–5.0   Text fades in — Funnel Display ExtraBold, #FAF9F6:
           "Your audience."
           Camera continues — model locks in the shot angle. Satisfied expression.

5.0–7.0   Text transitions to:
           "Your platform."
           Cut to: Hotica creator dashboard UI. Clean dark interface. Profile page — follower
           count, content grid, premium aesthetic. Real platform, not a mockup. 1.5s hold.

7.0–8.5   Cut back to: model/creator. Full confidence — lower the camera, look ahead. Not at
           viewer. At the horizon. Someone who has arrived.

8.5–9.5   Dip to near-black. Hotica logo fades in. Below in #877F98 (Funnel Sans Medium):
           "For creators who don't wait."

9.5–11.0  CTA in #FE9FB7:
           "Create on Hotica"

11.0–12.0 Logo + CTA + domain hold. End.

D. BEAT MAP
0.0–3.0   Intro — creator world, camera, confidence — no text yet
3.0–5.0   First text — "Your audience." — shifts from visual to declarative
5.0–7.0   Second text + UI — "Your platform." — platform made tangible
7.0–8.5   Model/creator holds — the identity moment
8.5–12.0  Logo, positioning line, CTA, hold

E. EDIT LANGUAGE
Pace:             Moderate — not slow like A1, not punchy like A2. This ad breathes.
Average shot:     2.0–2.5s
Fast cuts:        None
Match cut:        Model adjusting camera → UI dashboard (implied: captured content → platform)
Film grain:       10% — cleaner than A1/A2, signals platform quality
Color:            Slightly warmer than A1 — identity, not mystery
Glitch:           PROHIBITED
Vignette:         Lighter, 20% — more open feel

F. SAFE ASSET GUIDANCE
- Creator framing — no explicit risk from source assets
- Standard portrait framing rules apply
- UI dashboard must not show explicit thumbnail content — keep grid blurred or safe-framed stills only

G. ON-SCREEN COPY
Line 1:           "Your audience."
Line 2:           "Your platform."
Positioning:      "For creators who don't wait."
CTA:              "Create on Hotica"
Domain:           "hotica.com"

H. VOICE / SUBTITLES / CAPTIONS
Voiceover:        None
IG caption:       "Your platform. Your rules. Your audience. Build on Hotica. hotica.com"
Short variant:    "Your audience. Your platform. hotica.com"
CTA line:         "Link in bio → start creating."
Hashtags:         #Hotica #ContentCreator #CreatorEconomy #BuildYourBrand #CreatorPlatform

I. TECHNICAL EXECUTION NOTES
Aspect ratio:     9:16 primary, 1:1 secondary
Device:           Must look premium — no cracked or cheap-looking phone
UI dashboard:     Real dark-mode Hotica UI — not a placeholder screenshot
Export:           H.264, CRF 18, 30fps
Grain:            Lower than A ads — platform quality signal
"""

AD_B2 = """
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
AD B2 — YOUR PAGE. YOUR RULES.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

A. AD IDENTITY
Ad number:       B2
Title:           Your Page. Your Rules.
Purpose:         Creator conversion — warm audience who saw B1 or engaged with creator content
Audience:        Warm retarget (B1 viewers); cold creator audience with monetization interest
Platform:        Instagram Feed + Reels
Duration:        15 seconds

B. CREATIVE CONCEPT
Concept: The platform pays. This ad shows the income reality without being trashy about it —
         a rising subscriber count and a creator who clearly owns their space.
Rationale: B2 is the conversion ad for creators. It introduces income as confirmation of
           ownership, not as the lead hook. The creator sees themselves running something,
           not selling themselves. The income signal is premium — a counter animation, not
           a cash emoji cascade.
Emotion:  Ownership, financial confidence, platform trust
Action:   Creator signup → "Claim Your Page"

C. EXACT TIMELINE
0.0–2.0   Hotica creator profile UI — full screen. Profile name, subscriber count ticking up
           slowly (e.g. "2,847 subscribers"), content grid (blurred thumbnails, premium layout).

2.0–4.0   Counter accelerates slightly. Text fades in over UI — Funnel Sans Medium, #877F98, small:
           "Your subscribers."
           Then below: "Your income."

4.0–6.0   Cut to: model/creator. Seated, relaxed, confident. Not performing — in ownership mode.
           Phone in hand. Glances at it once, puts it down. They know what it says.

6.0–8.0   Text on black — Funnel Display ExtraBold, #FAF9F6, tracked +20:
           "You decide what they see."
           Two lines. Deliberate spacing. Hold.

8.0–10.0  Cut back to UI — counter continues. New notification populates:
           "New subscriber — @..." — elegant, premium app UX, not gimmicky.

10.0–11.5 Model again — same frame. Slight lift of the chin. That's it. No words needed.

11.5–13.0 Dip to near-black. Hotica logo. Below in #877F98:
           "Own your space."

13.0–14.5 CTA in #FE9FB7:
           "Start earning →"

14.5–15.0 Logo + domain hold. End.

D. BEAT MAP
0.0–4.0   Intro — UI world, counter, income signal — no model yet
4.0–6.0   First interrupt — model enters, the human behind the platform
6.0–8.0   Core message — "You decide what they see." — the emotional center, do not rush
8.0–11.5  Confirmation loop — UI notification + model close
11.5–15.0 Logo, positioning, CTA, hold

E. EDIT LANGUAGE
Pace:             Slower than B1 — 15s conversion ad, let it breathe
Average shot:     2.5–3.0s
Core copy hold:   The text-on-black at 6.0s is the emotional core — do not rush this
UI animations:    Smooth counter tick — premium app physics, no gimmick
Notification:     Fade-in, subtle slide — not a pop or bounce
Film grain:       10%

F. SAFE ASSET GUIDANCE
- Creator framing — no explicit risk
- UI content grid: all thumbnails blurred or safe-framed only
- Notification UI: show only username/subscriber event — no explicit content preview

G. ON-SCREEN COPY
UI labels:        "Your subscribers." / "Your income."
Core copy:        "You decide what they see."
Positioning:      "Own your space."
CTA:              "Start earning →"
Domain:           "hotica.com"

H. VOICE / SUBTITLES / CAPTIONS
Voiceover:        None
IG caption:       "You decide what they see. Build your Hotica page and start earning on your terms. hotica.com"
Short variant:    "Your rules. Your income. hotica.com"
CTA line:         "Link in bio → claim your page."
Hashtags:         #Hotica #CreatorIncome #ContentCreator #OwnYourContent #CreatorEconomy

I. TECHNICAL EXECUTION NOTES
Aspect ratio:     9:16 primary
Counter anim:     60fps interpolation — requestAnimationFrame, smooth easing, not setInterval
Notification UI:  Pixel-perfect dark mode — not a placeholder screenshot
Export:           H.264, CRF 18, 30fps
"""

AD_C1 = """
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
AD C1 — BEFORE. AFTER.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

A. AD IDENTITY
Ad number:       C1
Title:           Before. After.
Purpose:         Lifestyle consideration — contrast and upgrade logic for cold lifestyle audience
Audience:        F 22-32, lifestyle interest, premium app behavioral, cold
Platform:        Instagram Feed + Reels
Duration:        10 seconds

B. CREATIVE CONCEPT
Concept: The same moment, two versions — the before is ordinary, the after is Hotica.
Rationale: The contrast mechanic is the most direct conversion logic in the campaign. It
           gives the viewer a clear before/after framework with no explanation required.
           The "before" is not ugly — it is simply flat. The "after" has the full Hotica
           visual signature: dark, warm, premium.
Emotion:  Mild inadequacy at "before", desire and resolution at "after"
Action:   Upgrade click → features block

C. EXACT TIMELINE
RECOMMENDED: Sequential cut approach (more native to Reels format)

0.0–2.5   Before: flat, ordinary phone scroll — a generic content app. Bright, sterile,
           no personality. Or: same model under flat neutral lighting. No color treatment.
           Ordinary. Muted energy.

2.5–5.0   Hard cut. After: Hotica UI loaded — dark, warm, premium. Or: same model relit
           under golden editorial warmth, dark background. Everything is elevated. The
           visual contrast is immediate and unmistakable.

5.0–7.0   Text fades in over the After frame:
           "Same you."
           Then: "Better access."
           Hold on the premium visual. Let it do the work.

7.0–8.5   Dip to black. Hotica logo.

8.5–10.0  CTA in #FE9FB7:
           "Upgrade your access"
           Domain: "hotica.com"

ALTERNATE: Split-screen approach
- Left (Before): flat, sterile, bright
- Right (After): Hotica dark treatment
- Divider: 1px line at 20% opacity, centered
- Text overlaid on After half

D. BEAT MAP
0.0–2.5   Before — flat, ordinary, low energy
2.5–3.5   Pattern interrupt — hard cut to After, color contrast IS the interrupt
3.5–5.0   Copy lands — "Same you. Better access." — confirm the logic
5.0–7.0   Hold — premium visual settles, viewer sits in the upgrade
7.0–10.0  Logo, CTA, end

E. EDIT LANGUAGE
Core edit:        The Before/After cut — this IS the whole ad
Color contrast:   Must be dramatic but credible — After is premium, not retouched
Film grain:       Apply only to After half — Before is flat, After has texture
No flash cuts:    The contrast IS the pattern interrupt, nothing else needed
Glitch:           PROHIBITED

F. SAFE ASSET GUIDANCE
- Same crop rules if using model: shoulder, jaw, editorial only
- Upgrade is aesthetic and access-based — NOT about revealing more skin in the After
- Hotica UI in After: safe-framed or blurred content thumbnails only

G. ON-SCREEN COPY
Line 1:           "Same you."
Line 2:           "Better access."
CTA:              "Upgrade your access"
Domain:           "hotica.com"

H. VOICE / SUBTITLES / CAPTIONS
Voiceover:        None
IG caption:       "Same you. Better access. The upgrade is real. hotica.com"
Short variant:    "Better access. hotica.com"
CTA line:         "Link in bio."
Hashtags:         #Hotica #UpgradeYourAccess #ExclusiveContent #PremiumAccess #LevelUp

I. TECHNICAL EXECUTION NOTES
Aspect ratio:     9:16 primary, 1:1 secondary
Color grade:      Intentionally flat/desaturated for Before, full Hotica grade for After
Split-screen:     If used, center divider: 1px, #877F98 at 20% opacity
Export:           H.264, CRF 18, 30fps
"""

AD_C2 = """
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
AD C2 — THE ROOM YOU WANT TO BE IN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

A. AD IDENTITY
Ad number:       C2
Title:           The Room You Want To Be In
Purpose:         Cold awareness — aspirational lifestyle entry point
Audience:        Broad lifestyle cold (F 22-32), aspiration interest, fashion/luxury behavioral
Platform:        Instagram Feed + Reels
Duration:        10 seconds

B. CREATIVE CONCEPT
Concept: A rapid editorial montage of premium, desirable moments — none explicit — that
         creates the unmistakable feeling of a room you are not yet in but desperately
         need to be.
Rationale: C2 is the aspirational awareness ad — it sells the feeling before the product.
           The visual grammar is editorial fashion-film: quick but graceful cuts, warm light,
           beautiful restraint. The copy doesn't explain — it confirms what the viewer is
           already feeling.
Emotion:  Aspiration, elevated FOMO, status desire
Action:   Hero CTA → email signup / access

C. EXACT TIMELINE
0.0–1.0   Black. Then: a candle flame catches — warm edge light falls across fabric.
           Indeterminate — shoulder? Room? We don't know. We want to.

1.0–2.0   Cut: a hand trails along a dark surface — marble, glass, or fabric. Elegant. Slow.
           No explicit context.

2.0–3.0   Cut: a door slightly ajar, warm light pouring through. The suggestion of a space
           beyond. Camera doesn't go through the door.

3.0–4.5   Text fades in on near-dark frame — Funnel Display ExtraBold, #FAF9F6, tracked +20:
           "Not everyone gets in."
           Hold 1.5s.

4.5–5.5   Cut: a model — back to camera, standing in warm light. Editorial. Not explicit.
           Just the silhouette of someone who is already inside.

5.5–7.0   Text fades in:
           "You can."
           Two words. Same weight as the first line. Held. This is the turn — from exclusion
           to invitation.

7.0–8.0   Quick editorial flash: one more graceful moment — reflection, fabric movement,
           or hair. Confirmation of the world.

8.0–9.0   Dip to black. Hotica logo.

9.0–10.0  CTA in #FE9FB7:
           "Join the room"
           Domain: "hotica.com"

D. BEAT MAP
0.0–3.0   Intro — 3 editorial mood cuts, establish the world, pure feeling
3.0–4.5   First text — exclusion statement, land it slow
4.5–5.5   Model moment — the human signal, someone is already inside
5.5–7.0   The turn — "You can." — the invitation
7.0–8.0   Confirmation beat — one final editorial flash
8.0–10.0  Logo, CTA, end

E. EDIT LANGUAGE
Average shot:     1.0s in montage, 1.5s on text holds
Total cuts:       5–6 — controlled, not chaotic
Text turns:       "Not everyone gets in." → "You can." — the emotional backbone
Color:            Warmest of all 6 ads — candle warmth, golden editorial, #FFB534 in lighting
Film grain:       15% — matches A1 atmosphere
Cut style:        Every cut is intentional and graceful — no fast cuts, no glitch
Glitch:           PROHIBITED
Vignette:         30% — matches A1

F. SAFE ASSET GUIDANCE
- All clips: editorial framing — fabric, hands, back silhouette, edge light only
- Model at 4.5–5.5: full-back silhouette — zero nudity risk
- "The room" is implied through light and texture — never shown explicitly
- No close-up body parts that could read as voyeuristic

G. ON-SCREEN COPY
Line 1:           "Not everyone gets in."
Line 2:           "You can."
CTA:              "Join the room"
Domain:           "hotica.com"

H. VOICE / SUBTITLES / CAPTIONS
Voiceover:        None
IG caption:       "Not everyone gets in. You can. 🔐 hotica.com"
Short variant:    "The room you want to be in. hotica.com"
CTA line:         "Link in bio."
Hashtags:         #Hotica #ExclusiveAccess #LuxuryContent #PrivateAccess #JoinNow

I. TECHNICAL EXECUTION NOTES
Aspect ratio:     9:16 primary, 1:1 secondary
Color:            Warmest grade of the campaign — this is the invitation ad
Export:           H.264, CRF 18, 30fps
Loop:             Opens and closes on black — seamless loop
"""

POST_PRODUCTION_STYLE_GUIDE = """
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
POST-PRODUCTION MASTER STYLE GUIDE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

COLOR PHILOSOPHY
Target feel:      Luxury fashion film — not social reel, not editorial photo shoot
Black levels:     Crushed but not clipped — target IRE 5 minimum, avoid pure 0
Highlights:       Controlled rolloff — never blown. If blown, fix in grade before export.
Contrast profile: High contrast with gentle shoulder — deep blacks, rich mids, restrained highlights
Skin tone:        Warm — bias toward golden/amber, never orange, never cool-shifted blue
Saturation:       Restrained. Max +10 from neutral. Chroma must feel rich, not neon.
Consistency:      All 6 ads must share a recognizable grade. A1/C2 warmest. B1/B2 cleanest.

GRAIN TREATMENT
Type:             Luminance grain only — no color grain
Opacity:          15% max (A1, C2), 10% (B1, B2), 12% (A2, C1)
Grain size:       Fine — equivalent to ISO 800 film, not ISO 3200
Avoid:            Heavy grain that reads as compression artifact or cheap video look

BLUR STYLE
Blur purpose:     Safety (UI tiles), depth (background defocus), premium feel (lens falloff)
Safety blur:      40px Gaussian minimum on all model UI thumbnails
Lens blur:        Natural — simulate real lens falloff, not Photoshop radial blur
Glass blur:       backdrop-filter blur for overlays only, 12px

ABERRATION POLICY
Chromatic:        None intentionally added — remove if present in source
Lens distortion:  Correct if distracting. Minor barrel distortion acceptable for cinema feel.

TITLE ANIMATION LANGUAGE
Enter:            Fade-in — 0.3–0.5s, never pop
Exit:             Fade-out or cut — never fly out
Motion:           Subtle translateY on enter (8px up to 0) — adds presence without gimmick
Tracking:         All display headlines tracked +15 to +20 in final output
Never:            Typewriter effect, bounce, scale-up entrance, text that "drops in"

SUBTITLE ANIMATION LANGUAGE
Style:            Clean fade-in per line — no word-by-word animation
Font:             Funnel Sans Medium
Size:             Small — supporting, never competing with headline text
Color:            #FAF9F6 or #877F98 depending on importance

TRANSITION FAMILY
Primary:          Dip-to-black — used between major emotional sections
Secondary:        Hard cut — used within fast sequences
Prohibited:       Wipes, slides, spin transitions, iris effects, star wipes

MOTION PRINCIPLES
Camera motion:    Slow, intentional, single direction — never erratic
Pacing rule:      If you're not sure a cut is needed, remove it
Rest principle:   Every ad must have at least one moment where nothing moves for 1+ second
Speed ramp:       One per ad max, at emotional peak only

LUXURY DESIGN PRINCIPLES
1. Withhold — show less, suggest more
2. Rest — premium brands are not afraid of silence or stillness
3. Typography IS the design — when in doubt, let the type carry it
4. One hero moment per ad — identify it, protect it, do not bury it with effects
5. Dark beats light — for Hotica, darkness = premium, not depressing

AVOID-CHEAPNESS CHECKLIST
- No visible platform watermarks (TikTok logo, CapCut badge)
- No bounce or spring animations
- No text shadow with offset — use opacity-reduced glow only if needed
- No gradient text
- No rainbow or multicolor type treatments
- No hard drop shadows on type — flat or nothing
- No emoji in on-screen text (only in IG captions)
- No "swipe up" or "click the link" language in-video
- No cheesy countdown overlays

AVOID-SPAM-AD CHECKLIST
- No "hot girls" or explicit descriptor language
- No body part emojis anywhere in the campaign
- No "18+" badge overlaid on thumbnail — this signals spam
- No flashing price callouts in-video
- No fake celebrity endorsement implication
- No text that reads as affiliate/adult network template
"""

AUDIO_DIRECTION = """
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
AUDIO DIRECTION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

OVERALL MUSIC TREATMENT
Mood reference:   "Magic" by Taylor Belle, "Get High" by Kali Uchis — use as energy reference
                  Do not require exact tracks. License equivalents.
Genre target:     Dark R&B, atmospheric trap, luxury electronic — NOT club, NOT pop, NOT lofi
Tempo:            60–90 BPM feel — never frantic, never boring
Instrumentation:  Sparse — bass, atmospheric pad, occasional melodic element, minimal percussion
Energy curve:     All 6 ads share the same energy arc: quiet intro, build, hold, resolve

PER-BUCKET AUDIO DIRECTION
Bucket A (A1, A2):  Darkest audio — minimal melody, sub bass emphasis, atmospheric tension
                    A1: slower, more ambient — nearly cinematic
                    A2: adds a subtle rhythmic element to support the cut sequence
Bucket B (B1, B2):  Cleanest audio — slightly brighter, suggests confidence and platform energy
                    Still restrained — this is tech-luxury, not hype music
Bucket C (C1, C2):  Warmest audio — golden hour feel, slightly more melodic
                    C2 most musical — the editorial montage needs rhythmic support

SOFT INTRO USAGE
- All ads: music enters at low volume (around -18dB) and fades to target volume (-10dB) within 0.3s
- Never a hard music start — even A2 which has a beat entry should breathe in
- Silence for 0.1–0.3s before music onset on A1 specifically — creates anticipation

BASS EMPHASIS
- Sub bass present on all ads — not booming, but felt on phone speakers
- Mix for earbuds and phone speakers, not theater systems
- Test on iPhone speaker before export — if bass is absent, EQ up

CUT-ON-BREATH MOMENTS
- Place hard cuts on drum hits, bass hits, or breath moments in the music
- A2's 3-cut sequence at 6.0s must land on musical beats — retime if needed

TENSION SILENCES
- A1: 0.1s pre-music silence creates first tension beat
- A2: the pause at 5.0s (unlock fails) should align with a musical pause or dropout
- C2: the "Not everyone gets in." hold should fall in a musical rest or swell

RISERS AND SUB HITS
- A2: one subtle riser leading into the 6.0s cut sequence
- C2: one sub hit when the model silhouette appears at 4.5s
- B2: one gentle swell under the "You decide what they see." moment at 6.0s
- Do not overuse — these are accents, not clichés

REVERSE TAILS
- Allowed on A1 and C2 as subtle audio texture — short, 0.2–0.3s max
- Not on B ads — cleaner audio matches cleaner brand feel

UI SOUNDS
- A2: optional subtle UI click/tap sound when the lock icon appears (0.5s into ad)
- B2: optional subtle notification chime when the subscriber notification appears (8.5s)
- If used: these must be premium, subtle, diegetic — not SFX library sounds

LOUDNESS AND EXPORT
- Target LUFS: -14 LUFS integrated (matches IG/Facebook standard)
- True peak: -1dBTP maximum
- Do not compress to loudness — master gently, allow dynamics
- Vocal ducking: N/A (no voiceover on any ad)

LUXURY POLISH NOTES
- Silence is a tool — use it
- The music should feel like it was commissioned, not found on a free library
- If using royalty-free: use premium libraries (Artlist, Musicbed, Epidemic Sound premium tier)
- Avoid anything that sounds like it was featured in a viral IG reel last month
- The audio should still feel premium in 12 months
"""
