import argparse
from interview import run_interview
from gemini import generate_readme
from writer import write_readme
from config import get_api_key, reset_api_key
from display import print_banner, print_success, print_error, console


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
            console.print(f"[bold cyan]writeme[/bold cyan] [white]v{version('writeme')}[/white]")
        except Exception:
            console.print("[bold cyan]writeme[/bold cyan] [white]v0.1.0[/white]")
        return

    # print banner
    print_banner()

    # confirm API key exists before starting interview
    get_api_key()

    console.print(
        "\n[dim]This tool will interview you about your project and "
        "generate a complete README.md in the current directory.[/dim]\n"
    )

    # run the interview
    answers = run_interview()

    # generate readme from answers + codebase scan
    console.print("\n[dim]Scanning codebase and generating README...[/dim]")
    readme_content = generate_readme(answers)

    # write to file
    write_readme(readme_content)

    print_success("Done. Your README is ready.")

