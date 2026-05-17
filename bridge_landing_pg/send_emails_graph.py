import time
import json
import msal
import requests

CLIENT_ID = "ecf4d467-50dd-4eb9-a33f-fcd556630573"
TENANT_ID = "100bac27-926b-4cb3-b200-31f08d12370f"
SENDER_EMAIL = "effortbuildingcontractors@woodlaine.com"
SCOPES = ["Mail.Send"]

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


def build_body(username: str) -> str:
    return f"""\
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

Please send your photos and videos to:
  effortbuildingcontractors@woodlaine.com

The sooner we receive your content, the sooner your page goes live.

If you have any questions or need guidance on what to send, just reply to this email — we are happy to help.

Best regards,
The Hotica Team\
"""


def get_access_token() -> str:
    app = msal.PublicClientApplication(
        CLIENT_ID,
        authority=f"https://login.microsoftonline.com/{TENANT_ID}",
    )

    # Try cached token first
    accounts = app.get_accounts()
    if accounts:
        result = app.acquire_token_silent(SCOPES, account=accounts[0])
        if result and "access_token" in result:
            print("Using cached token.\n")
            return result["access_token"]

    # Device code flow — user authenticates in browser
    flow = app.initiate_device_flow(scopes=SCOPES)
    if "user_code" not in flow:
        raise RuntimeError(f"Failed to create device flow: {flow}")

    print("\n" + "=" * 60)
    print(flow["message"])
    print("=" * 60 + "\n")

    result = app.acquire_token_by_device_flow(flow)
    if "access_token" not in result:
        raise RuntimeError(f"Auth failed: {result.get('error_description', result)}")

    return result["access_token"]


def send_email(token: str, username: str, to_email: str) -> bool:
    payload = {
        "message": {
            "subject": "Your Personal Hotica Landing Page — We Need Your Photos & Videos",
            "body": {
                "contentType": "Text",
                "content": build_body(username),
            },
            "toRecipients": [
                {"emailAddress": {"address": to_email}}
            ],
        },
        "saveToSentItems": True,
    }

    resp = requests.post(
        "https://graph.microsoft.com/v1.0/me/sendMail",
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
        },
        data=json.dumps(payload),
        timeout=15,
    )

    return resp.status_code == 202


def main():
    print("Authenticating with Microsoft — follow the instructions below.\n")
    token = get_access_token()
    print("Authenticated. Starting to send...\n")

    sent, failed = 0, 0
    for username, email in RECIPIENTS:
        ok = send_email(token, username, email)
        if ok:
            print(f"  OK  {username:20s} -> {email}")
            sent += 1
        else:
            print(f"  ERR {username:20s} -> {email}")
            failed += 1
        time.sleep(1)

    print(f"\nDone. {sent} sent, {failed} failed.")


if __name__ == "__main__":
    main()
