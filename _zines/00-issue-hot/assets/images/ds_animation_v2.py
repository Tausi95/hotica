#!/usr/bin/env python3
"""
Data Science in Project Management — v2
Enhanced: voiceover + ambient music + glassmorphism + spring animations + slower pacing
"""

from PIL import Image, ImageDraw, ImageFont, ImageFilter
import numpy as np
import os, subprocess, math, shutil, wave, pyttsx3

# ─── CONFIG ──────────────────────────────────────────────────────────────────
W, H   = 1280, 720
FPS    = 30
OUTPUT = "/home/mage107/Documents/projects/hotica/ds_pm_v2.mp4"
FRAMES = "/tmp/dsv2_frames"
AUDIO  = "/tmp/dsv2_audio"

REG  = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"

# ─── SCENES  (frame ranges @ 30 fps) ─────────────────────────────────────────
# name          start   end   scene_fn
SCENE_MAP = [
    ("title",    0,     209),   # 7 s
    ("what",     210,   479),   # 9 s
    ("fields",   480,   719),   # 8 s
    ("pm",       720,   1079),  # 12 s
    ("concepts", 1080,  1439),  # 12 s
    ("tools",    1440,  1889),  # 15 s
    ("closing",  1890,  2069),  # 6 s
]
TOTAL = 2070   # 69 seconds

# ─── COLORS ──────────────────────────────────────────────────────────────────
BG    = (6,   6,  20);  BG2  = (14, 14, 44)
CYAN  = (0,  205, 255); RED  = (255, 65,  65)
YEL   = (255, 215, 45); GRN  = (65,  215, 100)
WHITE = (255, 255, 255); LGRAY= (160, 160, 196)
GRAY  = (90,  90, 130); PURP = (168, 80,  255)
ORNG  = (255, 145, 38); BLUE = (50,  128, 255)
TEAL  = (0,  175, 175); PINK = (255, 88,  172)

# ─── FONTS ───────────────────────────────────────────────────────────────────
_SIZES = [13,14,15,16,17,18,19,20,21,22,24,25,26,27,28,29,30,32,36,40,44,48,52,56,64,72,80,96]
FR = {s: ImageFont.truetype(REG,  s) for s in _SIZES}
FB = {s: ImageFont.truetype(BOLD, s) for s in _SIZES}

# ─── MATH / EASING ───────────────────────────────────────────────────────────
def clamp(v, lo=0.0, hi=1.0): return max(lo, min(hi, v))

def ease(t):
    t = clamp(t); return t*t*(3-2*t)

def ease_out(t):
    t = clamp(t); return 1-(1-t)**3

def bounce(t):
    """Slight overshoot then settle — pop-in feel."""
    t = clamp(t)
    if t < 0.75: return ease_out(t/0.75)
    x = (t-0.75)/0.25
    return 1.0 + 0.07*math.sin(x*math.pi)

def spring(t):
    t = clamp(t)
    return 1 - math.exp(-5.5*t)*math.cos(2*math.pi*t*0.9)

def prog(f, start, end):
    return clamp((f-start)/max(1, end-start))

# ─── COLOR HELPERS ────────────────────────────────────────────────────────────
def blend(col, a, bg=BG):
    return tuple(int(col[i]*a + bg[i]*(1-a)) for i in range(3))

def lerp_col(a, b, t):
    return tuple(int(a[i]+(b[i]-a[i])*t) for i in range(3))

# ─── DRAW PRIMITIVES ─────────────────────────────────────────────────────────
def tsz(draw, text, font):
    return draw.textsize(text, font=font)

