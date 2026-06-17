# Hotica — Landing Page Production Pack
# Generated: 2026-04-22
# Source: landing_pg_only.xml + master.xml (sections 6–9)

LANDING_PAGE_STRATEGY = """
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
LANDING PAGE STRATEGY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

PAGE GOAL
Convert Instagram ad traffic into paying subscribers and creator signups.
The page is a single-page mobile-first experience that mirrors the emotional logic
of each ad — same darkness, same restraint, same access psychology.

TARGET AUDIENCES
1. Consumer (curiosity/lifestyle) — wants access to premium content
2. Creator — wants to monetize content on a premium platform

HOW EACH AD THEME LANDS
- Curiosity traffic (A1, A2): arrives at hero already in desire state — page must not
  reset that state. Maintain mystery. Do not over-explain. Gate the access immediately.
- Creator traffic (B1, B2): arrives motivated by identity and income — direct them to
  the creator section quickly. Show platform credibility before income.
- Lifestyle traffic (C1, C2): arrives with upgrade logic primed — show the contrast
  between regular access and Hotica access in the features section.

PAGE ARCHITECTURE
The page has one emotional arc: you want to be inside → here is what's inside →
you can be inside → unlock.

TRUST STRATEGY
- Never show price in the hero — build desire first
- "For now." on the final CTA creates soft urgency without a countdown timer
- FAQ entry 4 (safety/privacy) is conversion-critical — answer it clearly, not defensively
- Social proof numbers must be real — fake-looking numbers hurt more than no numbers
- Creator section entry 6 in FAQ signals quality control: "we review every application"
  makes the platform feel exclusive from both sides

CONVERSION NOTES
- The blurred preview grid is the single most important conversion element on the page
- Sticky bottom CTA bar on mobile captures scroll-through visitors
- Email capture on final CTA block for users who aren't ready to pay yet
- Creator CTA differentiates from consumer CTA visually (#CBFB05 vs #FE9FB7)
"""

INFORMATION_ARCHITECTURE = """
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
INFORMATION ARCHITECTURE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

SECTION ORDER
1.  Hero                    — immediate access CTA, full viewport
2.  Social proof strip      — subscriber count, creator count, credibility
3.  Private access block    — blurred preview grid, lock/unlock mechanic
4.  Premium experience      — what access gets you (3 feature cards)
5.  Creator invitation      — creator angle: identity, earnings, ownership
6.  FAQ                     — 6 entries, objection handling
7.  Final CTA block         — email capture + primary access CTA
8.  Footer                  — minimal

ENTRY POINT ANCHORS BY AD
A1 → Hero (above fold, #enter)
A2 → Private access block (#unlock)
B1 → Creator section (#create)
B2 → Creator CTA inside creator section (#claim)
C1 → Premium experience / features block (#access)
C2 → Hero (#enter)

URL STRUCTURE
All ads link to: hotica.com/#enter (hero) or hotica.com/#unlock (access block)
Creator ads link to: hotica.com/#create
Deep-link routing: read UTM source param and auto-scroll to matching anchor on load
"""

