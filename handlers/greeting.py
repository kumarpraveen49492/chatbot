from core.session import create_session
from core.menu import menu_message

def handle_greeting(user_id, msg):
    msg = msg.strip().lower()

    
    if msg.isdigit():
        return None

    if msg in ["hi", "hello", "hey", "good morning", "good evening"]:
        create_session(user_id, "MENU")
        return {"reply": menu_message()}

    return {"reply": "👋 Please say *Hi* to start the conversation."}



