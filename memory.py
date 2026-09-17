import json
from pathlib import Path

MEMORY_FILE = Path("memory.json")

def load_memory():
    if not MEMORY_FILE.exists():
        return {}

    try:
        with open(MEMORY_FILE, "r") as file:
            return json.load(file) 

    except json.JSONDecodeError:
        return {}

def save_memory(memory):
    with open(MEMORY_FILE, "w") as file:
        json.dump(memory, file, indent=4)

def remember(key, value):
    memory = load_memory()
    memory[key] = value
    save_memory(memory)

def recall(key):
    memory = load_memory()
    return memory.get(key)

def forget(key):
    memory = load_memory()

    if key in memory:
        del memory[key]
        save_memory(memory)
        return True
    return False