WIREFRAME = """
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
RESPONSIVE WIREFRAME — SECTION BY SECTION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

─────────────────────────────────────────
SECTION 1: HERO
─────────────────────────────────────────
Purpose:         Stop the scroll. Confirm brand. Drive primary CTA. Match ad energy.
Headline:        "Some things aren't for everyone."
Subheadline:     "Hotica is private. Premium. Built for people who want more."
Primary CTA:     "Enter Hotica" — #FE9FB7 button, full-width mobile, 48px height
Secondary CTA:   "See what's inside ↓" — text link, #877F98, below primary

Layout:          Full viewport height (100dvh). Background: #14101E.
                 Text centered vertically and horizontally.
                 Logo (Hotica wordmark) top-center, 40px from top edge.
Visual:          Option A — editorial video loop of model silhouette at 20-30% opacity
                            behind text. Autoplay, muted, loop. Static fallback for low-bandwidth.
                 Option B — full bleed dark still from ad (collarbone/shoulder editorial)
                            with 60% dark overlay.
Film grain:      15% CSS grain overlay (canvas or SVG filter)
Vignette:        Radial gradient from transparent center to rgba(0,0,0,0.4) at edges
Motion:          Subtle parallax on background (hero only) — translateY at 0.1x scroll rate
Avoid:           Bright backgrounds, explanatory paragraph copy, hero with more than 2 CTAs,
                 price in hero, countdown timer

─────────────────────────────────────────
SECTION 2: SOCIAL PROOF STRIP
─────────────────────────────────────────
Purpose:         Quick credibility signal — does not break mystery, just adds weight
Content:         "12,847 subscribers"  ·  "340+ creators"  ·  "Private by design"
Layout:          Horizontal strip — 56px height. Background: #1D182C.
                 Numbers in #FAF9F6 (Funnel Display Bold, 18px).
                 Labels in #877F98 (Funnel Sans Regular, 12px, uppercase).
                 Mobile: horizontal scroll. Desktop: centered row, equal spacing.
Motion:          Numbers count up once on first view (IntersectionObserver trigger).
                 Duration: 1.2s, ease-out.
CRITICAL NOTE:   Numbers must be real. Remove this section if real numbers aren't available
                 at launch. Fake social proof is worse than no social proof.
Avoid:           Testimonial headshots, star ratings, "as seen in" logos, logo soup

─────────────────────────────────────────
SECTION 3: PRIVATE ACCESS BLOCK
─────────────────────────────────────────
Purpose:         Replicate the A2 ad mechanic — show locked content, drive the unlock.
                 This is the most important conversion section on the page.
Headline:        "Unlock what others can't see."
Subheadline:     "Subscriber-only content from Hotica's most exclusive creators."
Layout:          3x2 blurred thumbnail grid on mobile (2 columns × 3 rows).
                 3x2 or 4x2 on desktop. Each tile:
                   - 40px Gaussian blur minimum
                   - Centered lock icon in #FAF9F6 (SVG, 24px)
                   - Creator name below in #877F98, Funnel Sans Regular, 11px
                   - One tile has "Unlock to view" overlay in #FE9FB7
Background:      #1D182C (elevated from hero surface)
CTA:             "Unlock Access" — #FE9FB7, full-width mobile, 48px height, 12px radius
                 Positioned below grid.
Tap behavior:    Tapping any tile triggers the unlock CTA modal — does not navigate.
Animation:       Tiles fade in sequentially on scroll — stagger 100ms per tile.
CRITICAL NOTE:   This grid must use real Hotica UI design, not placeholder boxes.
                 Placeholder grid = lost conversion. Commission the design before building.
Avoid:           Animated blur removal on hover (feels gimmicky), explicit thumbnails,
                 tiles that link directly to content before payment

─────────────────────────────────────────
SECTION 4: PREMIUM EXPERIENCE
─────────────────────────────────────────
Purpose:         Articulate product value. Give the consumer reasons, not just desire.
Headline:        "What access gets you."
Feature 1:       Icon + "Exclusive creator content"
                 Body: "Private drops. Photos, videos, and more. Only for subscribers."
Feature 2:       Icon + "Direct creator connection"
                 Body: "Message, request, engage. Real access to real creators."
Feature 3:       Icon + "Always fresh"
                 Body: "New content from Hotica's top creators, consistently."
Layout:          Mobile: vertical stack of 3 cards.
                 Desktop: 3-column grid.
Card style:      Background #1D182C, 12px radius, no border, shadow: 0 4px 24px rgba(0,0,0,0.4)
Icon:            Minimal 1.5px stroke SVG, 24px, #FE9FB7
Headline:        Funnel Display Bold, 20px, #FAF9F6
Body:            Funnel Sans Medium, 15px, #877F98, 1.6 line-height
Animation:       Cards fade up on scroll (translateY 20px → 0, opacity 0 → 1, 400ms ease)
Avoid:           Checkmark bullet lists, SaaS feature table format, more than 3 features

─────────────────────────────────────────
SECTION 5: CREATOR INVITATION
─────────────────────────────────────────
Purpose:         Convert creator audience. Show platform value from the creator's perspective.
Anchor:          #create
Headline:        "Build your space."
Subheadline:     "Premium platform. Real income. Your content, your rules."
Features:
  Item 1:  "Your page, your rules" — "Full creative control. Set your price. Define your tiers."
  Item 2:  "Real subscribers, real income" — "No algorithm suppression. Subscribers pay directly."
  Item 3:  "Premium audience" — "Hotica subscribers are committed. They're here to pay, not browse."
CTA:             "Claim Your Page →" — #CBFB05 (UV Green), text #14101E
                 This color difference from the consumer CTA (#FE9FB7) is intentional —
                 it visually separates the two conversion paths.
Layout:          Dark section with slight warm tint (#1D182C). Headline dominant. 3-item list.
                 CTA below.
Anchor tag:      id="create" on section element
Avoid:           Leading with income before identity, generic "creator economy" language,
                 income projections without basis

─────────────────────────────────────────
SECTION 6: FAQ
─────────────────────────────────────────
Purpose:         Handle the 6 highest-friction objections before they block conversion.
Headline:        "Questions."
Layout:          Accordion. Mobile: touch targets 48px minimum height.
                 Each item: subtle bottom divider (1px, #877F98 at 15% opacity).
                 Questions: Funnel Display Bold, 17px, #FAF9F6.
                 Answers: Funnel Sans Medium, 15px, #877F98, 1.6 line-height.
Animation:       Smooth height expand/collapse, 250ms ease — no jumping

Entry 1:
  Q: "Is Hotica really private?"
  A: "Yes. Your profile, your activity, and your subscriptions are never public. Hotica is
      built for discretion."

Entry 2:
  Q: "What kind of content is on Hotica?"
  A: "Exclusive creator content — photos, videos, and direct access — from creators who
      make content specifically for Hotica subscribers."

Entry 3:
  Q: "Is it expensive?"
  A: "Access starts at [PRICE]. Less than a dinner. More than you'd expect."
  NOTE: Fill [PRICE] before launch. This entry must be real — placeholder copy loses trust.

Entry 4:
  Q: "Is it safe to sign up?"
  A: "Completely. Hotica uses encrypted payment processing and never shares your information."

Entry 5:
  Q: "Can I cancel anytime?"
  A: "Yes. No contracts, no questions, no friction."

Entry 6:
  Q: "I'm a creator. How do I join?"
  A: "Apply through the creator portal. We review every application. We only accept creators
      who match the platform's quality bar."

─────────────────────────────────────────
SECTION 7: FINAL CTA BLOCK
─────────────────────────────────────────
Purpose:         Last conversion opportunity. Echo the hero energy. Soft urgency.
Headline:        "The door is open."
Subheadline:     "For now."
                 NOTE: Do not replace "For now." with a countdown timer. The line works
                 because it is ambiguous and premium. A timer is cheap.
Primary CTA:     "Enter Hotica" — #FE9FB7, large, full-width mobile, 56px height
Email capture:   Below CTA: "Or enter your email to reserve early access →"
                 Input field: dark border (#877F98), #1D182C background, #FAF9F6 text
                 Submit: "Reserve" in #877F98, inline
                 Privacy line below: "We respect your privacy. No spam." — #877F98, 12px
Background:      #14101E — deep dark, echoes hero
Motion:          No animation on this section — stillness = gravity

─────────────────────────────────────────
SECTION 8: FOOTER
─────────────────────────────────────────
Purpose:         Legal compliance, secondary navigation. Not a design moment.
Content:         Hotica logo (small, 24px height) | Privacy Policy | Terms | Creator Portal | Contact
Layout:          Single row on desktop, stacked on mobile. Centered.
Colors:          #877F98 text on #14101E background.
Font:            Funnel Sans Regular, 13px
Avoid:           Social media icons, excessive links, newsletter signup, cookie popups that
                 break the experience (use a minimal compliant banner instead)
"""

