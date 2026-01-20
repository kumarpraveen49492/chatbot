from fastapi import FastAPI, Request
from services.whatsapp_service import send_whatsapp_message
from core.session import get_session
from handlers.greeting import handle_greeting
from handlers.menu_handler import handle_menu
from handlers.tracking import handle_tracking, handle_hub_menu
from utils.validators import is_valid_shipment_no

app = FastAPI()

GUPSHUP_SOURCE_NUMBER = "918652633632"  # your WhatsApp business number

@app.post("/webhook/whatsapp")
async def whatsapp_webhook(request: Request):
    payload = await request.json()

    
    user_id = payload["payload"]["source"]
    msg = payload["payload"]["payload"]["text"].strip()

    # --- EXISTING CHATBOT LOGIC ---
    reply = handle_greeting(user_id, msg)
    if reply is None:
        session = get_session(user_id)
        if not session:
            if is_valid_shipment_no(msg):
                reply = handle_tracking(user_id, msg)
            elif msg.isdigit():
                reply = {"reply": "👋 Please say *Hi* to start the conversation."}
            else:
                reply = handle_menu(user_id, msg)
        else:
            stage = session["stage"]
            if stage == "MENU":
                reply = handle_menu(user_id, msg)
            elif stage == "TRACKING":
                reply = handle_tracking(user_id, msg)
            elif stage in ["HUB", "PINCODE"]:
                option = "2" if stage == "HUB" else "3"
                reply = handle_hub_menu(user_id, option, msg)
            else:
                reply = {"reply": "❌ Unable to process request"}

    
    send_whatsapp_message(
        source=GUPSHUP_SOURCE_NUMBER,
        destination=user_id,
        message=reply["reply"]
    )

    
    return {"status": "ok"}
