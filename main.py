from fastapi import FastAPI, Request
from core.session import get_session
from handlers.greeting import handle_greeting
from handlers.menu_handler import handle_menu
from handlers.tracking import handle_tracking, handle_hub_menu

app = FastAPI()

@app.post("/webhook/whatsapp")
async def whatsapp_webhook(request: Request):
    payload = await request.json()
    msg = payload.get("text", "").strip()
    user_id = payload.get("sender")

    print("MESSAGE:", msg)

    # 1️⃣ Greeting
    reply = handle_greeting(user_id, msg)
    if reply is not None:
        return reply

    session = get_session(user_id)

    # 2️⃣ No session
    if not session:
        if msg.isdigit():
            return {"reply": "👋 Please say *Hi* to start."}
        return handle_menu(user_id, msg)

    stage = session["stage"]

    # 3️⃣ Menu
    if stage == "MENU":
        return handle_menu(user_id, msg)

    # 4️⃣ Tracking
    if stage == "TRACKING":
        return handle_tracking(user_id, msg)

    # 5️⃣ Hub / Pincode
    if stage in ["HUB", "PINCODE"]:
        option = "2" if stage == "HUB" else "3"
        return handle_hub_menu(user_id, option, msg)

    return {"reply": "❌ Unable to process request"}
