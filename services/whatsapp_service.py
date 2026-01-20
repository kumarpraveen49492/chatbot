import requests
import os

GUPSHUP_API_URL = "https://api.gupshup.io/sm/api/v1/msg"
GUPSHUP_API_KEY = os.getenv("GUPSHUP_API_KEY")

def send_whatsapp_message(source: str, destination: str, message: str):
    if not GUPSHUP_API_KEY:
        print("❌ GUPSHUP_API_KEY not found in environment")
        return

    headers = {
        "apikey": GUPSHUP_API_KEY,
        "Content-Type": "application/x-www-form-urlencoded"
    }

    data = {
        "channel": "whatsapp",
        "source": source,           # your Gupshup WhatsApp number
        "destination": destination, # user WhatsApp number
        "message": message
    }

    try:
        response = requests.post(
            GUPSHUP_API_URL,
            headers=headers,
            data=data,
            timeout=10
        )

        print("📨 Gupshup response:", response.status_code, response.text)

    except Exception as e:
        print("❌ WhatsApp send failed:", e)

