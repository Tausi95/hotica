#!/usr/bin/env python3
"""
Data Science in Project Management - Animated Video Generator
Produces: data_science_pm.mp4 (~32 seconds, 1280x720, 30fps)
Uses: Pillow + ffmpeg  (no Manim/MoviePy required)
"""

from PIL import Image, ImageDraw, ImageFont
import os, subprocess, math, shutil

# ── CONFIG ────────────────────────────────────────────────────────────────────
W, H   = 1280, 720
FPS    = 30
FRAMES = "/tmp/ds_pm_frames"
OUTPUT = "/home/mage107/Documents/projects/hotica/data_science_pm.mp4"

REG_TTF  = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
BOLD_TTF = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"

# ── COLORS ────────────────────────────────────────────────────────────────────
BG     = (8,  8,  25)
BG2    = (18, 18, 50)
CYAN   = (0,  200, 255)
RED    = (255, 75,  75)
YEL    = (255, 210, 50)
GRN    = (72,  210, 110)
WHITE  = (255, 255, 255)
LGRAY  = (170, 170, 200)
GRAY   = (100, 100, 140)
PURP   = (165, 85,  255)
ORNG   = (255, 145, 45)
BLUE   = (55,  135, 255)
TEAL   = (0,   175, 175)

# ── FONTS ─────────────────────────────────────────────────────────────────────
SIZES = [15, 16, 17, 18, 19, 20, 22, 24, 26, 28, 30, 32, 36, 40, 44, 48, 56, 64, 72, 80]
FR, FB = {}, {}
for s in SIZES:
    FR[s] = ImageFont.truetype(REG_TTF,  s)
    FB[s] = ImageFont.truetype(BOLD_TTF, s)

# ── MATH HELPERS ──────────────────────────────────────────────────────────────
def ease(t):
    t = max(0.0, min(1.0, t))
    return t * t * (3 - 2 * t)

def ease_out(t):
    t = max(0.0, min(1.0, t))
    return 1 - (1 - t) ** 2

def prog(frame, start, end):
    """Return 0..1 progress of frame within [start, end]."""
    if end <= start:
        return 1.0
    return max(0.0, min(1.0, (frame - start) / (end - start)))

# ── DRAW HELPERS ──────────────────────────────────────────────────────────────
def blend(color, alpha, bg=BG):
    return tuple(int(color[i] * alpha + bg[i] * (1 - alpha)) for i in range(3))

def tsz(draw, text, font):
    """PIL-7 compatible text size."""
    return draw.textsize(text, font=font)

