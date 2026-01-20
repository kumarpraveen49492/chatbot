from core.session import create_session
from core.menu import menu_message

def handle_greeting(user_id, msg):
    msg = msg.strip().lower()

    greetings = ["hi", "hello", "hey", "good morning", "good evening"]

    if msg in greetings:
        create_session(user_id, "MENU")
        return {"reply": menu_message()}

    
    return None




