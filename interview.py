SKIP_KEYWORD = "SKIP"
QUIT_KEYWORD = "QUIT"
TLDR_KEYWORD = "TLDR"

GENERIC_ANSWERS = {
    "q1": "[SKIPPED — infer project purpose, target user, and problem solved from codebase]",
    "q2": "[SKIPPED — infer tech stack from pyproject.toml, requirements.txt, or equivalent]",
    "q3": "[SKIPPED — infer setup steps from project structure and dependency files]",
    "q4": "[SKIPPED — infer expected output from main entry point and codebase]",
    "q5": "[SKIPPED — list common setup errors based on the tech stack and dependencies]",
    "q6": "[SKIPPED — infer major features from codebase and project structure]",
    "q7": "[SKIPPED — infer primary workflow from entry point and module structure]",
    "q8": "[SKIPPED — infer user roles or modes from codebase, default to single user if unclear]",
    "q9": "[SKIPPED — infer configuration options from codebase and environment variable usage]",
    "q9b": "[SKIPPED — infer config loading mechanism from codebase]",
    "q10": "[SKIPPED — infer sensitive config values from variable names and usage patterns]",
    "q11": "[SKIPPED — infer failure behaviour on missing config from codebase]",
    "q12": "[SKIPPED — project tree will be provided via codebase scan]",
    "q13": "[SKIPPED — infer folder responsibilities from project structure and file names]",
    "q14": "[SKIPPED — infer critical execution path from entry point and module imports]",
    "q15": "[SKIPPED — infer component communication model from codebase]",
    "q16": "[SKIPPED — no non-obvious design decisions provided]",
    "q17": "[SKIPPED — infer sensitive data handled from variable names and API usage]",
    "q18": "[SKIPPED — infer auth model from codebase, default to none if not present]",
    "q19": "[SKIPPED — infer network exposure from codebase and dependencies]",
    "q20": "[SKIPPED — .gitignore not provided]",
    "q21": "[SKIPPED — dependency audit not run, include warning block in security section]",
    "q22": "[SKIPPED — no known security limitations provided]",
    "q23": "[SKIPPED — infer deployment target from project type and structure]",
    "q24": "[SKIPPED — no containerisation or environment differences provided]",
    "q25": "[SKIPPED — no production-specific setup steps provided]",
    "q26": "[SKIPPED — git log not provided, generate changelog from feature list]",
    "q27": "[SKIPPED — no contribution guidelines provided]",
    "q28": "[SKIPPED — no bug reporting process provided]",
    "q29": "[SKIPPED — no maintainer contact provided]",
    "q30": "[SKIPPED — no license or attribution provided]",
}

CONTINUE_SENTINEL = object()

def _print_controls():
    print("  (Type SKIP to skip this question, TLDR for a generic answer, QUIT to exit)\n")


def _handle_quit(all_answers: dict):
    print("\nAre you sure you want to quit?")
    print("Your current progress will be used to generate a partial README.")
    print("[Y] Quit and generate with current answers")
    print("[N] Continue the questionnaire")
    choice = input("> ").strip().upper()
    if choice == "Y":
        return all_answers
    return CONTINUE_SENTINEL


def _read_single(prompt_key: str) -> str:
    response = input("> ").strip()
    if response.upper() == SKIP_KEYWORD or response.upper() == TLDR_KEYWORD:
        print("  → Using generic answer.")
        return GENERIC_ANSWERS[prompt_key]
    if response.upper() == QUIT_KEYWORD:
        return QUIT_KEYWORD
    return response


def _read_multiline(prompt_key: str) -> str:
    print("  (Type END on a new line to submit, SKIP to skip, TLDR for generic, QUIT to exit)")
    lines = []
    while True:
        line = input()
        if line.strip().upper() == "END":
            break
        if line.strip().upper() in (SKIP_KEYWORD, TLDR_KEYWORD):
            print("  → Using generic answer.")
            return GENERIC_ANSWERS[prompt_key]
        if line.strip().upper() == QUIT_KEYWORD:
            return QUIT_KEYWORD
        lines.append(line)
    result = "\n".join(lines).strip()
    if not result:
        print("  → Empty answer. Using generic answer.")
        return GENERIC_ANSWERS[prompt_key]
    return result


