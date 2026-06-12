import requests
import os

KEYWORDS = [
    "خانه به دوش",
    "متهم گریخت",
    "ترش و شیرین",
    "بزنگاه"
]

URL = "https://en.ifilmtv.ir/Schedule/Index"

TOKEN = os.environ.get("TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")

def send(msg):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": CHAT_ID, "text": msg})

html = requests.get(URL).text

found = []

for k in KEYWORDS:
    if k in html:
        found.append(k)

if found:
    send("📺 سریال پیدا شد:\n" + "\n".join(found))
