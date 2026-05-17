import os
import smtplib
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

SMTP_SERVER = "smtp.office365.com"
SMTP_PORT = 587
SENDER_EMAIL = "effortbuildingcontractors@woodlaine.com"
SENDER_PASSWORD = os.environ.get("HOTICA_EMAIL_PASSWORD", "")

# Active + Inactive models with no studio — skip suspicious/male accounts
RECIPIENTS = [
    # --- Active models ---
    ("Vayanakiss",          "yvanesku@gmail.com"),
    ("Sexysuzzy1",          "stipme4@gmail.com"),
    ("AnnRose",             "naledirose375@gmail.com"),
    ("JumboBrain",          "warwaraw7@gmail.com"),
    ("SweetNicole",         "moonmagicgame1@gmail.com"),
    ("LissaRoss",           "sakuranakayama2020@gmail.com"),
    ("Sweetib",             "babrakabachwa@gmail.com"),
    ("Brunetthot",          "istelarodriguessilva@gmail.com"),
    ("NikkiHolland",        "nikkihollandcam@gmail.com"),
    ("HeavenQueen",         "tyfelici@yahoo.com"),
    ("nastycurious",        "jamiecardenasricardo@gmail.com"),
    ("stesh",               "stazham427@gmail.com"),
    ("Cherrylnisha",        "cherrylnisha207@gmail.com"),
    # --- Inactive / dormant models ---
    ("Swtviv",              "makenaritah24@gmail.com"),
    ("NanaTheLover",        "nanasakura2023@gmail.com"),
    ("sassy_electra",       "muyakerz@gmail.com"),
    ("oliviagates",         "orangefanta654@gmail.com"),
    ("Feniixjp",            "carolinaapereira97@gmail.com"),
    ("Lizzielulu",          "daniellemealey@icloud.com"),
    ("Pantera_doce",        "panterahot773@gmail.com"),
    ("Lisagirl",            "mo0985149708@gmail.com"),
    ("girlfromtheinternet", "vmairew98@gmail.com"),
    ("MisssPePsi",          "auda7799@gmail.com"),
    ("burmilla",            "manuellaelisafranke@gmail.com"),
    ("Pamela",              "rosmiloca34@gmail.com"),
    ("hotbomb",             "probookg5+3@yahoo.com"),
    ("sexymiss24",          "modaswenke@gmail.com"),
    ("Khalessi69",          "serinamcfadden@gmail.com"),
    ("EvieWolf",            "kspthings1@gmail.com"),
]


def build_email(username: str):
    subject = "Your Personal Hotica Landing Page — We Need Your Photos"
    body = f"""\
Hi {username},

We have exciting news — we are building you a personal landing page on Hotica!

This page will be your own dedicated space where fans can find you, learn about you, and connect with you directly. It will be live under your own link and designed to help you grow your audience.

To get your page ready, we need the following from you:

  Photos (5–6 total):
  • A clear profile photo (face visible, good lighting)
  • 3–4 promotional photos that best represent you and your style
  • A cover/banner photo (wide/landscape format preferred)

  Videos (2–3 total):
  • Short clips showcasing your personality or content style
  • Any teaser or highlight videos you would like featured on your page

Please send your photos to:
  effortbuildingcontractors@woodlaine.com

The sooner we receive your photos, the sooner your page goes live.

If you have any questions or need guidance on what to send, just reply to this email — we are happy to help.

Best regards,
The Hotica Team\
"""
    return subject, body


def send_emails(dry_run: bool = True) -> None:
    if not SENDER_PASSWORD and not dry_run:
        print("ERROR: HOTICA_EMAIL_PASSWORD environment variable is not set.")
        return

    print(f"{'[DRY RUN] ' if dry_run else ''}Preparing to send to {len(RECIPIENTS)} recipients.\n")

    server = None
    if not dry_run:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.ehlo()
        server.starttls()
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        print("Connected to smtp.office365.com\n")

    sent = 0
    failed = 0
    for username, to_email in RECIPIENTS:
        subject, body = build_email(username)

        msg = MIMEMultipart()
        msg["From"] = SENDER_EMAIL
        msg["To"] = to_email
        msg["Subject"] = subject
        msg.attach(MIMEText(body, "plain"))

        if dry_run:
            print(f"  [DRY RUN] {username:20s} -> {to_email}")
        else:
            try:
                server.sendmail(SENDER_EMAIL, to_email, msg.as_string())
                print(f"  OK  {username:20s} -> {to_email}")
                sent += 1
                time.sleep(2)  # stay well under Office 365 rate limits (30 msg/min)
            except Exception as exc:
                print(f"  ERR {username:20s} -> {to_email}  ({exc})")
                failed += 1

    if server:
        server.quit()

    if not dry_run:
        print(f"\nDone. {sent} sent, {failed} failed.")
    else:
        print(f"\nDry run complete — {len(RECIPIENTS)} emails staged. Set dry_run=False to send.")


if __name__ == "__main__":
    # Preview all emails first (dry_run=True).
    # When ready: export HOTICA_EMAIL_PASSWORD="your-password" then change to dry_run=False
    send_emails(dry_run=False)
