def run_phase_one() -> dict:
    answers = {}

    # Q1
    print("Q1. What does this project do, who is it for, and what problem does it solve?")
    answers["q1"] = input("> ").strip()

    # Q2
    print("\nQ2. What is the full tech stack?")
    print("  - Language and version")
    print("  - Database, if any")
    print("  - Hardware, if any")
    print("  - Operating system(s) it runs on")
    print("  - Package manager used")
    answers["q2"] = input("> ").strip()

    # Q3
    print("\nQ3. Paste your exact terminal session from a clean setup to a running app.")
    print("    (literal commands you typed and the output you saw)")
    print("    If mid-build, list commands in order and mark uncertain steps with [?]")
    print("    Paste everything, then type END on a new line and press Enter:")
    lines = []
    while True:
        line = input()
        if line.strip().upper() == "END":
            break
        lines.append(line)
    answers["q3"] = "\n".join(lines).strip()

    # Q4
    print("\nQ4. What does a fully successful run look like?")
    print("    Paste the terminal output or describe exactly what the user sees:")
    print("    Type END on a new line when done:")
    lines = []
    while True:
        line = input()
        if line.strip().upper() == "END":
            break
        lines.append(line)
    answers["q4"] = "\n".join(lines).strip()

    # Q5
    print("\nQ5. What are the 3 errors people most commonly hit during setup?")
    print("    For each: paste the exact error message and the exact fix.")
    print("    Type END on a new line when done:")
    lines = []
    while True:
        line = input()
        if line.strip().upper() == "END":
            break
        lines.append(line)
    answers["q5"] = "\n".join(lines).strip()

    print("\n" + "="*60)
    print("Phase 1 complete. Sending to Gemini...")
    print("="*60 + "\n")

    return answers

def run_phase_two() -> dict:
    pass


def run_phase_three() -> dict:
    pass
