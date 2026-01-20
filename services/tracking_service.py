import requests
import logging


TRACKING_API_URL = "https://staging.bvclogistics.com/BVCUniverseAPI/rest/BVCAPI/TrackShipments"

HEADERS = {
    "X-Contacts-AppId": "NGipu5GRSpxNhK6rDlgQCJj1n",
    "X-Contacts-Key": "D9foQOsaw0duoL0zH8C0SqpcBgCwCCNBjXUalWV6XzE2AYBjRJ"
}

def get_tracking_status(shipping_note_no: str) -> str:
    try:
        res = requests.get(
            TRACKING_API_URL,
            params={"ShippingNoteNo": shipping_note_no},
            headers=HEADERS,
            timeout=5
        )
        res.raise_for_status()
        data = res.json()

        if not data:
            return "Please register and come again"

        return data[0].get("TrackingStatus", "Status not available")

    except requests.exceptions.Timeout:
        logging.exception("Tracking timeout")
        return "⏳ Tracking system is slow."

    except requests.exceptions.RequestException:
        logging.exception("Tracking error")
        return "❌ Unable to fetch tracking details."


# ---------------- Hub / Pincode ----------------
BOT_API_URL = "https://prod.bvclogistics.com/BVCUniverseAPI/rest/Bot/BotAPI"

BOT_HEADERS = {
    "Authorization": "Basic YnZjQm90VXNlcjpCdmNAYm90XjM0NTY="
}

def get_hub_details(pincode: str) -> dict:
    try:
        res = requests.get(
            BOT_API_URL,
            params={
                "API_Name": "HubDetailsAPI",
                "PAN": "AADCM9043R",
                "Pincode": pincode
            },
            headers=BOT_HEADERS,
            timeout=5
        )
        res.raise_for_status()
        return res.json()

    except requests.exceptions.Timeout:
        return {"error": "⏳ Hub service timeout"}

    except requests.exceptions.RequestException:
        return {"error": "❌ Hub service unavailable"}
