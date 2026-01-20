from core.session import clear_session
from services.tracking_service import get_tracking_status, get_hub_details
from utils.validators import is_valid_shipment_no

def handle_tracking(user_id, msg):
    if not is_valid_shipment_no(msg):
        return {"reply": "❌ Please enter a valid shipment number (e.g. OS509911)."}

    status = get_tracking_status(msg)
    clear_session(user_id)

    return {
        "reply": f"📦 Shipment *{msg}* status:\n*{status}*\n\n Say *Hi* to start again."
    }


def handle_hub_menu(user_id, option, pincode):
    if not pincode.isdigit() or len(pincode) != 6:
        return {"reply": "❌ Please enter a valid 6-digit pincode."}

    data = get_hub_details(pincode)

   
    if not data or not data.get("HubName"):
        return {
             " There are no nearby hub points to your location.Please enter another pincode."
        }

    if data.get("error"):
        return {"reply": data["error"]}

    clear_session(user_id)

    if option == "2":
        return {
            "reply": (
                f"📍 *Hub Details*\n"
                f"Hub Name: {data.get('HubName')}\n"
                f"City: {data.get('HubCity')}\n"
                f"Address: {data.get('Address1')}\n"
                f"Email: {data.get('Email')}\n"
                f"Location: {data.get('Location')}\n\n"
                "Say *Hi* to start again."
            )
        }

    if option == "3":
        status = data.get("PincodeType")
        msg = "✅ SERVICEABLE" if status == "Serviceable" else "❌ NOT SERVICEABLE"
        return {"reply": f"{msg}\nSay *Hi* to start again."}

    return {"reply": "❌ Invalid option"}
