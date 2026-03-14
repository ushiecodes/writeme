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

    print("Phase 1 complete. Sending to Gemini...")


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

    print("Phase 2 complete.")


    return answers
    

def run_phase_three() -> dict:
    
    answers = {}
    
    print("PHASE 3 — Completion Layer")
    print("Group A: Security")
    
        # Q17
    print("Q17. What sensitive data does this project handle?")
    print("     (passwords, tokens, PII, financial data, session state)")
    answers["q17"] = input("> ").strip()

    # Q18
    print("\nQ18. Describe your authentication and authorisation model.")
    print("     Who can do what, and how is it enforced in code?")
    answers["q18"] = input("> ").strip()

    # Q19
    print("\nQ19. What is the network exposure?")
    print("     (local only / LAN / internet-facing / behind auth proxy)")
    answers["q19"] = input("> ").strip()

    # Q20
    print("\nQ20. Paste your .gitignore file in full.")
    print("     Type END on a new line when done:")
    lines = []
    while True:
        line = input()
        if line.strip().upper() == "END":
            break
        lines.append(line)
    answers["q20"] = "\n".join(lines).strip()

    # Q21
    print("\nQ21. Run the dependency audit for your stack and paste the output.")
    print("     Python:  pip install pip-audit && pip-audit")
    print("     Node:    npm audit")
    print("     Rust:    cargo audit")
    print("     If skipping, type SKIP — a warning block will be added to the README.")
    lines = []
    while True:
        line = input()
        if line.strip().upper() in ("END", "SKIP"):
            answers["q21_skipped"] = line.strip().upper() == "SKIP"
            break
        lines.append(line)
    answers["q21"] = "\n".join(lines).strip()

    # Q22
    print("\nQ22. What are the known security limitations or assumptions a deployer must understand?")
    print("     Type END on a new line when done:")
    lines = []
    while True:
        line = input()
        if line.strip().upper() == "END":
            break
        lines.append(line)
    answers["q22"] = "\n".join(lines).strip()

    print("\n" + "="*60)
    print("Group B: Deployment")
    print("="*60 + "\n")

    # Q23
    print("Q23. What is the deployment target?")
    print("     (local only / VPS / cloud VM / container / managed service / embedded / other)")
    answers["q23"] = input("> ").strip()

    # Q24
    print("\nQ24. Is this containerised?")
    print("     If yes, paste your Dockerfile or docker-compose.yml.")
    print("     If no, describe every difference between local dev and production.")
    print("     Type END on a new line when done:")
    lines = []
    while True:
        line = input()
        if line.strip().upper() == "END":
            break
        lines.append(line)
    answers["q24"] = "\n".join(lines).strip()

    # Q25
    print("\nQ25. Are there any production-specific setup steps that differ from Phase 1?")
    answers["q25"] = input("> ").strip()

    print("\n" + "="*60)
    print("Group C: Changelog and Maintenance")
    print("="*60 + "\n")

    # Q26
    print("Q26. Run `git log --oneline -20` and paste the full output.")
    print("     Type END on a new line when done:")
    lines = []
    while True:
        line = input()
        if line.strip().upper() == "END":
            break
        lines.append(line)
    answers["q26"] = "\n".join(lines).strip()

    # Q27
    print("\nQ27. Is this project open to contributions?")
    print("     If yes: branching strategy, PR process, linter/style config.")
    print("     Type END on a new line when done:")
    lines = []
    while True:
        line = input()
        if line.strip().upper() == "END":
            break
        lines.append(line)
    answers["q27"] = "\n".join(lines).strip()

    # Q28
    print("\nQ28. How should bugs be reported and features requested?")
    answers["q28"] = input("> ").strip()

    # Q29
    print("\nQ29. Who maintains this project and how can they be reached?")
    answers["q29"] = input("> ").strip()

    # Q30
    print("\nQ30. What license applies?")
    print("     List any third-party code or assets requiring attribution.")
    answers["q30"] = input("> ").strip()

    print("Phase 3 complete.")

    return answers
    
    
def _ask_layer_prompt() -> str:
    
    print("\nYour README draft is ready and publishable as-is.")
    print("\nTwo optional depth layers are available:")
    print("  Layer 2 — usage guide, configuration reference, architecture")
    print("  Layer 3 — security, deployment, changelog, contributing guide")
    print("\nType 'more' for both, 'layer 2', 'layer 3', or 'done' to finish.")
    response = input("> ").strip().lower()
    return response
    
def _parse_layer_intent(response: str) -> list[str]:
    depth_keywords = ["more", "both", "everything", "all", "complete ", "full"]
    layer2_keywords = ["layer 2", "usage", "architecture", "config", "depth"]
    layer3_keywords = ["layer 3", "security", "depl", "changelog", "contributing"]
    
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
    
    phase1 = run_phase_one()
    all_answers.update(phase1)
    
    response = _ask_layer_prompt()
    
    if response == "done":
        return all_answers

    layers = _parse_layer_intent(response)
    
    if not layers:
        print("Intent unclear. Do you want to add more depth to the README? or is the draft SUFFICIENT?")
        clarification = input("> ").strip().lower()
        
        if "yes" in clarification or "more" in clarification or "depth" in clarification:
            layers = ["layer2", "layer3"]
        else:
            return all_answers
    
    if "layer2" in layers:
        phase2 = run_phase_two()
        all_answers.update(phase2)
        response = _ask_layer_prompt()
        
        if response != "done":
            new_layers = _parse_layer_intent(response)
            if "layer3" in new_layers:
                layers.append("layer3")

    if "layer3" in layers:
        phase3 = run_phase_three()
        all_answers.update(phase3)
    
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
        "q30": "Q30. License and attribution"
    }

    lines = ["DEVELOPER INTERVIEW ANSWERS\n"]
    for key, label in labels.items():
        if key in answers and key != "q21_skipped":
            lines.append(f"[{label}]")
            lines.append(answers[key] or "(not provided)")
            lines.append("")
            
    if answers.get("q21_skipped"):
        lines.append("[Q21. Dependency Audit]")
        lines.append("SKIPPED - Insert warning block in security section")
        lines.append("")
    
    return "\n".join(lines)
