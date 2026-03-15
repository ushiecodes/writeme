import argparse
from interview import run_interview
from gemini import generate_readme
from writer import write_readme
from config import get_api_key, reset_api_key


def main():
    parser = argparse.ArgumentParser(
        prog="writeme", description="AI-powered README generator"
    )
    parser.add_argument(
        "--reset", action="store_true", help="Reset your saved Gemini API key"
    )
    parser.add_argument(
        "--version", action="store_true", help="Show the current version"
    )
    args = parser.parse_args()

    if args.reset:
        reset_api_key()
        return

    if args.version:
        try:
            from importlib.metadata import version

            print(f"writeme v{version('writeme')}")
        except Exception:
            print("writeme v0.1.0")
        return

    # confirm API key exists before starting interview
    get_api_key()

    print("\nWelcome to WriteMe — AI-powered README generator")
    print("=" * 60)
    print("This tool will interview you about your project and")
    print("generate a complete README.md in the current directory.")
    print("=" * 60 + "\n")

    # run the interview
    answers = run_interview()

    # generate readme from answers + codebase scan
    readme_content = generate_readme(answers)

    # write to file
    write_readme(readme_content)

    print("\nDone. Your README is ready.")