def run_phase_one(all_answers: dict):
    print("\n" + "="*60)
    print("PHASE 1 — Publishable Draft")
    print("="*60)
    _print_controls()

    # Q1
    print("Q1. What does this project do, who is it for, and what problem does it solve?")
    result = _read_single("q1")
    if result == QUIT_KEYWORD:
        quit_result = _handle_quit(all_answers)
        if quit_result is CONTINUE_SENTINEL:
            pass
        else:
            return quit_result
    else:
        all_answers["q1"] = result

    # Q2
    print("\nQ2. What is the full tech stack?")
    print("  - Language and version")
    print("  - Database, if any")
    print("  - Hardware, if any")
    print("  - Operating system(s) it runs on")
    print("  - Package manager used")
    result = _read_single("q2")
    if result == QUIT_KEYWORD:
        quit_result = _handle_quit(all_answers)
        if quit_result is CONTINUE_SENTINEL:
            pass
        else:
            return quit_result
    else:
        all_answers["q2"] = result

    # Q3
    print("\nQ3. Paste your exact terminal session from a clean setup to a running app.")
    print("    If mid-build, list commands in order and mark uncertain steps with [?]")
    result = _read_multiline("q3")
    if result == QUIT_KEYWORD:
        quit_result = _handle_quit(all_answers)
        if quit_result is CONTINUE_SENTINEL:
            pass
        else:
            return quit_result
    else:
        all_answers["q3"] = result

    # Q4
    print("\nQ4. What does a fully successful run look like?")
    print("    Paste the terminal output or describe exactly what the user sees:")
    result = _read_multiline("q4")
    if result == QUIT_KEYWORD:
        quit_result = _handle_quit(all_answers)
        if quit_result is CONTINUE_SENTINEL:
            pass
        else:
            return quit_result
    else:
        all_answers["q4"] = result

    # Q5
    print("\nQ5. What are the 3 errors people most commonly hit during setup?")
    print("    For each: paste the exact error message and the exact fix.")
    result = _read_multiline("q5")
    if result == QUIT_KEYWORD:
        quit_result = _handle_quit(all_answers)
        if quit_result is CONTINUE_SENTINEL:
            pass
        else:
            return quit_result
    else:
        all_answers["q5"] = result

    print("\nPhase 1 complete.")
    return all_answers