def ct(draw, cx, cy, text, font, color):
    tw, th = tsz(draw, text, font)
    draw.text((cx-tw//2, cy-th//2), text, font=font, fill=color)

def lt(draw, x, cy, text, font, color):
    _, th = tsz(draw, text, font)
    draw.text((x, cy-th//2), text, font=font, fill=color)

def sct(draw, cx, cy, text, font, color, shadow=2):
    """Text with drop shadow."""
    sc = blend(color, 0.25, (0,0,0))
    ct(draw, cx+shadow, cy+shadow, text, font, sc)
    ct(draw, cx, cy, text, font, color)

def rrect(draw, x1, y1, x2, y2, r=12, fill=None, outline=None, lw=2):
    if x2<=x1 or y2<=y1: return
    r = min(r, (x2-x1)//2, (y2-y1)//2)
    if fill:
        draw.rectangle([x1+r,y1,x2-r,y2], fill=fill)
        draw.rectangle([x1,y1+r,x2,y2-r], fill=fill)
        for ex,ey in [(x1,y1),(x2-2*r,y1),(x1,y2-2*r),(x2-2*r,y2-2*r)]:
            draw.ellipse([ex,ey,ex+2*r,ey+2*r], fill=fill)
    if outline:
        draw.arc([x1,y1,x1+2*r,y1+2*r],180,270,fill=outline,width=lw)
        draw.arc([x2-2*r,y1,x2,y1+2*r],270,360,fill=outline,width=lw)
        draw.arc([x1,y2-2*r,x1+2*r,y2],90,180,fill=outline,width=lw)
        draw.arc([x2-2*r,y2-2*r,x2,y2],0,90,fill=outline,width=lw)
        draw.line([(x1+r,y1),(x2-r,y1)],fill=outline,width=lw)
        draw.line([(x1+r,y2),(x2-r,y2)],fill=outline,width=lw)
        draw.line([(x1,y1+r),(x1,y2-r)],fill=outline,width=lw)
        draw.line([(x2,y1+r),(x2,y2-r)],fill=outline,width=lw)

def glass_card(img, x1, y1, x2, y2, r=14, col=WHITE, fill_a=0.08, border_a=0.5, glow_layers=3):
    """RGBA-composited glassmorphism card with glow border."""
    r = min(r, max(1,(x2-x1)//2), max(1,(y2-y1)//2))
    ov = Image.new("RGBA", img.size, (0,0,0,0))
    od = ImageDraw.Draw(ov)
    fc = (*col, int(255*fill_a))
    od.rectangle([x1+r,y1,x2-r,y2], fill=fc)
    od.rectangle([x1,y1+r,x2,y2-r], fill=fc)
    for ex,ey in [(x1,y1),(x2-2*r,y1),(x1,y2-2*r),(x2-2*r,y2-2*r)]:
        od.ellipse([ex,ey,ex+2*r,ey+2*r], fill=fc)
    result = Image.alpha_composite(img.convert("RGBA"), ov).convert("RGB")
    d = ImageDraw.Draw(result)
    for i in range(glow_layers,0,-1):
        g = i*4
        rrect(d, x1-g,y1-g,x2+g,y2+g, r+g, outline=blend(col, border_a*0.15*(i/glow_layers)), lw=1)
    rrect(d, x1,y1,x2,y2, r, outline=blend(col, border_a), lw=2)
    return result

def gradient_bg(img):
    d = ImageDraw.Draw(img)
    for y in range(H):
        t = y/H
        r = int(BG[0]+(BG2[0]-BG[0])*t)
        g = int(BG[1]+(BG2[1]-BG[1])*t)
        b = int(BG[2]+(BG2[2]-BG[2])*t)
        d.line([(0,y),(W,y)], fill=(r,g,b))

def dot_grid(draw, frame, col=CYAN, a=0.045):
    sp = 65
    ox = (frame*0.35)%sp; oy = (frame*0.18)%sp
    for gx in range(int(-ox), W+sp, sp):
        for gy in range(int(-oy), H+sp, sp):
            pulse = math.sin(frame*0.04 + gx*0.008 + gy*0.008)*0.5+0.5
            c = blend(col, a*pulse)
            draw.ellipse([gx-1,gy-1,gx+2,gy+2], fill=c)

def particles(draw, frame, n=22, col=CYAN, a=0.10):
    import random; rng = random.Random(77)
    for _ in range(n):
        sx,sy = rng.randint(0,W), rng.randint(0,H)
        spd   = rng.uniform(0.2,0.8); sz = rng.uniform(0.5,2.8)
        x = (sx+frame*spd*0.5)%W; y = (sy-frame*spd*0.25)%H
        draw.ellipse([x-sz,y-sz,x+sz,y+sz], fill=blend(col, a*rng.uniform(0.3,1.0)))

def glow_dot(draw, cx, cy, r, col, a=0.35, layers=5):
    for i in range(layers,0,-1):
        gr = r+i*5; ga = a*(i/layers)*0.65
        draw.ellipse([cx-gr,cy-gr,cx+gr,cy+gr], outline=blend(col,ga), width=2)
    draw.ellipse([cx-r,cy-r,cx+r,cy+r], fill=blend(col,a*0.9))

def header(draw, title, sub=None, a=1.0):
    cx = W//2
    tw,th = tsz(draw, title, FB[52])
    draw.text((cx-tw//2+2, 52-th//2+2), title, font=FB[52], fill=blend(WHITE,a*0.2))
    draw.text((cx-tw//2, 52-th//2), title, font=FB[52], fill=blend(WHITE,a))
    llen = int(tw*a)
    draw.line([(cx-llen//2,86),(cx+llen//2,86)], fill=blend(CYAN,a*0.7), width=3)
    if sub:
        sw,_ = tsz(draw, sub, FR[22])
        draw.text((cx-sw//2,106), sub, font=FR[22], fill=blend(LGRAY,a*0.75))

def bar(draw, x, y, w, h, val, col, a=1.0):
    rrect(draw, x,y,x+w,y+h, 3, fill=blend(col,0.12))
    fw = max(6, int(w*val))
    rrect(draw, x,y,x+fw,y+h, 3, fill=blend(col,a*0.85))

def ring(draw, cx, cy, r, val, col, a=1.0, thick=7):
    draw.arc([cx-r,cy-r,cx+r,cy+r],0,360, fill=blend(col,0.12), width=thick)
    if val > 0:
        draw.arc([cx-r,cy-r,cx+r,cy+r],-90,-90+int(360*val), fill=blend(col,a), width=thick)

def new_frame():
    img = Image.new("RGB",(W,H),BG)
    gradient_bg(img)
    return img

# ─── SCENE 1 · TITLE  (0–209) ────────────────────────────────────────────────
def s_title(f):
    t = prog(f,0,209)
    img = new_frame(); d = ImageDraw.Draw(img)
    dot_grid(d, f, CYAN, 0.035)
    particles(d, f, 28, CYAN, 0.11)

    cx,cy = W//2, H//2
    pulse = math.sin(f*0.08)*0.5+0.5
    for r in [240,200,162]:
        d.ellipse([cx-r,cy-r+15,cx+r,cy+r+15], outline=blend(CYAN,0.03+pulse*0.025), width=1)

    # DATA SCIENCE title — bounces in
    ta = bounce(clamp(t*3.5))
    y_off = int((1-ta)*60)
    tw,th = tsz(d,"DATA SCIENCE",FB[80])
    d.text((cx-tw//2+2,cy-102-th//2+2+y_off),"DATA SCIENCE",font=FB[80],fill=blend(CYAN,ta*0.18))
    d.text((cx-tw//2,cy-102-th//2+y_off),"DATA SCIENCE",font=FB[80],fill=blend(CYAN,ta))
    llen = int(tw*ta)
    d.line([(cx-llen//2,cy-102+th//2+8),(cx+llen//2,cy-102+th//2+8)],fill=blend(CYAN,ta*0.75),width=3)

    # Subtitle slides from left
    sa = ease_out(clamp((t-0.18)*3))
    sx_off = int((1-sa)*200)
    sub = "FOR PROJECT MANAGEMENT PROFESSIONALS"
    sw,sh = tsz(d,sub,FR[29])
    d.text((cx-sw//2-sx_off,cy-5-sh//2),sub,font=FR[29],fill=blend(WHITE,sa*0.88))

    # Tagline slides from right
    ga = ease_out(clamp((t-0.32)*3))
    gx_off = int((1-ga)*200)
    tag = "Tools  ·  Concepts  ·  Analytics"
    gw,gh = tsz(d,tag,FB[30])
    d.text((cx-gw//2+gx_off,cy+58-gh//2),tag,font=FB[30],fill=blend(YEL,ga))

    # Bottom sweep
    bw = int(W*ease(t))
    d.line([(cx-bw//2,H-32),(cx+bw//2,H-32)],fill=blend(CYAN,0.5),width=2)

    # Corner data symbols
    syms = ["01","10","11","00","01"]
    for i,s2 in enumerate(syms):
        sa2 = ease(clamp((t-0.5)*3))
        x_s = 40+i*60; y_s = 40
        d.text((x_s,y_s),s2,font=FR[14],fill=blend(CYAN,sa2*0.2))
        d.text((x_s,H-55),s2,font=FR[14],fill=blend(CYAN,sa2*0.2))
    return img

# ─── SCENE 2 · WHAT IS DATA SCIENCE  (210–479) ───────────────────────────────
def s_what(f):
    t = prog(f,210,479)
    img = new_frame(); d = ImageDraw.Draw(img)
    dot_grid(d, f, BLUE, 0.03)
    particles(d, f, 16, BLUE, 0.08)

    ha = ease(clamp(t*3)); header(d,"What is Data Science?",a=ha)
    d.line([(80,128),(W-80,128)],fill=blend(CYAN,ha*0.2),width=1)

    # Definition box slides up
    da = ease_out(clamp((t-0.15)*3))
    dy = int((1-da)*40)
    img = glass_card(img,85,142+dy,W-85,240+dy,r=12,col=CYAN,fill_a=0.06,border_a=0.35,glow_layers=2)
    if da > 0.1:
        d2 = ImageDraw.Draw(img)
        lines = [
            ("An interdisciplinary field combining statistics, programming & domain knowledge",FR[25],WHITE,182+dy),
            ("to extract insights from data and drive smarter, data-driven decisions.",FR[25],LGRAY,212+dy),
        ]
        for txt,fnt,col,y in lines:
            tw,th = tsz(d2,txt,fnt); d2.text((W//2-tw//2,y-th//2),txt,font=fnt,fill=blend(col,da))

    # Three pillars pop in with bounce
    pillars = [
        (200,  "Statistics &\nMathematics", CYAN,  "Probability · Regression\nHypothesis Testing"),
        (W//2, "Programming\n& Tools",      PURP,  "Python · R · SQL\nVisualization Libs"),
        (W-200,"Domain\nKnowledge",         GRN,   "Industry context\nBusiness understanding"),
    ]
    for i,(px,name,col,desc) in enumerate(pillars):
        delay = 0.28+i*0.14
        sc = bounce(clamp((t-delay)*3.5))
        a  = ease(clamp((t-delay)*3))
        if sc <= 0: continue
        py = 455
        cw,ch = int(240*sc), int(195*sc)
        img = glass_card(img,px-cw//2,py-ch//2,px+cw//2,py+ch//2,r=int(14*sc),col=col,fill_a=0.09,border_a=0.6,glow_layers=2)
        d2 = ImageDraw.Draw(img)
        # Icon circle
        ir = int(27*sc)
        if ir>3:
            d2.ellipse([px-ir,py-int(80*sc)-ir,px+ir,py-int(80*sc)+ir],fill=blend(col,a*0.85))
        # Name
        if sc > 0.45:
            for j,ln in enumerate(name.split('\n')):
                tw,th = tsz(d2,ln,FB[24]); d2.text((px-tw//2,py-30+j*29-th//2),ln,font=FB[24],fill=blend(col,a))
        # Desc
        if sc > 0.65:
            for j,ln in enumerate(desc.split('\n')):
                tw,th = tsz(d2,ln,FR[18]); d2.text((px-tw//2,py+38+j*23-th//2),ln,font=FR[18],fill=blend(LGRAY,a*0.8))
    return img

# ─── SCENE 3 · FIELDS  (480–719) ─────────────────────────────────────────────
def s_fields(f):
    t = prog(f,480,719)
    img = new_frame(); d = ImageDraw.Draw(img)
    dot_grid(d, f, PURP, 0.03)
    particles(d, f, 16, PURP, 0.07)

    ha = ease(clamp(t*3)); header(d,"Data Science Across Industries",a=ha)
    d.line([(80,128),(W-80,128)],fill=blend(CYAN,ha*0.2),width=1)

    fields = [
        (160,   "Healthcare",   RED,  "Diagnosis\nOutcomes\nDrug Discovery"),
        (376,   "Finance",      YEL,  "Risk Modeling\nFraud Detection\nTrading"),
        (W//2,  "Marketing",    ORNG, "Segmentation\nCampaign Analytics\nCLV"),
        (W-376, "Manufacturing",BLUE, "Quality Control\nPred. Maintenance\nIoT"),
        (W-160, "Project Mgmt", GRN,  "Risk & Resources\nSchedule & Budget\nKPIs"),
    ]
    py_center = 400

    for i,(px,name,col,desc) in enumerate(fields):
        delay = 0.10+i*0.11
        sc = bounce(clamp((t-delay)*3.5))
        a  = ease(clamp((t-delay)*3))
        if sc<=0: continue

        is_pm = (i==4)
        r = int((80 if is_pm else 64)*sc)

        # Connection line to previous node
        if i>0 and t>delay+0.2:
            prev_px = fields[i-1][0]
            la = ease(clamp((t-delay-0.1)*4))
            lx1 = prev_px + (64 if i-1<4 else 80)
            lx2 = px - r
            d.line([(lx1,py_center),(lx2,py_center)],fill=blend(col,la*0.3),width=1)

        # Glow for PM
        if is_pm:
            glow_dot(d,px,py_center,r+15,col,a=a*0.15,layers=4)

        # Main circle
        d.ellipse([px-r,py_center-r,px+r,py_center+r],
                  fill=blend(col,a*(0.22 if is_pm else 0.13)),
                  outline=blend(col,a*(1.0 if is_pm else 0.7)),
                  width=(3 if is_pm else 2))

        if is_pm and a>0.5:
            fw2,fh2 = tsz(d,"FOCUS",FB[17])
            d.text((px-fw2//2,py_center-r-26-fh2//2),"FOCUS",font=FB[17],fill=blend(YEL,a))

        fnt = FB[25 if is_pm else 21]
        tw,th = tsz(d,name,fnt)
        sct(d,px,py_center,name,fnt,blend(col,a))

        # Desc below
        if sc>0.5:
            dy2 = py_center+r+20
            for j,ln in enumerate(desc.split('\n')):
                tw,th = tsz(d,ln,FR[16])
                d.text((px-tw//2,dy2+j*20-th//2),ln,font=FR[16],fill=blend(LGRAY,a*0.75))

    # Footer
    na = ease(clamp((t-0.85)*5))
    if na>0:
        note="Our focus today:  Project Management"
        nw,nh = tsz(d,note,FB[26]); d.text((W//2-nw//2,H-50-nh//2),note,font=FB[26],fill=blend(GRN,na))
    return img

# ─── SCENE 4 · PM FOCUS  (720–1079) ──────────────────────────────────────────
def s_pm(f):
    t = prog(f,720,1079)
    img = new_frame(); d = ImageDraw.Draw(img)
    dot_grid(d, f, GRN, 0.03)
    particles(d, f, 16, GRN, 0.07)

    ha = ease(clamp(t*3)); header(d,"Data Science in Project Management",a=ha)
    d.line([(80,128),(W-80,128)],fill=blend(CYAN,ha*0.2),width=1)

    cases = [
        ("RISK\nASSESSMENT",       RED,  "Identify & quantify risks\nbefore they occur",            "◆", 0.90),
        ("RESOURCE\nPLANNING",     BLUE, "Optimize team allocation\n& capacity forecasting",        "■", 0.78),
        ("SCHEDULE\nOPTIMIZATION", CYAN, "Critical path analysis\n& delay prediction",              "▲", 0.85),
        ("BUDGET\nFORECASTING",    YEL,  "Predict cost overruns\n& control spend",                  "$", 0.80),
        ("KPI\nTRACKING",          GRN,  "Monitor project health\n& performance metrics",           "●", 0.95),
    ]
    positions = [(185,340),(505,340),(825,340),(335,570),(695,570)]

    for i,((name,col,desc,icon,impact),(px,py)) in enumerate(zip(cases,positions)):
        delay = 0.12+i*0.11
        sc = bounce(clamp((t-delay)*3.5)); a = ease(clamp((t-delay)*3))
        if sc<=0: continue
        cw,ch = int(255*sc), int(170*sc)

        img = glass_card(img,px-cw//2,py-ch//2,px+cw//2,py+ch//2,r=int(13*sc),
                         col=col,fill_a=0.09,border_a=0.65,glow_layers=2)
        d2 = ImageDraw.Draw(img)

        if sc>0.3:
            iw,ih = tsz(d2,icon,FB[28]); d2.text((px-iw//2,py-int(60*sc)-ih//2),icon,font=FB[28],fill=blend(col,a))

        if sc>0.5:
            for j,ln in enumerate(name.split('\n')):
                tw,th = tsz(d2,ln,FB[21]); d2.text((px-tw//2,py-8+j*25-th//2),ln,font=FB[21],fill=blend(col,a))

        if sc>0.65:
            for j,ln in enumerate(desc.split('\n')):
                tw,th = tsz(d2,ln,FR[17]); d2.text((px-tw//2,py+48+j*21-th//2),ln,font=FR[17],fill=blend(LGRAY,a*0.85))

        # Impact bar
        if sc>0.7:
            bar_a = ease(clamp((t-delay-0.18)*3))
            bx,by,bw2,bh2 = px-int(90*sc), py+int(80*sc), int(180*sc), int(8*sc)
            bh2 = max(bh2,4)
            bar(d2,bx,by,bw2,bh2, impact*bar_a, col, a)
    return img

# ─── SCENE 5 · CONCEPTS  (1080–1439) ─────────────────────────────────────────
def s_concepts(f):
    t = prog(f,1080,1439)
    img = new_frame(); d = ImageDraw.Draw(img)
    dot_grid(d, f, YEL, 0.025)
    particles(d, f, 16, YEL, 0.07)

    ha = ease(clamp(t*3)); header(d,"4 Types of Data Analytics",a=ha)
    d.line([(80,128),(W-80,128)],fill=blend(CYAN,ha*0.2),width=1)

    items = [
        ("Descriptive",  CYAN, "What\nhappened?",    "Dashboards · Reports\nHistorical summaries", 0.25, "Past performance\nbudget summaries"),
        ("Diagnostic",   ORNG, "Why did it\nhappen?","Root Cause Analysis\nCorrelation Studies",   0.50, "Delay root-\ncause analysis"),
        ("Predictive",   PURP, "What will\nhappen?", "ML Forecasting\nRisk Scoring",               0.75, "Schedule &\nrisk prediction"),
        ("Prescriptive", GRN,  "What should\nwe do?","Optimization\nDecision Support",             1.00, "Resource &\ncost optimization"),
    ]
    sp = (W-140)//4; x0 = 70+sp//2

    for i,(atype,col,question,examples,ring_val,pm_ctx) in enumerate(items):
        px = x0+i*sp
        delay = 0.10+i*0.13
        sc = bounce(clamp((t-delay)*3.5)); a = ease(clamp((t-delay)*3))
        if sc<=0: continue

        by,bh2,bw = 150, int(430*sc), sp-30

        # Card
        img = glass_card(img,px-bw//2,by,px+bw//2,by+bh2,r=int(13*sc),
                         col=col,fill_a=0.10,border_a=0.60,glow_layers=2)
        d2 = ImageDraw.Draw(img)

        # Number badge
        d2.ellipse([px-22,by-22,px+22,by+22],fill=blend(col,a*0.9))
        nw,nh = tsz(d2,str(i+1),FB[22])
        d2.text((px-nw//2,by-nh//2),str(i+1),font=FB[22],fill=BG)

        if sc>0.4:
            # Progress ring
            ring_prog = ease(clamp((t-delay-0.12)*3))*ring_val
            ring(d2,px,by+int(80*sc),int(30*sc),ring_prog,col,a,thick=max(4,int(7*sc)))

        if sc>0.5:
            aw,ah = tsz(d2,atype,FB[22])
            d2.text((px-aw//2,by+int(125*sc)-ah//2),atype,font=FB[22],fill=blend(col,a))
            for j,ln in enumerate(question.split('\n')):
                tw,th = tsz(d2,ln,FR[19]); d2.text((px-tw//2,by+int(168*sc)+j*23-th//2),ln,font=FR[19],fill=blend(WHITE,a*0.9))

        if sc>0.7:
            da2 = ease(clamp((t-delay-0.18)*3))
            dlen = int((bw-30)*da2)
            d2.line([(px-dlen//2,by+int(228*sc)),(px+dlen//2,by+int(228*sc))],fill=blend(col,a*0.3),width=1)
            for j,ln in enumerate(examples.split('\n')):
                tw,th = tsz(d2,ln,FR[17]); d2.text((px-tw//2,by+int(250*sc)+j*21-th//2),ln,font=FR[17],fill=blend(LGRAY,a*0.8))

        if sc>0.85:
            pa2 = ease(clamp((t-delay-0.28)*4))
            pw,ph = tsz(d2,"PM:",FB[15])
            d2.text((px-bw//2+12,by+int(330*sc)),"PM:",font=FB[15],fill=blend(col,pa2*0.7))
            for j,ln in enumerate(pm_ctx.split('\n')):
                tw,th = tsz(d2,ln,FR[16]); d2.text((px-tw//2,by+int(355*sc)+j*20-th//2),ln,font=FR[16],fill=blend(col,pa2*0.6))

        # Arrow to next
        if i<3:
            arr_a = ease(clamp((t-delay-0.15)*4))
            if arr_a>0:
                ax = px+sp//2; ay = by+bh2//2
                ac = blend(GRAY,arr_a*0.55)
                d2.line([(ax-18,ay),(ax+12,ay)],fill=ac,width=2)
                d2.polygon([(ax+12,ay-6),(ax+12,ay+6),(ax+25,ay)],fill=ac)
    return img

# ─── SCENE 6 · TOOLS  (1440–1889) ────────────────────────────────────────────
def s_tools(f):
    t = prog(f,1440,1889)
    img = new_frame(); d = ImageDraw.Draw(img)
    dot_grid(d, f, ORNG, 0.028)
    particles(d, f, 16, ORNG, 0.07)

    ha = ease(clamp(t*3)); header(d,"Essential Tools for PM Data Science",a=ha)
    d.line([(80,128),(W-80,128)],fill=blend(CYAN,ha*0.2),width=1)

    tools = [
        {"name":"Excel / Google Sheets","cat":"Spreadsheets","col":GRN, "lvl":"Beginner",
         "uses":["Data entry & cleaning","Pivot tables & formulas","Charts & VLOOKUP","Basic dashboards"],
         "skill":0.65, "slide":-1},
        {"name":"Power BI / Tableau",   "cat":"Visualization","col":YEL, "lvl":"Intermediate",
         "uses":["Interactive dashboards","Real-time reporting","Drill-down analysis","Share & publish"],
         "skill":0.78, "slide":1},
        {"name":"Python / R",           "cat":"Programming",  "col":CYAN,"lvl":"Advanced",
         "uses":["pandas, numpy, sklearn","Statistical modeling","Machine learning","Automation scripts"],
         "skill":0.85, "slide":-1},
        {"name":"Jira / MS Project",    "cat":"PM Software",  "col":BLUE,"lvl":"PM Native",
         "uses":["Gantt & sprints","Burndown charts","Resource mgmt","BI integration"],
         "skill":0.72, "slide":1},
        {"name":"SQL / Databases",      "cat":"Data Storage", "col":ORNG,"lvl":"Recommended",
         "uses":["Query project data","JOIN & filter sets","Aggregate KPIs","Feed dashboards"],
         "skill":0.70, "slide":-1},
    ]
    positions = [(215,305),(640,305),(1065,305),(400,565),(880,565)]

    for i,(tool,(px,py)) in enumerate(zip(tools,positions)):
        delay = 0.10+i*0.11
        a = ease(clamp((t-delay)*3))
        # Slide in from alternating sides
        slide_a = ease_out(clamp((t-delay)*2.8))
        x_off = int((1-slide_a)*220*tool["slide"])
        if a<=0: continue
        col = tool["col"]; cw,ch = 365,215

        img = glass_card(img,px-cw//2+x_off,py-ch//2,px+cw//2+x_off,py+ch//2,
                         r=13,col=col,fill_a=0.09,border_a=0.60,glow_layers=2)
        d2 = ImageDraw.Draw(img)
        xo = x_off  # shorthand

        # Left accent strip
        for sy in range(py-ch//2+12, py+ch//2-12):
            d2.line([(px-cw//2+xo+4,sy),(px-cw//2+xo+9,sy)],fill=blend(col,a*0.85))

        # Category badge
        bx = px-cw//2+xo+18
        bw2,bh2 = tsz(d2,tool["cat"],FR[16])
        rrect(d2,bx,py-ch//2+10,bx+bw2+16,py-ch//2+10+bh2+6,4,fill=blend(col,a*0.22))
        d2.text((bx+8,py-ch//2+13),tool["cat"],font=FR[16],fill=blend(col,a))

        # Level tag
        lw2,_ = tsz(d2,tool["lvl"],FR[14])
        d2.text((px+cw//2+xo-lw2-14,py-ch//2+14),tool["lvl"],font=FR[14],fill=blend(col,a*0.6))

        # Tool name
        nw,nh = tsz(d2,tool["name"],FB[22])
        d2.text((px-cw//2+xo+20,py-42-nh//2),tool["name"],font=FB[22],fill=blend(WHITE,a))

        # Skill bar
        skill_a = ease(clamp((t-delay-0.12)*3))
        bar(d2,px-cw//2+xo+20,py-12,160,8, tool["skill"]*skill_a, col, a)
        sw2,sh2 = tsz(d2,"Proficiency",FR[13])
        d2.text((px-cw//2+xo+186,py-14),f"{int(tool['skill']*100)}%",font=FR[14],fill=blend(col,a*0.7))

        # Uses list
        for j,use in enumerate(tool["uses"]):
            ua = ease(clamp((t-delay-0.10-j*0.04)*5))
            if ua>0:
                dx = px-cw//2+xo+22; dy = py+15+j*30
                d2.ellipse([dx-3,dy-3,dx+3,dy+3],fill=blend(col,ua*0.8))
                d2.text((dx+12,dy-10),use,font=FR[17],fill=blend(LGRAY,ua*0.88))
    return img

# ─── SCENE 7 · CLOSING  (1890–2069) ──────────────────────────────────────────
def s_close(f):
    t = prog(f,1890,2069)
    img = new_frame(); d = ImageDraw.Draw(img)
    dot_grid(d, f, CYAN, 0.04)
    particles(d, f, 32, CYAN, 0.13)

    cx = W//2
    pulse = math.sin(f*0.07)*0.5+0.5
    for r in [215,175,135]:
        d.ellipse([cx-r,H//2-r,cx+r,H//2+r],outline=blend(CYAN,(0.04+pulse*0.03)*ease(t)),width=1)

    ta = ease(clamp(t*2.5))
    title = "Data-Driven Project Management"
    tw,th = tsz(d,title,FB[44])
    d.text((cx-tw//2+2,192-th//2+2),title,font=FB[44],fill=blend(CYAN,ta*0.18))
    d.text((cx-tw//2,192-th//2),title,font=FB[44],fill=blend(CYAN,ta))
    llen = int(tw*ta)
    d.line([(cx-llen//2,223),(cx+llen//2,223)],fill=blend(CYAN,ta*0.6),width=2)

    takeaways = [
        ("Understand your data",                CYAN),
        ("Choose the right tool for each task", YEL),
        ("Apply analytics to drive decisions",  GRN),
        ("Communicate insights to stakeholders",ORNG),
    ]
    for i,(txt,col) in enumerate(takeaways):
        ia = ease(clamp((t-0.18-i*0.13)*4))
        if ia>0:
            ty = 295+i*62
            sc = bounce(clamp((t-0.18-i*0.13)*4))
            # Bullet pop
            bsz = int(18*sc); bx = cx-290
            if bsz>2: d.ellipse([bx-bsz//2,ty-bsz//2,bx+bsz//2,ty+bsz//2],fill=blend(col,ia))
            d.text((cx-262,ty-14),txt,font=FR[27],fill=blend(WHITE,ia*0.92))

    ba = ease(clamp((t-0.75)*5))
    tag = "Start with data.  Lead with insight."
    bw,bh = tsz(d,tag,FB[32])
    d.text((cx-bw//2,582-bh//2),tag,font=FB[32],fill=blend(YEL,ba))

    bw2 = int(W*ease(t))
    d.line([(cx-bw2//2,H-28),(cx+bw2//2,H-28)],fill=blend(CYAN,0.45),width=2)
    return img

# ─── SCENE DISPATCH ──────────────────────────────────────────────────────────
_SCENE_FNS = [s_title, s_what, s_fields, s_pm, s_concepts, s_tools, s_close]

def render_frame(fi):
    for idx,(name,start,end) in enumerate(SCENE_MAP):
        if start <= fi <= end:
            return _SCENE_FNS[idx](fi)
    return new_frame()

def apply_fade(img, fi, margin=15):
    black = Image.new("RGB",(W,H),(0,0,0))
    for name,start,end in SCENE_MAP:
        if start <= fi <= end:
            fo = end - fi; fi2 = fi - start
            if fi2 < margin:
                img = Image.blend(black, img, fi2/margin)
            elif fo < margin:
                img = Image.blend(black, img, fo/margin)
            break
    return img

# ─── AUDIO GENERATION ────────────────────────────────────────────────────────
VOICEOVER_LINES = [
    (0.5,  "Welcome. Data Science for Project Management Professionals."),
    (4.0,  "Exploring the tools, concepts, and applications that transform project delivery."),
    (8.0,  "Data science combines statistics and mathematics, programming and tools, and domain knowledge."),
    (14.0, "Together, these disciplines extract insights and power smarter decisions."),
    (17.5, "Data science is transforming industries worldwide."),
    (20.5, "From healthcare and finance to manufacturing — and now project management."),
    (24.5, "For project managers, data science enables five critical capabilities."),
    (28.5, "Risk assessment, resource planning, schedule optimization, budget forecasting, and real-time KPI tracking."),
    (37.0, "Four types of analytics drive every decision: descriptive, diagnostic, predictive, and prescriptive."),
    (43.5, "Descriptive tells what happened. Diagnostic explains why. Predictive forecasts the future. And prescriptive recommends the best action."),
    (51.5, "The modern project manager uses five essential tools."),
    (54.5, "Excel and Sheets for analysis. Power BI and Tableau for dashboards."),
    (59.0, "Python and R for advanced modeling. Jira and MS Project for tracking. SQL for database queries."),
    (65.0, "The future of project management is data-driven."),
    (68.0, "Start with data, apply the right analytics, and always lead your team with clear insight."),
]

def gen_voiceover(audio_dir, total_s, sr=44100):
    print("  Generating voiceover clips ...")
    os.makedirs(audio_dir, exist_ok=True)
    engine = pyttsx3.init()
    for v in engine.getProperty('voices'):
        if 'Great Britain' in v.name:
            engine.setProperty('voice', v.id); break
    engine.setProperty('rate', 150)
    engine.setProperty('volume', 0.95)

    total_n = int(total_s * sr)
    vo = np.zeros(total_n, dtype=np.float32)

    for idx,(start_s,text) in enumerate(VOICEOVER_LINES):
        clip = os.path.join(audio_dir, f"vo_{idx:03d}.wav")
        engine.save_to_file(text, clip)
        engine.runAndWait()
        if not os.path.exists(clip): continue
        try:
            with wave.open(clip,'r') as wf:
                clip_sr = wf.getframerate(); clip_ch = wf.getnchannels()
                raw = wf.readframes(wf.getnframes())
                samples = np.frombuffer(raw, dtype=np.int16).astype(np.float32)/32768.0
                if clip_ch==2: samples = samples.reshape(-1,2).mean(axis=1)
                if clip_sr != sr:
                    new_n = int(len(samples)*sr/clip_sr)
                    samples = np.interp(np.linspace(0,len(samples)-1,new_n),np.arange(len(samples)),samples)
            s0 = int(start_s*sr); s1 = min(s0+len(samples), total_n)
            vo[s0:s1] += samples[:s1-s0]
        except Exception as e:
            print(f"    VO clip {idx} error: {e}")

    peak = np.max(np.abs(vo))
    if peak>0.01: vo = vo/peak*0.90
    out = os.path.join(audio_dir,"vo_full.wav")
    with wave.open(out,'w') as wf:
        wf.setnchannels(1); wf.setsampwidth(2); wf.setframerate(sr)
        wf.writeframes((vo*32767).astype(np.int16).tobytes())
    print(f"  Voiceover: {out}")
    return out

def gen_music(total_s, audio_dir, sr=44100):
    print("  Generating ambient music ...")
    n = int(total_s*sr)
    t = np.linspace(0, total_s, n, False)

    # Ambient pad — C major pentatonic
    freqs_pad = [130.81,164.81,196.00,261.63,329.63]
    pad = np.zeros(n)
    chord_dur = 8.0
    for ci,freq in enumerate(freqs_pad):
        phase = ci*0.7
        wave_ = (0.5*np.sin(2*np.pi*freq*t+phase) +
                 0.18*np.sin(2*np.pi*freq*2*t) +
                 0.06*np.sin(2*np.pi*freq*3*t))
        mod = 0.85 + 0.15*np.sin(2*np.pi*0.04*t + ci)
        pad += wave_*mod*0.055

    # Sub bass pulse
    bass_f = 65.41
    beat = sr*60/68  # 68 BPM
    bass = np.zeros(n)
    for bi in range(int(n/beat)+1):
        bs = int(bi*beat); be = min(bs+int(beat*0.45),n)
        if bs>=n: break
        seg_t = np.arange(be-bs)/sr
        env = np.exp(-5*seg_t/max(be-bs,1)*sr*(beat/sr))
        bass[bs:be] += np.sin(2*np.pi*bass_f*seg_t)*env*0.12

    # High shimmer arp
    arp = [523.25,659.25,783.99,1046.5]
    arp_beat = sr*60/68/2
    shimmer = np.zeros(n)
    for ai in range(int(n/arp_beat)+1):
        note = arp[ai%len(arp)]
        bs = int(ai*arp_beat); be = min(bs+int(arp_beat*0.55),n)
        if bs>=n: break
        seg_t = np.arange(be-bs)/sr
        env = np.exp(-9*seg_t/max(be-bs,1)*sr*(arp_beat/sr))
        shimmer[bs:be] += np.sin(2*np.pi*note*seg_t)*env*0.025

    music = pad+bass+shimmer
    peak = np.max(np.abs(music))
    if peak>0: music = music/peak*0.35
    fade = min(int(2.5*sr),n//4)
    music[:fade]  *= np.linspace(0,1,fade)
    music[-fade:] *= np.linspace(1,0,fade)

    out = os.path.join(audio_dir,"bgm.wav")
    with wave.open(out,'w') as wf:
        wf.setnchannels(1); wf.setsampwidth(2); wf.setframerate(sr)
        wf.writeframes((music*32767).astype(np.int16).tobytes())
    print(f"  Music: {out}")
    return out

# ─── MAIN ────────────────────────────────────────────────────────────────────
def main():
    total_s = TOTAL/FPS
    print(f"\nData Science PM v2  |  {W}x{H}  |  {FPS}fps  |  {TOTAL} frames  |  {total_s:.0f}s\n")

    # Prep dirs
    for d in [FRAMES, AUDIO]:
        if os.path.exists(d): shutil.rmtree(d)
        os.makedirs(d)

    # ── Audio phase ──────────────────────────────────────────────────────────
    vo_path  = gen_voiceover(AUDIO, total_s)
    bgm_path = gen_music(total_s, AUDIO)

    # ── Frame render phase ───────────────────────────────────────────────────
    print(f"\nRendering {TOTAL} frames ...")
    for fi in range(TOTAL):
        img = render_frame(fi)
        img = apply_fade(img, fi)
        img.save(os.path.join(FRAMES, f"f_{fi:05d}.png"))
        if fi%90==0 or fi==TOTAL-1:
            scene = next((n for n,s,e in SCENE_MAP if s<=fi<=e),"?")
            print(f"  [{100*fi//(TOTAL-1):3d}%] {fi:4d}/{TOTAL}  scene={scene}")

    # ── ffmpeg: video only ───────────────────────────────────────────────────
    vid_only = OUTPUT.replace(".mp4","_noaudio.mp4")
    print("\nCompiling video ...")
    subprocess.run([
        "ffmpeg","-y","-framerate",str(FPS),
        "-i",os.path.join(FRAMES,"f_%05d.png"),
        "-c:v","libx264","-preset","slow","-crf","18","-pix_fmt","yuv420p",
        vid_only
    ], check=True, capture_output=True)

    # ── ffmpeg: mix audio ────────────────────────────────────────────────────
    print("Mixing audio ...")
    subprocess.run([
        "ffmpeg","-y",
        "-i", vid_only,
        "-i", bgm_path,
        "-i", vo_path,
        "-filter_complex",
        "[1:a]volume=0.28[music];[2:a]volume=1.0[vo];[music][vo]amix=inputs=2:duration=first[aout]",
        "-map","0:v","-map","[aout]",
        "-c:v","copy","-c:a","aac","-b:a","192k",
        OUTPUT
    ], check=True, capture_output=True)

    os.remove(vid_only)
    size_mb = os.path.getsize(OUTPUT)/1e6
    print(f"\nDone!  {OUTPUT}")
    print(f"       {size_mb:.1f} MB  |  {total_s:.0f}s  |  {W}x{H}  |  {FPS}fps")

    # Cleanup
    shutil.rmtree(FRAMES); shutil.rmtree(AUDIO)
    print("Temp files cleaned up.")

if __name__=="__main__":
    main()
