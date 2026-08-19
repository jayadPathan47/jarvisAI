import json
import os

MEMORY_FILE = "memory.json"


def load_memory():

    if not os.path.exists(MEMORY_FILE):
        return []

    try:

        with open(MEMORY_FILE, "r", encoding="utf-8") as file:
            return json.load(file)

    except Exception:

        return []


def save_memory(memory):

    with open(MEMORY_FILE, "w", encoding="utf-8") as file:

        json.dump(
            memory,
            file,
            indent=4,
            ensure_ascii=False
        )


def add_memory(user_message, jarvis_response):

    memory = load_memory()

    memory.append({
        "user": user_message,
        "jarvis": jarvis_response
    })

    # Keep only latest 20 conversations
    memory = memory[-20:]

    save_memory(memory)


def get_memory():

    return load_memory()


def clear_memory():

    save_memory([])