def run_phase_two(all_answers: dict):
    print("\n" + "="*60)
    print("PHASE 2 — Depth Layer")
    print("Batch A: Usage and Configuration")
    print("="*60)
    _print_controls()

    # Q6
    print("Q6. List every major feature with a one-line description of what it does.")
    result = _read_multiline("q6")
    if result == QUIT_KEYWORD:
        quit_result = _handle_quit(all_answers)
        if quit_result is CONTINUE_SENTINEL:
            pass
        else:
            return quit_result
    else:
        all_answers["q6"] = result

    # Q7
    print("\nQ7. Walk me through the primary workflow — from launch to first result.")
    print("    What does the user see, type, and receive at each step?")
    result = _read_multiline("q7")
    if result == QUIT_KEYWORD:
        quit_result = _handle_quit(all_answers)
        if quit_result is CONTINUE_SENTINEL:
            pass
        else:
            return quit_result
    else:
        all_answers["q7"] = result

    # Q8
    print("\nQ8. Are there different user roles, modes, or permission levels?")
    print("    If yes, what can each do? If no, just say 'none'.")
    result = _read_single("q8")
    if result == QUIT_KEYWORD:
        quit_result = _handle_quit(all_answers)
        if quit_result is CONTINUE_SENTINEL:
            pass
        else:
            return quit_result
    else:
        all_answers["q8"] = result

    # Q9
    print("\nQ9. List every configuration option in this format:")
    print("    VARIABLE_NAME | what it controls | default value | valid values | required?")
    print("    One line per variable.")
    result = _read_multiline("q9")
    if result == QUIT_KEYWORD:
        quit_result = _handle_quit(all_answers)
        if quit_result is CONTINUE_SENTINEL:
            pass
        else:
            return quit_result
    else:
        all_answers["q9"] = result

    # Q9b
    print("\nQ9b. How does the app load these variables? Check all that apply:")
    print("  - .env file read by a library (e.g. python-dotenv)")
    print("  - Shell environment variables set before launch")
    print("  - Config file (.yaml, .toml, .json, .ini)")
    print("  - Cloud secrets manager")
    print("  - Hardcoded defaults with env override")
    print("  - Other — describe")
    result = _read_single("q9b")
    if result == QUIT_KEYWORD:
        quit_result = _handle_quit(all_answers)
        if quit_result is CONTINUE_SENTINEL:
            pass
        else:
            return quit_result
    else:
        all_answers["q9b"] = result

    # Q10
    print("\nQ10. Which config values are sensitive (passwords, tokens, API keys)?")
    print("     Where are they stored and how are they protected?")
    result = _read_single("q10")
    if result == QUIT_KEYWORD:
        quit_result = _handle_quit(all_answers)
        if quit_result is CONTINUE_SENTINEL:
            pass
        else:
            return quit_result
    else:
        all_answers["q10"] = result

    # Q11
    print("\nQ11. What happens if a required config value is missing?")
    print("     Does the app crash immediately with a clear message, or fail downstream?")
    print("     If you are not certain, say so.")
    result = _read_single("q11")
    if result == QUIT_KEYWORD:
        quit_result = _handle_quit(all_answers)
        if quit_result is CONTINUE_SENTINEL:
            pass
        else:
            return quit_result
    else:
        all_answers["q11"] = result

    print("\n" + "="*60)
    print("Batch A complete. Moving to Batch B: Architecture.")
    print("="*60)
    _print_controls()

    # Q12
    print("Q12. Paste the output of `tree` or equivalent from your project root.")
    print("     Windows: tree /F")
    print("     Linux/Mac: find . -not -path '*/.*' | sort")
    result = _read_multiline("q12")
    if result == QUIT_KEYWORD:
        quit_result = _handle_quit(all_answers)
        if quit_result is CONTINUE_SENTINEL:
            pass
        else:
            return quit_result
    else:
        all_answers["q12"] = result

    # Q13
    print("\nQ13. For each folder in that tree, write its single responsibility in one sentence.")
    result = _read_multiline("q13")
    if result == QUIT_KEYWORD:
        quit_result = _handle_quit(all_answers)
        if quit_result is CONTINUE_SENTINEL:
            pass
        else:
            return quit_result
    else:
        all_answers["q13"] = result

    # Q14
    print("\nQ14. Starting from the moment a user triggers the primary action —")
    print("     name every function, module, or service that executes, in exact order.")
    print("     Include every database query. Format as a numbered list.")
    result = _read_multiline("q14")
    if result == QUIT_KEYWORD:
        quit_result = _handle_quit(all_answers)
        if quit_result is CONTINUE_SENTINEL:
            pass
        else:
            return quit_result
    else:
        all_answers["q14"] = result

    # Q15
    print("\nQ15. How do the major components communicate?")
    print("     (function calls, HTTP, serial port, message queue, shared DB, events, other)")
    result = _read_single("q15")
    if result == QUIT_KEYWORD:
        quit_result = _handle_quit(all_answers)
        if quit_result is CONTINUE_SENTINEL:
            pass
        else:
            return quit_result
    else:
        all_answers["q15"] = result

    # Q16
    print("\nQ16. What are the non-obvious design decisions in this project?")
    print("     Things that look strange but were deliberate — and why.")
    result = _read_multiline("q16")
    if result == QUIT_KEYWORD:
        quit_result = _handle_quit(all_answers)
        if quit_result is CONTINUE_SENTINEL:
            pass
        else:
            return quit_result
    else:
        all_answers["q16"] = result

    print("\nPhase 2 complete.")
    return all_answers

