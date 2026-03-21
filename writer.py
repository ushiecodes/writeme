from pathlib import Path


def write_readme(content: str, directory: str = ".") -> None:
    readme_path = Path(directory) / "README.md"

    # clean gemini's markdown wrapping if present
    content = _clean_output(content)

    if readme_path.exists():
        print(f"\nA README.md already exists in {Path(directory).resolve()}")
        print("[O]verwrite   [A]ppend   [C]ancel")
        choice = input("> ").strip().lower()

        if choice == "o":
            readme_path.write_text(content, encoding="utf-8")
            print("README.md overwritten.")
        elif choice == "a":
            existing = readme_path.read_text(encoding="utf-8")
            readme_path.write_text(existing + "\n\n" + content, encoding="utf-8")
            print("README.md updated.")
        elif choice == "c":
            print("Cancelled. README.md was not modified.")
        else:
            print("Invalid choice. README.md was not modified.")
    else:
        readme_path.write_text(content, encoding="utf-8")
        print(f"\nREADME.md created at {readme_path.resolve()}")

def _clean_output(text: str) -> str:
    text = text.strip()

    # strip markdown code fences
    if text.startswith("```markdown"):
        text = text[len("```markdown"):].strip()
    if text.startswith("```"):
        text = text[3:].strip()
    if text.endswith("```"):
        text = text[:-3].strip()

    # strip everything before the first top-level heading
    # only match # at the very start of a line, not inside code blocks
    lines = text.split("\n")
    for i, line in enumerate(lines):
        if line.startswith("# "):
            text = "\n".join(lines[i:])
            return text.strip()

    return text.strip()
