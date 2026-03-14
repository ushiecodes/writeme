def run_phase_one() -> dict:
    answers = {}
    print("PHASE 1 — Publishable Draft")
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
    answers = {}

    print("PHASE 2 — Depth Layer")
    print("Batch A: Usage and Configuration")
    # Q6
    print("Q6. List every major feature with a one-line description of what it does.")
    print("    Type END on a new line when done:")
    lines = []
    while True:
        line = input()
        if line.strip().upper() == "END":
            break
        lines.append(line)
    answers["q6"] = "\n".join(lines).strip()

    # Q7
    print("\nQ7. Walk me through the primary workflow — from launch to first result.")
    print("    What does the user see, type, and receive at each step?")
    print("    Type END on a new line when done:")
    lines = []
    while True:
        line = input()
        if line.strip().upper() == "END":
            break
        lines.append(line)
    answers["q7"] = "\n".join(lines).strip()

    # Q8
    print("\nQ8. Are there different user roles, modes, or permission levels?")
    print("    If yes, what can each do? If no, just say 'none'.")
    answers["q8"] = input("> ").strip()

    # Q9
    print("\nQ9. List every configuration option in this format:")
    print("    VARIABLE_NAME | what it controls | default value | valid values | required?")
    print("    One line per variable. Type END on a new line when done:")
    lines = []
    while True:
        line = input()
        if line.strip().upper() == "END":
            break
        lines.append(line)
    answers["q9"] = "\n".join(lines).strip()

    # Q9b
    print("\nQ9b. How does the app load these variables? Check all that apply:")
    print("  - .env file read by a library (e.g. python-dotenv)")
    print("  - Shell environment variables set before launch")
    print("  - Config file (.yaml, .toml, .json, .ini)")
    print("  - Cloud secrets manager (AWS Secrets Manager, Vault, etc.)")
    print("  - Hardcoded defaults with env override")
    print("  - Other — describe")
    answers["q9b"] = input("> ").strip()

    # Q10
    print("\nQ10. Which config values are sensitive (passwords, tokens, API keys)?")
    print("     Where are they stored and how are they protected?")
    answers["q10"] = input("> ").strip()

    # Q11
    print("\nQ11. What happens if a required config value is missing?")
    print("     Does the app crash immediately with a clear message, or fail downstream?")
    print("     If you are not certain, say so.")
    answers["q11"] = input("> ").strip()

    print("\n" + "="*60)
    print("Batch A complete. Moving to Batch B: Architecture.")
    print("="*60 + "\n")

    # Q12
    print("Q12. Paste the output of `tree` or equivalent from your project root.")
    print("     Windows: tree /F")
    print("     Linux/Mac: find . -not -path '*/.*' | sort")
    print("     Type END on a new line when done:")
    lines = []
    while True:
        line = input()
        if line.strip().upper() == "END":
            break
        lines.append(line)
    answers["q12"] = "\n".join(lines).strip()

    # Q13
    print("\nQ13. For each folder in that tree, write its single responsibility in one sentence.")
    print("     Type END on a new line when done:")
    lines = []
    while True:
        line = input()
        if line.strip().upper() == "END":
            break
        lines.append(line)
    answers["q13"] = "\n".join(lines).strip()

    # Q14
    print("\nQ14. Starting from the moment a user triggers the primary action —")
    print("     name every function, module, or service that executes, in exact order.")
    print("     Include every database query. Format as a numbered list.")
    print("     Type END on a new line when done:")
    lines = []
    while True:
        line = input()
        if line.strip().upper() == "END":
            break
        lines.append(line)
    answers["q14"] = "\n".join(lines).strip()

    # Q15
    print("\nQ15. How do the major components communicate?")
    print("     (function calls, HTTP, serial port, message queue, shared DB, events, other)")
    answers["q15"] = input("> ").strip()

    # Q16
    print("\nQ16. What are the non-obvious design decisions in this project?")
    print("     Things that look strange but were deliberate — and why.")
    print("     Type END on a new line when done:")
    lines = []
    while True:
        line = input()
        if line.strip().upper() == "END":
            break
        lines.append(line)
    answers["q16"] = "\n".join(lines).strip()

    print("\n" + "="*60)
    print("Phase 2 complete.")
    print("="*60 + "\n")

    return answers
    

def run_phase_three() -> dict:
    pass
