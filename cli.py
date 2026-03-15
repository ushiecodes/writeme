import argparse
from interview import run_interview
from gemini import generate_readme
from writer import write_readme
from config import get_api_key, reset_api_key

def main():
    parser = argparse.ArgumentParser(
        prog="turtell",
        description="AI-powered README generator"
    )
    parser.add_argument(
        "--reset",
        action="store_true",
        help="Reset your saved Gemini API key"
    )
    parser.add_argument(
        "--version",
        action="store_true",
        help="Show the current version"
    )
    args = parser.parse_args()

    if args.reset:
        reset_api_key()
        return

    if args.version:
        try:
            from importlib.metadata import version
            print(f"turtell v{version('turtell')}")
        except Exception:
            print("turtell v0.1.0")
        return

    # confirm API key exists before starting interview
    get_api_key()
