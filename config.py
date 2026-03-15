import os
import json
from pathlib import Path
from dotenv import load_dotenv

CONFIG_DIR = Path.home() / ".config" / "turtell"
CONFIG_FILE = CONFIG_DIR / "config.json"

def save_api_key(api_key: str) -> None:
    CONFIG_DIR.mkdir(parents=True, exist_ok=True)
    with open(CONFIG_FILE, "w") as f:
        json.dump({"api.key": api_key}, f)

def load_api_key() -> str | None:
    if CONFIG_FILE.exists():
        with open(CONFIG_FILE) as f:
            data = json.load(f)
            return data.get("api_key")
    
    load_dotenv(dotenv_path=".env.local")
    return os.getenv("API_KEY")

def prompt_for_api_key() -> str:
    print("\nNo API key found...")
    print("Get one at: https://aistudio.google.com/api-keys")
    api_key = input("Enter your Gemini API Key: ").strip()
    save_api_key(api_key)
    print("API Key Saved...\n")
    return api_key

def get_api_key() -> str:
    api_key = load_api_key()
    if not api_key:
        api_key = prompt_for_api_key()
    return api_key

def reset_api_key() -> None:
    if CONFIG_FILE.exists():
        CONFIG_FILE.unlink()
        print("API Key was removed...")
    else:
        print("No saved API Key was found...")
