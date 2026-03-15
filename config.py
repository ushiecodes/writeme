import os
import json
from pathlib import Path
from dotenv import load_dotenv

CONFIG_DIR = Path.home() / ".config" / "turtell"
CONFIG_FILE = CONFIG_DIR / "config.json"
