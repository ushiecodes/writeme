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

    # strip everything before the first markdown heading
    # audit reports, preamble, and security questions appear before the README
    heading_index = text.find("\n# ")
    if heading_index != -1:
        text = text[heading_index:].strip()
    elif text.startswith("# "):
        pass  # already starts with heading, no strip needed
    else:
        # last resort — find any heading
        for prefix in ["## ", "### "]:
            idx = text.find(prefix)
            if idx != -1:
                text = text[idx:].strip()
                break

    return text