UI_DESIGN_SYSTEM = """
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
UI DESIGN SYSTEM
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

DESIGN DIRECTION
Premium luxury-tech with fashion-editorial restraint. Dark. Controlled. Confident.
The visual language says: this platform knows exactly what it is. No clutter.
No explanations. No design choices that apologize for themselves.

GRID SYSTEM
Mobile:   4 columns, 16px gutter, 16px margin
Tablet:   8 columns, 24px gutter, 32px margin
Desktop:  12 columns, 24px gutter, max-width 1200px, centered

SPACING SCALE
4px / 8px / 12px / 16px / 24px / 32px / 48px / 64px / 96px / 128px

SURFACE HIERARCHY
Level 0 (deepest):  #14101E — page background, hero, final CTA
Level 1:            #1D182C — sections, cards, sidebars
Level 2:            #261F39 — elevated cards, modals, dropdowns
Level 3:            #392E59 — highest surface, selected states, active indicators

CARD STYLE
Background:   #1D182C
Border:       None (use elevation via shadow only)
Radius:       12px
Shadow:       box-shadow: 0 4px 24px rgba(0,0,0,0.4)
Padding:      24px mobile, 32px desktop

RADIUS PHILOSOPHY
Buttons:      12px (premium rounded, not pill, not sharp)
Cards:        12px
Inputs:       8px
Modals:       20px
Section cont: 0px (full-bleed sections, no container radius)

SHADOW PHILOSOPHY
Only dark shadows — never light/white/colored shadows
Standard:     0 4px 24px rgba(0,0,0,0.4)
Modal:        0 16px 64px rgba(0,0,0,0.6)
No inset shadows. No drop shadows on text (use opacity instead).

BLUR / GLASS POLICY
Use only for overlay panels and modals — backdrop-filter: blur(12px) on rgba(20,16,30,0.8)
Do not blur section backgrounds — this is not a glassmorphism campaign
Blurred content thumbnails: Gaussian blur 40px minimum (CSS filter: blur(40px))

LINE STYLE
Dividers:     1px solid rgba(135,127,152,0.15) — barely visible, structural only
No decorative lines. No underlines on headlines. No borders on cards.

BUTTON SYSTEM
Primary (consumer):
  Background: #FE9FB7
  Text:       #14101E (Funnel Display Bold, 16px, letter-spacing +1px)
  Height:     48px mobile, 52px desktop
  Radius:     12px
  Width:      Full-width on mobile, auto (min 200px) on desktop
  Hover:      scale(1.02), transition 200ms ease
  Press:      scale(0.98), transition 100ms ease

Secondary:
  Background: transparent
  Border:     1px solid rgba(135,127,152,0.5)
  Text:       #FAF9F6 (Funnel Sans Medium, 15px)
  Same sizing as primary
  Hover:      border-color: #FAF9F6, transition 200ms

Creator CTA:
  Background: #CBFB05
  Text:       #14101E (Funnel Display Bold, 16px, letter-spacing +1px)
  Same sizing as primary
  Used only for creator conversion CTAs — not interchangeable with primary

ICON STYLE
Style:        Minimal stroke icons, 1.5px weight, 24x24px grid
Color:        #FE9FB7 for feature icons, #FAF9F6 for UI icons, #877F98 for secondary
Library:      Custom or Lucide (clean, minimal) — no filled icons, no emoji-style icons

HOVER AND PRESS BEHAVIOR
All buttons:  scale transform — see button system above
Links:        color: #FAF9F6 on hover, transition 150ms
Cards:        subtle translateY(-2px) on hover, transition 200ms — optional, use sparingly

MOBILE NAV
Type:         None (single-page app — no navigation bar needed)
Exception:    Sticky bottom CTA bar — appears after 30% scroll
              Content: "Enter Hotica" (primary button, full-width minus 32px margin)
              Background: rgba(20,16,30,0.95) with backdrop-filter: blur(8px)
              Height: 72px (includes 12px safe area at bottom for iPhone home indicator)

ANIMATION AND MOTION LANGUAGE
Entrance:     translateY(20px) → translateY(0) + opacity 0 → 1
Duration:     400ms ease for cards/sections, 250ms ease for UI elements
Trigger:      IntersectionObserver, threshold 0.15 — never scroll event listener
Stagger:      100ms between sibling elements (used in grid tiles, feature cards)
No GSAP required — CSS transitions + IntersectionObserver sufficient

MODAL / OVERLAY STYLE
Background:   rgba(20,16,30,0.8) + backdrop-filter: blur(16px)
Panel:        #1D182C surface, 20px radius, max-height 90dvh, overflow-y scroll
Width:        90vw mobile, 480px desktop, centered
Close button: top-right, 40x40px tap target, X icon in #877F98
Animation:    scale(0.95) + opacity 0 → scale(1) + opacity 1, 250ms ease
"""

