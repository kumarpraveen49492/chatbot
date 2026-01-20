import requests
import os

GUPSHUP_API_URL = "https://api.gupshup.io/sm/api/v1/msg"
GUPSHUP_API_KEY = os.getenv("GUPSHUP_API_KEY")

def send_whatsapp_message(source: str, destination: str, message: str):
    headers = {
        "apikey": GUPSHUP_API_KEY,
        "Content-Type": "application/x-www-form-urlencoded"
    }

    data = {
        "channel": "whatsapp",
        "source": source,          
        "destination": destination,  
        "message": message
    }

    requests.post(GUPSHUP_API_URL, headers=headers, data=data, timeout=10)

