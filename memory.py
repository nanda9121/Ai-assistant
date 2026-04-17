import json
import os

MEMORY_FILE = "memory.json"

DEFAULT_MEMORY = {
    "user_name": "Nanda",
    "facts": [],
    "preferences": [],
    "recent_topics": []
}

def load_memory():
    if os.path.exists(MEMORY_FILE):
        try:
            with open(MEMORY_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except json.JSONDecodeError:
            return DEFAULT_MEMORY.copy()
    return DEFAULT_MEMORY.copy()

def save_memory(memory_data):
    with open(MEMORY_FILE, "w", encoding="utf-8") as f:
        json.dump(memory_data, f, indent=2)

def clear_memory():
    save_memory(DEFAULT_MEMORY.copy())

def add_fact(fact):
    memory = load_memory()
    if fact and fact not in memory["facts"]:
        memory["facts"].append(fact)
    save_memory(memory)

def memory_as_text():
    memory = load_memory()
    return (
        f"User name: {memory.get('user_name', '')}\n"
        f"Facts: {', '.join(memory.get('facts', []))}\n"
        f"Preferences: {', '.join(memory.get('preferences', []))}\n"
        f"Recent topics: {', '.join(memory.get('recent_topics', []))}"
    )