def center_text(draw, cx, cy, text, font, color):
    tw, th = tsz(draw, text, font)
    draw.text((cx - tw // 2, cy - th // 2), text, font=font, fill=color)

def left_text(draw, x, cy, text, font, color):
    _, th = tsz(draw, text, font)
    draw.text((x, cy - th // 2), text, font=font, fill=color)

def rrect(draw, x1, y1, x2, y2, r, fill=None, outline=None, lw=2):
    """Rounded rectangle — Pillow-7 compatible."""
    if fill:
        draw.rectangle([x1 + r, y1, x2 - r, y2], fill=fill)
        draw.rectangle([x1, y1 + r, x2, y2 - r], fill=fill)
        for ex, ey in [(x1, y1), (x2 - 2*r, y1), (x1, y2 - 2*r), (x2 - 2*r, y2 - 2*r)]:
            draw.ellipse([ex, ey, ex + 2*r, ey + 2*r], fill=fill)
    if outline:
        draw.arc([x1, y1, x1+2*r, y1+2*r], 180, 270, fill=outline, width=lw)
        draw.arc([x2-2*r, y1, x2, y1+2*r], 270, 360, fill=outline, width=lw)
        draw.arc([x1, y2-2*r, x1+2*r, y2], 90,  180, fill=outline, width=lw)
        draw.arc([x2-2*r, y2-2*r, x2, y2], 0,   90,  fill=outline, width=lw)
        draw.line([(x1+r, y1), (x2-r, y1)],     fill=outline, width=lw)
        draw.line([(x1+r, y2), (x2-r, y2)],     fill=outline, width=lw)
        draw.line([(x1, y1+r), (x1, y2-r)],     fill=outline, width=lw)
        draw.line([(x2, y1+r), (x2, y2-r)],     fill=outline, width=lw)

def gradient_bg(img):
    draw = ImageDraw.Draw(img)
    for y in range(H):
        t = y / H
        r = int(BG[0] + (BG2[0] - BG[0]) * t)
        g = int(BG[1] + (BG2[1] - BG[1]) * t)
        b = int(BG[2] + (BG2[2] - BG[2]) * t)
        draw.line([(0, y), (W, y)], fill=(r, g, b))

def particles(draw, frame, n=20, col=CYAN, a=0.1):
    import random
    rng = random.Random(99)
    for _ in range(n):
        sx, sy = rng.randint(0, W), rng.randint(0, H)
        spd = rng.uniform(0.2, 1.0)
        sz  = rng.randint(1, 3)
        x = (sx + frame * spd * 0.4) % W
        y = (sy - frame * spd * 0.2) % H
        c = blend(col, a * rng.uniform(0.4, 1.0))
        draw.ellipse([x-sz, y-sz, x+sz, y+sz], fill=c)

def header(draw, title, sub=None, a=1.0):
    tw, th = tsz(draw, title, FB[56])
    cx = W // 2
    draw.text((cx - tw//2, 55 - th//2), title, font=FB[56], fill=blend(WHITE, a))
    lw = int(tw * a)
    draw.line([(cx-lw//2, 90), (cx+lw//2, 90)], fill=blend(CYAN, a*0.6), width=3)
    if sub:
        sw, sh = tsz(draw, sub, FR[24])
        draw.text((cx - sw//2, 112 - sh//2), sub, font=FR[24], fill=blend(LGRAY, a*0.8))

def divider(draw, y, a=1.0):
    draw.line([(80, y), (W-80, y)], fill=blend(CYAN, a*0.25), width=1)

def new_frame():
    img = Image.new("RGB", (W, H), BG)
    gradient_bg(img)
    return img

# ── SCENE 1 · TITLE  (frames 0-89) ───────────────────────────────────────────
def s_title(f):
    t  = f / 89
    img = new_frame(); d = ImageDraw.Draw(img)
    particles(d, f, 30, CYAN, 0.12)

    cx, cy = W // 2, H // 2
    pulse = math.sin(f * 0.1) * 0.5 + 0.5
    for r in [230, 195, 160]:
        d.ellipse([cx-r, cy-r+10, cx+r, cy+r+10],
                  outline=blend(CYAN, 0.04 + pulse*0.02), width=1)

    # Main title
    ta = ease(min(1, t * 2.5))
    tw, th = tsz(d, "DATA SCIENCE", FB[80])
    d.text((cx - tw//2, cy - 95 - th//2), "DATA SCIENCE", font=FB[80], fill=blend(CYAN, ta))
    if ta > 0.05:
        llen = int(tw * ta)
        d.line([(cx-llen//2, cy-95+th//2+10), (cx+llen//2, cy-95+th//2+10)],
               fill=blend(CYAN, ta), width=3)

    # Subtitle
    sa = ease(max(0, (t-0.2)*2))
    sub = "FOR PROJECT MANAGEMENT PROFESSIONALS"
    sw, sh = tsz(d, sub, FR[30])
    d.text((cx-sw//2, cy-5-sh//2), sub, font=FR[30], fill=blend(WHITE, sa*0.9))

    # Tagline
    ga = ease(max(0, (t-0.4)*2))
    tag = "Tools  |  Concepts  |  Applications"
    gw, gh = tsz(d, tag, FB[32])
    d.text((cx-gw//2, cy+60-gh//2), tag, font=FB[32], fill=blend(YEL, ga))

    # Bottom border sweep
    bw = int(W * ease(t))
    d.line([(cx-bw//2, H-35), (cx+bw//2, H-35)], fill=blend(CYAN, 0.5), width=2)
    return img

# ── SCENE 2 · WHAT IS DATA SCIENCE?  (frames 90-209) ─────────────────────────
def s_what(f):
    t  = prog(f, 90, 209)
    img = new_frame(); d = ImageDraw.Draw(img)
    particles(d, f, 18, BLUE, 0.07)

    ha = ease(min(1, t*3))
    header(d, "What is Data Science?", a=ha)
    divider(d, 130, ha)

    # Definition box
    da = ease(max(0, (t-0.2)*2.5))
    if da > 0:
        rrect(d, 80, 150, W-80, 245, 12,
              fill=blend((18, 28, 60), da),
              outline=blend(CYAN, da*0.45))
        lines = [
            ("An interdisciplinary field that combines statistics, programming &", FR[26], WHITE, 183),
            ("domain knowledge to extract insights and drive data-driven decisions.", FR[26], LGRAY, 213),
        ]
        for txt, fnt, col, y in lines:
            tw, th = tsz(d, txt, fnt)
            d.text((W//2-tw//2, y-th//2), txt, font=fnt, fill=blend(col, da))

    # Three pillars
    pillars = [
        (210,  "Statistics &\nMathematics", CYAN,  "Probability  •  Regression\nHypothesis Testing"),
        (W//2, "Programming\n& Tools",      PURP,  "Python  •  R  •  SQL\nVisualization Libraries"),
        (W-210,"Domain\nKnowledge",         GRN,   "Industry context\nBusiness understanding"),
    ]
    for i, (px, name, col, desc) in enumerate(pillars):
        pa = ease(max(0, (t - 0.3 - i*0.15)*3))
        if pa > 0:
            py = 460
            cw, ch = 240, 195
            rrect(d, px-cw//2, py-ch//2, px+cw//2, py+ch//2, 14,
                  fill=blend(col, pa*0.12), outline=blend(col, pa*0.7))
            # Icon circle
            ir = 26
            d.ellipse([px-ir, py-80-ir, px+ir, py-80+ir], fill=blend(col, pa*0.8))
            # Name
            for j, ln in enumerate(name.split('\n')):
                lw2, lh2 = tsz(d, ln, FB[26])
                d.text((px-lw2//2, py-32+j*30-lh2//2), ln, font=FB[26], fill=blend(col, pa))
            # Desc
            for j, ln in enumerate(desc.split('\n')):
                lw2, lh2 = tsz(d, ln, FR[19])
                d.text((px-lw2//2, py+38+j*23-lh2//2), ln, font=FR[19], fill=blend(LGRAY, pa*0.8))
    return img

# ── SCENE 3 · FIELDS  (frames 210-329) ────────────────────────────────────────
def s_fields(f):
    t  = prog(f, 210, 329)
    img = new_frame(); d = ImageDraw.Draw(img)
    particles(d, f, 18, PURP, 0.07)

    ha = ease(min(1, t*3))
    header(d, "Data Science Across Industries", a=ha)
    divider(d, 130, ha)

    fields = [
        (160,    "Healthcare",        RED,  "Diagnosis\nOutcomes\nDrug Discovery"),
        (380,    "Finance",           YEL,  "Risk Modeling\nFraud Detection\nTrading"),
        (W//2,   "Marketing",         ORNG, "Segmentation\nCampaign Analytics\nCLV"),
        (W-380,  "Manufacturing",     BLUE, "Quality Control\nPred. Maintenance\nIoT"),
        (W-160,  "Project Mgmt",      GRN,  "Risk & Resources\nSchedule & Budget\nKPIs"),
    ]

    for i, (px, name, col, desc) in enumerate(fields):
        fa = ease(max(0, (t - 0.1 - i*0.12)*3))
        if fa > 0:
            is_pm = (i == 4)
            r = 78 if is_pm else 62
            py = 410

            # Glow ring for PM
            if is_pm:
                for gr in [r+22, r+14]:
                    d.ellipse([px-gr, py-gr, px+gr, py+gr],
                              outline=blend(col, fa*0.18), width=2)

            d.ellipse([px-r, py-r, px+r, py+r],
                      fill=blend(col, fa*(0.22 if is_pm else 0.13)),
                      outline=blend(col, fa*(1.0 if is_pm else 0.65)),
                      width=3 if is_pm else 2)

            if is_pm:
                sw2, sh2 = tsz(d, "FOCUS", FB[18])
                d.text((px-sw2//2, py-r-28-sh2//2), "FOCUS", font=FB[18], fill=blend(YEL, fa))

            # Name
            font_n = FB[26] if is_pm else FB[22]
            tw2, th2 = tsz(d, name, font_n)
            d.text((px-tw2//2, py-th2//2-4), name, font=font_n, fill=blend(col, fa))

            # Description below
            dy = py + r + 22
            for j, ln in enumerate(desc.split('\n')):
                lw2, lh2 = tsz(d, ln, FR[17])
                d.text((px-lw2//2, dy+j*21-lh2//2), ln, font=FR[17], fill=blend(LGRAY, fa*0.8))

    # Footer note
    na = ease(max(0, (t-0.85)*5))
    if na > 0:
        note = "Our focus  >>  Project Management"
        nw, nh = tsz(d, note, FB[28])
        d.text((W//2-nw//2, H-52-nh//2), note, font=FB[28], fill=blend(GRN, na))
    return img

# ── SCENE 4 · PM FOCUS  (frames 330-509) ──────────────────────────────────────
def s_pm(f):
    t  = prog(f, 330, 509)
    img = new_frame(); d = ImageDraw.Draw(img)
    particles(d, f, 18, GRN, 0.07)

    ha = ease(min(1, t*3))
    header(d, "Data Science in Project Management", a=ha)
    divider(d, 130, ha)

    cases = [
        ("RISK\nASSESSMENT",      RED,  "Identify & quantify risks\nbefore they occur",           "◆"),
        ("RESOURCE\nPLANNING",    BLUE, "Optimize team allocation\n& capacity planning",           "="),
        ("SCHEDULE\nOPTIMIZATION",CYAN, "Forecast delays & critical\npath analysis",               ">>>"),
        ("BUDGET\nFORECASTING",   YEL,  "Predict cost overruns\n& control spend",                  "$"),
        ("KPI\nTRACKING",         GRN,  "Monitor performance &\nproject health metrics",           "o"),
    ]
    positions = [(180,340),(500,340),(820,340),(330,565),(700,565)]

    for i, ((name, col, desc, icon), (px, py)) in enumerate(zip(cases, positions)):
        ca = ease(max(0, (t - 0.12 - i*0.12)*3))
        if ca > 0:
            cw, ch = 255, 175
            rrect(d, px-cw//2, py-ch//2, px+cw//2, py+ch//2, 12,
                  fill=blend(col, ca*0.10), outline=blend(col, ca*0.70))
            # Icon
            iw, ih = tsz(d, icon, FB[28])
            d.text((px-iw//2, py-65-ih//2), icon, font=FB[28], fill=blend(col, ca))
            # Name lines
            for j, ln in enumerate(name.split('\n')):
                lw2, lh2 = tsz(d, ln, FB[22])
                d.text((px-lw2//2, py-12+j*26-lh2//2), ln, font=FB[22], fill=blend(col, ca))
            # Desc
            for j, ln in enumerate(desc.split('\n')):
                lw2, lh2 = tsz(d, ln, FR[18])
                d.text((px-lw2//2, py+50+j*22-lh2//2), ln, font=FR[18], fill=blend(LGRAY, ca*0.85))
    return img

# ── SCENE 5 · ANALYTICS CONCEPTS  (frames 510-659) ────────────────────────────
def s_concepts(f):
    t  = prog(f, 510, 659)
    img = new_frame(); d = ImageDraw.Draw(img)
    particles(d, f, 18, YEL, 0.07)

    ha = ease(min(1, t*3))
    header(d, "4 Types of Data Analytics", a=ha)
    divider(d, 130, ha)

    analytics = [
        ("Descriptive",  CYAN, "What\nhappened?",    "Dashboards, Reports\nHistorical Analysis", "Past performance\nsummaries"),
        ("Diagnostic",   ORNG, "Why did it\nhappen?","Root Cause Analysis\nCorrelation Studies", "Delay cause\nanalysis"),
        ("Predictive",   PURP, "What will\nhappen?", "ML Models, Forecasting\nRisk Scoring",      "Risk &\nprediction"),
        ("Prescriptive", GRN,  "What should\nwe do?","Optimization\nDecision Support",            "Resource\noptimization"),
    ]

    spacing = (W - 140) // 4
    x0 = 70 + spacing // 2

    for i, (atype, col, question, examples, pm) in enumerate(analytics):
        px  = x0 + i * spacing
        delay = 0.12 + i * 0.14
        a   = ease(max(0, (t - delay) * 3))
        if a <= 0:
            continue

        by, bh = 160, 430
        bw = spacing - 28

        # Card
        rrect(d, px-bw//2, by, px+bw//2, by+bh, 12,
              fill=blend(col, a*0.11), outline=blend(col, a*0.65))

        # Number badge
        d.ellipse([px-22, by-22, px+22, by+22], fill=blend(col, a*0.9))
        nw, nh = tsz(d, str(i+1), FB[24])
        d.text((px-nw//2, by-nh//2), str(i+1), font=FB[24], fill=blend(BG, 1.0, col))

        # Type name
        aw, ah = tsz(d, atype, FB[24])
        d.text((px-aw//2, by+50-ah//2), atype, font=FB[24], fill=blend(col, a))

        # Question
        for j, ln in enumerate(question.split('\n')):
            lw2, lh2 = tsz(d, ln, FR[20])
            d.text((px-lw2//2, by+90+j*24-lh2//2), ln, font=FR[20], fill=blend(WHITE, a*0.9))

        # Divider
        da2 = ease(max(0, (t-delay-0.1)*4))
        dlen = int((bw-32)*da2)
        if dlen > 0:
            d.line([(px-dlen//2, by+160), (px+dlen//2, by+160)],
                   fill=blend(col, a*0.35), width=1)

        # Examples
        for j, ln in enumerate(examples.split('\n')):
            lw2, lh2 = tsz(d, ln, FR[17])
            d.text((px-lw2//2, by+185+j*22-lh2//2), ln, font=FR[17], fill=blend(LGRAY, a*0.8))

        # PM context label
        pa2 = ease(max(0, (t-delay-0.25)*4))
        if pa2 > 0:
            pw, ph = tsz(d, "PM context:", FB[16])
            d.text((px-bw//2+14, by+295), "PM context:", font=FB[16], fill=blend(col, pa2*0.7))
            for j, ln in enumerate(pm.split('\n')):
                lw2, lh2 = tsz(d, ln, FR[17])
                d.text((px-lw2//2, by+325+j*22-lh2//2), ln, font=FR[17], fill=blend(col, pa2*0.6))

        # Arrow to next
        if i < 3:
            arr_a = ease(max(0, (t - delay - 0.12)*4))
            if arr_a > 0:
                ax = px + spacing // 2
                ay = by + bh // 2
                ac = blend(GRAY, arr_a * 0.5)
                d.line([(ax-18, ay), (ax+12, ay)], fill=ac, width=2)
                d.polygon([(ax+12, ay-6), (ax+12, ay+6), (ax+25, ay)], fill=ac)
    return img

# ── SCENE 6 · TOOLS  (frames 660-869) ─────────────────────────────────────────
def s_tools(f):
    t  = prog(f, 660, 869)
    img = new_frame(); d = ImageDraw.Draw(img)
    particles(d, f, 18, ORNG, 0.07)

    ha = ease(min(1, t*3))
    header(d, "Essential Tools for PM Data Science", a=ha)
    divider(d, 130, ha)

    tools = [
        {
            "name":  "Excel / Google Sheets",
            "cat":   "Spreadsheets",
            "col":   GRN,
            "level": "Beginner Friendly",
            "uses":  ["Data entry & cleaning", "Pivot tables & formulas", "Basic charts & visuals", "VLOOKUP  |  IF  |  INDEX"],
        },
        {
            "name":  "Power BI / Tableau",
            "cat":   "Visualization",
            "col":   YEL,
            "level": "Intermediate",
            "uses":  ["Interactive dashboards", "Real-time project reports", "Drill-down analysis", "Sharing & publishing"],
        },
        {
            "name":  "Python / R",
            "cat":   "Programming",
            "col":   CYAN,
            "level": "Advanced",
            "uses":  ["pandas, numpy, scikit-learn", "Statistical modeling", "Machine learning & ML", "Custom automation scripts"],
        },
        {
            "name":  "Jira / MS Project",
            "cat":   "PM Software",
            "col":   BLUE,
            "level": "PM Native",
            "uses":  ["Gantt charts & sprints", "Burndown / velocity", "Resource management", "Integration with BI tools"],
        },
        {
            "name":  "SQL / Databases",
            "cat":   "Data Storage",
            "col":   ORNG,
            "level": "Recommended",
            "uses":  ["Query project databases", "JOIN & filter data sets", "Aggregate KPI metrics", "Feed BI dashboards"],
        },
    ]

    positions = [(215,300),(640,300),(1065,300),(395,555),(885,555)]

    for i, (tool, (px, py)) in enumerate(zip(tools, positions)):
        ta = ease(max(0, (t - 0.10 - i*0.12)*3))
        if ta <= 0:
            continue
        col = tool["col"]
        cw, ch = 365, 205

        # Card
        rrect(d, px-cw//2, py-ch//2, px+cw//2, py+ch//2, 12,
              fill=blend(col, ta*0.09), outline=blend(col, ta*0.65))

        # Left accent strip
        for sy in range(py-ch//2+12, py+ch//2-12):
            d.line([(px-cw//2+4, sy), (px-cw//2+9, sy)], fill=blend(col, ta*0.8))

        # Category badge
        bx1 = px - cw//2 + 18
        bx_text = bx1 + 8
        bw2, bh2 = tsz(d, tool["cat"], FR[17])
        rrect(d, bx1, py-ch//2+10, bx1+bw2+16, py-ch//2+10+bh2+6, 4,
              fill=blend(col, ta*0.22))
        d.text((bx_text, py-ch//2+13), tool["cat"], font=FR[17], fill=blend(col, ta))

        # Level tag (right side)
        lw2, lh2 = tsz(d, tool["level"], FR[15])
        d.text((px+cw//2-lw2-14, py-ch//2+14), tool["level"], font=FR[15], fill=blend(col, ta*0.6))

        # Tool name
        nw, nh = tsz(d, tool["name"], FB[22])
        d.text((px-cw//2+20, py-38-nh//2), tool["name"], font=FB[22], fill=blend(WHITE, ta))

        # Uses list
        for j, use in enumerate(tool["uses"]):
            ua = ease(max(0, (t - 0.10 - i*0.12 - 0.08 - j*0.04)*5))
            if ua > 0:
                dx = px - cw//2 + 24
                dy = py - 2 + j * 28
                d.ellipse([dx-3, dy-3, dx+3, dy+3], fill=blend(col, ua*0.75))
                d.text((dx+12, dy-10), use, font=FR[18], fill=blend(LGRAY, ua*0.85))
    return img

# ── SCENE 7 · CLOSING  (frames 870-959) ───────────────────────────────────────
def s_close(f):
    t  = prog(f, 870, 959)
    img = new_frame(); d = ImageDraw.Draw(img)
    particles(d, f, 35, CYAN, 0.14)

    cx = W // 2
    pulse = math.sin(f * 0.08) * 0.5 + 0.5
    for r in [200, 165, 130]:
        d.ellipse([cx-r, H//2-r, cx+r, H//2+r],
                  outline=blend(CYAN, (0.05 + pulse*0.03) * ease(t)), width=1)

    # Title
    ta = ease(min(1, t*2.5))
    title = "Data-Driven Project Management"
    tw, th = tsz(d, title, FB[44])
    d.text((cx-tw//2, 195-th//2), title, font=FB[44], fill=blend(CYAN, ta))
    llen = int(tw * ta)
    d.line([(cx-llen//2, 225), (cx+llen//2, 225)], fill=blend(CYAN, ta*0.6), width=2)

    # Takeaways
    items = [
        ("Understand your data first",           CYAN),
        ("Choose the right tool for each task",  YEL),
        ("Apply analytics to drive decisions",   GRN),
        ("Communicate insights to stakeholders", ORNG),
    ]
    for i, (txt, col) in enumerate(items):
        ia = ease(max(0, (t - 0.20 - i*0.14)*4))
        if ia > 0:
            ty = 305 + i * 58
            d.text((cx-290, ty-14), ">>", font=FB[26], fill=blend(col, ia))
            d.text((cx-240, ty-14), txt, font=FR[26], fill=blend(WHITE, ia*0.9))

    # Bottom tagline
    ba = ease(max(0, (t-0.78)*5))
    tag = "Start with data.  Lead with insight."
    bw, bh = tsz(d, tag, FB[32])
    d.text((cx-bw//2, 575-bh//2), tag, font=FB[32], fill=blend(YEL, ba))

    # Bottom bar
    bar_w = int(W * ease(t))
    d.line([(cx-bar_w//2, H-30), (cx+bar_w//2, H-30)], fill=blend(CYAN, 0.45), width=2)
    return img

# ── SCENE TABLE ────────────────────────────────────────────────────────────────
SCENES = [
    (0,   89,  s_title),
    (90,  209, s_what),
    (210, 329, s_fields),
    (330, 509, s_pm),
    (510, 659, s_concepts),
    (660, 869, s_tools),
    (870, 959, s_close),
]
TOTAL = 960   # frames  →  32 seconds @ 30 fps

def apply_fade(img, f, margin=12):
    """Fade-in first <margin> frames and fade-out last <margin> frames of each scene."""
    for (start, end, _) in SCENES:
        if start <= f <= end:
            black = Image.new("RGB", (W, H), (0, 0, 0))
            fi = f - start
            fo = end - f
            if fi < margin:
                img = Image.blend(black, img, fi / margin)
            elif fo < margin:
                img = Image.blend(black, img, fo / margin)
            break
    return img

# ── MAIN ───────────────────────────────────────────────────────────────────────
def main():
    print("Data Science PM  —  Video Generator")
    print(f"Resolution: {W}x{H}  |  {FPS} fps  |  {TOTAL/FPS:.0f} s  |  {TOTAL} frames")
    print()

    if os.path.exists(FRAMES):
        shutil.rmtree(FRAMES)
    os.makedirs(FRAMES)

    for fi in range(TOTAL):
        img = None
        for (start, end, fn) in SCENES:
            if start <= fi <= end:
                img = fn(fi)
                break
        if img is None:
            img = new_frame()
        img = apply_fade(img, fi, margin=12)
        img.save(os.path.join(FRAMES, f"frame_{fi:05d}.png"))
        if fi % 60 == 0 or fi == TOTAL - 1:
            pct = 100 * fi // (TOTAL - 1)
            scene_name = next((f.__name__ for s, e, f in SCENES if s <= fi <= e), "?")
            print(f"  [{pct:3d}%] frame {fi:4d}  scene={scene_name}")

    print("\nRunning ffmpeg ...")
    cmd = [
        "ffmpeg", "-y",
        "-framerate", str(FPS),
        "-i", os.path.join(FRAMES, "frame_%05d.png"),
        "-c:v", "libx264",
        "-preset", "slow",
        "-crf", "18",
        "-pix_fmt", "yuv420p",
        OUTPUT
    ]
    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode != 0:
        print("ffmpeg error:\n", res.stderr[-2000:])
    else:
        size_mb = os.path.getsize(OUTPUT) / 1e6
        print(f"\nDone!  {OUTPUT}")
        print(f"Size:  {size_mb:.1f} MB  |  Duration: {TOTAL/FPS:.0f}s")

    shutil.rmtree(FRAMES)
    print("Temp frames removed.")

if __name__ == "__main__":
    main()
