import os
import json
from pathlib import Path
from dotenv import load_dotenv
from display import print_info, print_success

CONFIG_DIR = Path.home() / ".config" / "writeme"
CONFIG_FILE = CONFIG_DIR / "config.json"

load_dotenv(dotenv_path=".env.local")  # always load, not conditionally

def save_api_key(api_key: str) -> None:
    CONFIG_DIR.mkdir(parents=True, exist_ok=True)
    with open(CONFIG_FILE, "w") as f:
        json.dump({"api_key": api_key}, f)  # fixed: was "api.key"

def load_api_key() -> str | None:
    if CONFIG_FILE.exists():
        with open(CONFIG_FILE) as f:
            data = json.load(f)
            return data.get("api_key")  # now matches save
    return os.getenv("API_KEY")

def prompt_for_api_key() -> str:
    print_info("No API key found...")
    print_info("Get one at: https://aistudio.google.com/api-keys")
    api_key = input("Enter your Gemini API Key: ").strip()
    save_api_key(api_key)
    print_success("API Key Saved...")
    return api_key

def get_api_key() -> str:
    api_key = load_api_key()
    if not api_key:
        api_key = prompt_for_api_key()
    return api_key

def reset_api_key() -> None:
    if CONFIG_FILE.exists():
        CONFIG_FILE.unlink()
        print_success("API key removed.")
    else:
        print_info("No saved API key was found.")