def run_phase_three(all_answers: dict):
    print("\n" + "="*60)
    print("PHASE 3 — Completion Layer")
    print("Group A: Security")
    print("="*60)
    _print_controls()

    # Q17
    print("Q17. What sensitive data does this project handle?")
    print("     (passwords, tokens, PII, financial data, session state)")
    result = _read_single("q17")
    if result == QUIT_KEYWORD:
        quit_result = _handle_quit(all_answers)
        if quit_result is CONTINUE_SENTINEL:
            pass
        else:
            return quit_result
    else:
        all_answers["q17"] = result

    # Q18
    print("\nQ18. Describe your authentication and authorisation model.")
    print("     Who can do what, and how is it enforced in code?")
    result = _read_single("q18")
    if result == QUIT_KEYWORD:
        quit_result = _handle_quit(all_answers)
        if quit_result is CONTINUE_SENTINEL:
            pass
        else:
            return quit_result
    else:
        all_answers["q18"] = result

    # Q19
    print("\nQ19. What is the network exposure?")
    print("     (local only / LAN / internet-facing / behind auth proxy)")
    result = _read_single("q19")
    if result == QUIT_KEYWORD:
        quit_result = _handle_quit(all_answers)
        if quit_result is CONTINUE_SENTINEL:
            pass
        else:
            return quit_result
    else:
        all_answers["q19"] = result

    # Q20
    print("\nQ20. Paste your .gitignore file in full.")
    result = _read_multiline("q20")
    if result == QUIT_KEYWORD:
        quit_result = _handle_quit(all_answers)
        if quit_result is CONTINUE_SENTINEL:
            pass
        else:
            return quit_result
    else:
        all_answers["q20"] = result

    # Q21
    print("\nQ21. Run the dependency audit for your stack and paste the output.")
    print("     Python:  pip install pip-audit && pip-audit")
    print("     Node:    npm audit")
    print("     Rust:    cargo audit")
    print("     If skipping, type SKIP — a warning block will be added to the README.")
    lines = []
    while True:
        line = input()
        if line.strip().upper() == "END":
            all_answers["q21_skipped"] = False
            break
        if line.strip().upper() in (SKIP_KEYWORD, TLDR_KEYWORD):
            print("  → Skipped. Warning block will be added to the README.")
            all_answers["q21_skipped"] = True
            all_answers["q21"] = GENERIC_ANSWERS["q21"]
            break
        if line.strip().upper() == QUIT_KEYWORD:
            quit_result = _handle_quit(all_answers)
            if quit_result is CONTINUE_SENTINEL:
                break
            else:
                return quit_result
        lines.append(line)
    if not all_answers.get("q21"):
        all_answers["q21"] = "\n".join(lines).strip()

    # Q22
    print("\nQ22. What are the known security limitations or assumptions a deployer must understand?")
    result = _read_multiline("q22")
    if result == QUIT_KEYWORD:
        quit_result = _handle_quit(all_answers)
        if quit_result is CONTINUE_SENTINEL:
            pass
        else:
            return quit_result
    else:
        all_answers["q22"] = result

    print("\n" + "="*60)
    print("Group B: Deployment")
    print("="*60)
    _print_controls()

    # Q23
    print("Q23. What is the deployment target?")
    print("     (local only / VPS / cloud VM / container / managed service / embedded / other)")
    result = _read_single("q23")
    if result == QUIT_KEYWORD:
        quit_result = _handle_quit(all_answers)
        if quit_result is CONTINUE_SENTINEL:
            pass
        else:
            return quit_result
    else:
        all_answers["q23"] = result

    # Q24
    print("\nQ24. Is this containerised?")
    print("     If yes, paste your Dockerfile or docker-compose.yml.")
    print("     If no, describe every difference between local dev and production.")
    result = _read_multiline("q24")
    if result == QUIT_KEYWORD:
        quit_result = _handle_quit(all_answers)
        if quit_result is CONTINUE_SENTINEL:
            pass
        else:
            return quit_result
    else:
        all_answers["q24"] = result

    # Q25
    print("\nQ25. Are there any production-specific setup steps that differ from Phase 1?")
    result = _read_single("q25")
    if result == QUIT_KEYWORD:
        quit_result = _handle_quit(all_answers)
        if quit_result is CONTINUE_SENTINEL:
            pass
        else:
            return quit_result
    else:
        all_answers["q25"] = result

    print("\n" + "="*60)
    print("Group C: Changelog and Maintenance")
    print("="*60)
    _print_controls()

    # Q26
    print("Q26. Run `git log --oneline -20` and paste the full output.")
    result = _read_multiline("q26")
    if result == QUIT_KEYWORD:
        quit_result = _handle_quit(all_answers)
        if quit_result is CONTINUE_SENTINEL:
            pass
        else:
            return quit_result
    else:
        all_answers["q26"] = result

    # Q27
    print("\nQ27. Is this project open to contributions?")
    print("     If yes: branching strategy, PR process, linter/style config.")
    result = _read_multiline("q27")
    if result == QUIT_KEYWORD:
        quit_result = _handle_quit(all_answers)
        if quit_result is CONTINUE_SENTINEL:
            pass
        else:
            return quit_result
    else:
        all_answers["q27"] = result

    # Q28
    print("\nQ28. How should bugs be reported and features requested?")
    result = _read_single("q28")
    if result == QUIT_KEYWORD:
        quit_result = _handle_quit(all_answers)
        if quit_result is CONTINUE_SENTINEL:
            pass
        else:
            return quit_result
    else:
        all_answers["q28"] = result

    # Q29
    print("\nQ29. Who maintains this project and how can they be reached?")
    result = _read_single("q29")
    if result == QUIT_KEYWORD:
        quit_result = _handle_quit(all_answers)
        if quit_result is CONTINUE_SENTINEL:
            pass
        else:
            return quit_result
    else:
        all_answers["q29"] = result

    # Q30
    print("\nQ30. What license applies?")
    print("     List any third-party code or assets requiring attribution.")
    result = _read_single("q30")
    if result == QUIT_KEYWORD:
        quit_result = _handle_quit(all_answers)
        if quit_result is CONTINUE_SENTINEL:
            pass
        else:
            return quit_result
    else:
        all_answers["q30"] = result

    print("\nPhase 3 complete.")
    return all_answers

