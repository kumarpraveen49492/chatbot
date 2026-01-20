from core.session import update_stage, clear_session
from core.menu import menu_message

def handle_menu(user_id, msg):
    msg = msg.strip()

    if msg == "1":
        update_stage(user_id, "TRACKING")
        return {"reply": "📦 Please enter your shipment number."}

    if msg == "2":
        update_stage(user_id, "HUB")
        return {"reply": "🏢 Please enter the pincode to get hub details."}

    if msg == "3":
        update_stage(user_id, "PINCODE")
        return {"reply": "📍 Please enter the pincode to check serviceability."}

    if msg == "4":
        clear_session(user_id)
        return {"reply": "Please contact support at support@bvclogistics.com"}

    # 🚫 invalid numbers
    if msg.isdigit():
        return {"reply": "❌ Please choose *1, 2, 3 or 4* only."}

    return {"reply": menu_message()}
