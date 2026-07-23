import json
import os

CHAT_FILE = "chat_history.json"
MAX_MESSAGES = 10

def load_chat():
    if not os.path.exists(CHAT_FILE):
        return []

    with open(CHAT_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_chat(chat):
    with open(CHAT_FILE, "w", encoding="utf-8") as f:
        json.dump(chat, f, ensure_ascii=False, indent=4)

def add_message(role, content):
    chat = load_chat()

    chat.append({
        "role": role,
        "content": content
    })

    chat = chat[-MAX_MESSAGES:]

    save_chat(chat)

def get_chat():
    return load_chat()

def clear_chat():
    save_chat([])