def _ask_layer_prompt() -> str:
    print("\nYour README draft is ready and publishable as-is.")
    print("\nTwo optional depth layers are available:")
    print("  Layer 2 — usage guide, configuration reference, architecture")
    print("  Layer 3 — security, deployment, changelog, contributing guide")
    print("\nType 'more' for both, 'layer 2', 'layer 3', or 'done' to finish.")
    response = input("> ").strip().lower()
    return response


def _parse_layer_intent(response: str) -> list[str]:
    depth_keywords = ["more", "both", "everything", "all", "complete", "full"]
    layer2_keywords = ["layer 2", "usage", "architecture", "config", "depth"]
    layer3_keywords = ["layer 3", "security", "deploy", "changelog", "contributing"]

    layers = []
    if any(k in response for k in depth_keywords):
        layers = ["layer2", "layer3"]
    else:
        if any(k in response for k in layer2_keywords):
            layers.append("layer2")
        if any(k in response for k in layer3_keywords):
            layers.append("layer3")

    return layers


def run_interview() -> dict:
    all_answers = {}

    result = run_phase_one(all_answers)
    if result is CONTINUE_SENTINEL or result is None:
        return all_answers
    all_answers = result

    response = _ask_layer_prompt()

    if response.strip().lower() == "done":
        return all_answers

    layers = _parse_layer_intent(response)

    if not layers:
        print("Intent unclear. Do you want to add more depth to the README, or is the draft sufficient?")
        clarification = input("> ").strip().lower()
        if clarification == "done" or "no" in clarification or "sufficient" in clarification:
            return all_answers
        elif "yes" in clarification or "more" in clarification or "depth" in clarification:
            layers = ["layer2", "layer3"]
        else:
            return all_answers

    if "layer2" in layers:
        result = run_phase_two(all_answers)
        if result is CONTINUE_SENTINEL or result is None:
            return all_answers
        all_answers = result

        response = _ask_layer_prompt()
        if response.strip().lower() == "done":
            return all_answers

        new_layers = _parse_layer_intent(response)
        if "layer3" in new_layers:
            layers.append("layer3")

    if "layer3" in layers:
        result = run_phase_three(all_answers)
        if result is CONTINUE_SENTINEL or result is None:
            return all_answers
        all_answers = result

    return all_answers

def format_answers(answers: dict) -> str:
    labels = {
        "q1": "Q1. Project description, target user, and problem solved",
        "q2": "Q2. Full tech stack",
        "q3": "Q3. Terminal session — clean setup to running app",
        "q4": "Q4. Successful run output",
        "q5": "Q5. Three common setup errors and fixes",
        "q6": "Q6. Major features",
        "q7": "Q7. Primary workflow",
        "q8": "Q8. User roles and modes",
        "q9": "Q9. Configuration options",
        "q9b": "Q9b. Config loading mechanism",
        "q10": "Q10. Sensitive config values and storage",
        "q11": "Q11. Behaviour on missing required config",
        "q12": "Q12. Project file tree",
        "q13": "Q13. Folder responsibilities",
        "q14": "Q14. Critical execution path",
        "q15": "Q15. Component communication model",
        "q16": "Q16. Non-obvious design decisions",
        "q17": "Q17. Sensitive data handled",
        "q18": "Q18. Auth model",
        "q19": "Q19. Network exposure",
        "q20": "Q20. .gitignore contents",
        "q21": "Q21. Dependency audit output",
        "q22": "Q22. Known security limitations",
        "q23": "Q23. Deployment target",
        "q24": "Q24. Containerisation and env differences",
        "q25": "Q25. Production-specific setup steps",
        "q26": "Q26. Git log",
        "q27": "Q27. Contribution guidelines",
        "q28": "Q28. Bug reporting and feature requests",
        "q29": "Q29. Maintainer contact",
        "q30": "Q30. License and attribution",
    }

    lines = ["=== DEVELOPER INTERVIEW ANSWERS ===\n"]
    for key, label in labels.items():
        if key in answers and key != "q21_skipped":
            lines.append(f"[{label}]")
            lines.append(answers[key] or "(not provided)")
            lines.append("")

    if answers.get("q21_skipped"):
        lines.append("[Q21. Dependency audit]")
        lines.append("SKIPPED — insert warning block in Security section.")
        lines.append("")

    return "\n".join(lines)