COLOR_SYSTEM = """
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
COLOR SYSTEM
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

ROLE                | TOKEN NAME        | HEX     | CSS VAR
Primary background  | Darkest Desire    | #14101E | --color-bg-primary
Secondary BG        | Purple Haze       | #1D182C | --color-bg-secondary
Elevated surface    | Sunset Purple     | #261F39 | --color-bg-elevated
Deep elevated       | Phangan Purple    | #392E59 | --color-bg-deep
Primary accent      | Pink Bubblegum    | #FE9FB7 | --color-accent-primary
Creator accent      | UV Green          | #CBFB05 | --color-accent-creator
Warm highlight      | Warm Sun          | #FFB534 | --color-accent-warm
Destructive         | UV Red            | #F11E5D | --color-destructive
Primary text        | Off White         | #FAF9F6 | --color-text-primary
Secondary text      | Muted White       | #877F98 | --color-text-secondary
Divider             | Muted White 15%   | rgba(135,127,152,0.15) | --color-divider

USAGE RULES
- Primary accent (#FE9FB7) on consumer CTAs only — do not scatter it across decorative elements
- Creator accent (#CBFB05) on creator CTAs only — the contrast signals a different path
- Warm Sun (#FFB534) for editorial warmth accents in specific sections — use sparingly
- UV Red (#F11E5D) for destructive/error states only — not for emphasis
- Never use white (#FFFFFF) — use Off White (#FAF9F6) as the lightest text color
- Never use black (#000000) as a background — use Darkest Desire (#14101E)
"""

TYPOGRAPHY_SYSTEM = """
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
TYPOGRAPHY SYSTEM
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

FONTS
Primary display:  Funnel Display (ExtraBold 800, Bold 700) — Google Fonts
Body:             Funnel Sans (Medium 500, Regular 400) — Google Fonts
UI/labels:        Funnel Sans Regular 400 — smaller sizes, uppercase labels
No fallback fonts beyond system sans-serif — if Funnel Display fails, the brand fails

TYPE SCALE
Role             | Font                  | Weight | Mobile | Desktop | Leading | Tracking
Hero headline    | Funnel Display        | 800    | 40px   | 64px    | 1.0     | -0.02em
Section headline | Funnel Display        | 700    | 28px   | 40px    | 1.1     | -0.01em
Card headline    | Funnel Display        | 700    | 20px   | 24px    | 1.2     | 0
Body             | Funnel Sans           | 500    | 16px   | 18px    | 1.6     | 0
Caption/label    | Funnel Sans           | 400    | 12px   | 13px    | 1.4     | +0.05em
CTA text         | Funnel Display        | 700    | 16px   | 17px    | 1.0     | +0.05em
FAQ question     | Funnel Display        | 700    | 17px   | 18px    | 1.2     | 0
FAQ answer       | Funnel Sans           | 500    | 15px   | 16px    | 1.6     | 0

ALIGNMENT
Hero text:        Center — this is the only centered section
All other text:   Left-aligned on mobile and desktop
CTA buttons:      Text centered within button

CAPITALIZATION
Headlines:        Sentence case — never ALL CAPS for full headlines (feels cheap)
Labels/caps:      Uppercase for small UI labels only (e.g. "SUBSCRIBER ONLY")
CTAs:             Sentence case — "Enter Hotica", not "ENTER HOTICA"

LUXURY FASHION-TECH TONE
- Tight leading on display headlines — condensed, powerful
- Generous tracking (+0.05em) on CTA text — expands the action word, feels intentional
- Never use more than 2 type sizes in a single card
- The whitespace around type IS part of the design — do not compress it
- When in doubt: bigger headline, smaller body, more space between them
"""

COPY_DECK = """
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
COPY DECK — LANDING PAGE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

HERO
Headline:         "Some things aren't for everyone."
Subheadline:      "Hotica is private. Premium. Built for people who want more."
Primary CTA:      "Enter Hotica"
Secondary CTA:    "See what's inside ↓"

SOCIAL PROOF STRIP
"12,847 subscribers  ·  340+ creators  ·  Private by design"

PRIVATE ACCESS BLOCK
Headline:         "Unlock what others can't see."
Subheadline:      "Subscriber-only content from Hotica's most exclusive creators."
Tile overlay:     "Unlock to view"
CTA:              "Unlock Access"

PREMIUM EXPERIENCE
Headline:         "What access gets you."

Feature 1:
  Title:  "Exclusive creator content"
  Body:   "Private drops. Photos, videos, and more. Only for subscribers."

Feature 2:
  Title:  "Direct creator connection"
  Body:   "Message, request, engage. Real access to real creators."

Feature 3:
  Title:  "Always fresh"
  Body:   "New content from Hotica's top creators, consistently."

CREATOR INVITATION
Headline:         "Build your space."
Subheadline:      "Premium platform. Real income. Your content, your rules."

Feature 1:
  Title:  "Your page, your rules"
  Body:   "Full creative control. Set your price. Define your access tiers."

Feature 2:
  Title:  "Real subscribers, real income"
  Body:   "No algorithm suppression. Subscribers pay directly. You earn."

Feature 3:
  Title:  "Premium audience"
  Body:   "Hotica subscribers are committed. They're here to pay, not browse."

CTA:              "Claim Your Page →"

FAQ
Headline:         "Questions."

Q1: "Is Hotica really private?"
A1: "Yes. Your profile, your activity, and your subscriptions are never public.
     Hotica is built for discretion."

Q2: "What kind of content is on Hotica?"
A2: "Exclusive creator content — photos, videos, and direct access — from creators
     who make content specifically for Hotica subscribers."

Q3: "Is it expensive?"
A3: "Access starts at [PRICE]. Less than a dinner. More than you'd expect."
    [FILL BEFORE LAUNCH]

Q4: "Is it safe to sign up?"
A4: "Completely. Hotica uses encrypted payment processing and never shares your information."

Q5: "Can I cancel anytime?"
A5: "Yes. No contracts, no questions, no friction."

Q6: "I'm a creator. How do I join?"
A6: "Apply through the creator portal. We review every application. We only accept
     creators who match the platform's quality bar."

FINAL CTA BLOCK
Headline:         "The door is open."
Subheadline:      "For now."
CTA:              "Enter Hotica"
Email label:      "Or enter your email to reserve early access →"
Privacy note:     "We respect your privacy. No spam."

FOOTER
Nav links:        Privacy Policy  ·  Terms  ·  Creator Portal  ·  Contact
Tagline (opt):    "Turn up the heat."

MOBILE INTERACTION NOTES
- Hero CTA must be fully visible on iPhone SE (375px × 667px) above the fold
- Sticky bottom CTA bar appears after 30% scroll — "Enter Hotica" button
- FAQ accordion: 48px minimum touch target per item
- Blurred grid tiles: tap triggers unlock CTA modal, not navigation
- Use IntersectionObserver for all scroll animations — NOT scroll event listeners
- No horizontal scroll except the social proof strip (intentional, snapped)
- Tap highlight color: rgba(254,159,183,0.1) — subtle pink on iOS tap

WHAT TO AVOID
- White or light backgrounds at any point in the page
- Testimonial carousels with headshots and star ratings
- Price in the hero section
- Countdown timers (use "For now." instead)
- "Limited time offer" language
- Generic stock photography
- Any content grid that reads as explicit on a quick scroll
- SaaS-style feature tables with checkmark lists
- Footer with 40+ links
- Cookie popups that cover the hero on first load
- Auto-playing audio
- Animations that run on every scroll (set once with IntersectionObserver)
"""
