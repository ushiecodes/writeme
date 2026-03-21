from display import (
    console,
    print_phase_header,
    print_controls,
    print_question,
    print_rtfm,
    print_layer_prompt,
    print_success,
    print_warning,
    print_info,
)

SKIP_KEYWORD = "SKIP"
QUIT_KEYWORD = "QUIT"
TLDR_KEYWORD = "TLDR"
RTFM_KEYWORD = "RTFM"

# ---------------------------------------------------------------------------
# GENERIC ANSWERS
# ---------------------------------------------------------------------------

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

# ---------------------------------------------------------------------------
# FORMAT LABELS
# Used by format_answers() to label each answer for Gemini
# ---------------------------------------------------------------------------

ANSWER_LABELS = {
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

# ---------------------------------------------------------------------------
# SENTINEL
# ---------------------------------------------------------------------------

CONTINUE_SENTINEL = object()
QUIT_SENTINEL = object()
# ---------------------------------------------------------------------------
# QUESTION BANK
# Each question is a dict with these fields:
#   key        — answer dict key, matches GENERIC_ANSWERS and ANSWER_LABELS
#   phase      — human-readable label shown in audit/debug output
#   text       — the question text printed to the user
#   hints      — list of additional lines printed below the question text
#   multiline  — True = END-terminated block, False = single line
#   required   — True = SKIP/TLDR not accepted, user must answer
# ---------------------------------------------------------------------------

PHASE_1_QUESTIONS = [
    {
        "key": "q1",
        "phase": "Phase 1 — Publishable Draft",
        "text": "Q1. What does this project do, who is it for, and what problem does it solve?",
        "hints": [],
        "multiline": False,
        "required": False,
        "rtfm": (
            "Answer three things in any order:\n"
            "  1. What the project does (one sentence)\n"
            "  2. Who it is for (the target user)\n"
            "  3. What problem it solves\n\n"
            "Example:\n"
            "  'WriteMe is a CLI tool for developers who hate writing README files.\n"
            "   It interviews you about your project and uses Gemini AI to generate\n"
            "   a complete README.md automatically.'"
        ),
    },
    {
        "key": "q2",
        "phase": "Phase 1 — Publishable Draft",
        "text": "Q2. What is the full tech stack?",
        "hints": [
            "  - Language and version",
            "  - Database, if any",
            "  - Hardware, if any",
            "  - Operating system(s) it runs on",
            "  - Package manager used",
        ],
        "multiline": True,
        "required": False,
        "rtfm": (
            "List every technology your project uses to run.\n\n"
            "Example:\n"
            "  Language: Python 3.12\n"
            "  Database: PostgreSQL 15\n"
            "  Hardware: none\n"
            "  OS: Windows, Linux, macOS\n"
            "  Package manager: uv\n\n"
            "If you have no database or hardware, just say 'none'."
        ),
    },
    {
        "key": "q3",
        "phase": "Phase 1 — Publishable Draft",
        "text": "Q3. Paste your exact terminal session from a clean setup to a running app.",
        "hints": [
            "    If mid-build, list commands in order and mark uncertain steps with [?]",
        ],
        "multiline": True,
        "required": False,
        "rtfm": (
            "Open a fresh terminal and run your project from scratch. Paste everything.\n\n"
            "Example:\n"
            "  $ git clone https://github.com/yourname/project.git\n"
            "  $ cd project\n"
            "  $ uv sync\n"
            "  $ uv run cli.py\n"
            "  Welcome to MyProject...\n\n"
            "If a step is uncertain, mark it:\n"
            "  $ pip install special-dep  [?]\n\n"
            "Type END when done."
        ),
    },
    {
        "key": "q4",
        "phase": "Phase 1 — Publishable Draft",
        "text": "Q4. What does a fully successful run look like?",
        "hints": [
            "    Paste the terminal output or describe exactly what the user sees:",
        ],
        "multiline": True,
        "required": False,
        "rtfm": (
            "Describe or paste exactly what a user sees when everything works.\n\n"
            "Example:\n"
            "  Welcome to WriteMe — AI-powered README generator\n"
            "  ============================================================\n"
            "  Q1. What does this project do?\n"
            "  > ...\n"
            "  Scanning codebase...\n"
            "  Generating README...\n"
            "  README.md created.\n"
            "  Done. Your README is ready.\n\n"
            "Type END when done."
        ),
    },
    {
        "key": "q5",
        "phase": "Phase 1 — Publishable Draft",
        "text": "Q5. What are the 3 errors people most commonly hit during setup?",
        "hints": [
            "    For each: paste the exact error message and the exact fix.",
        ],
        "multiline": True,
        "required": False,
        "rtfm": (
            "Think about the last 3 times someone (or you) had trouble setting this up.\n\n"
            "Format each error like this:\n\n"
            "  Error 1:\n"
            "  ModuleNotFoundError: No module named 'google'\n"
            "  Fix: Run `uv sync` to install all dependencies.\n\n"
            "  Error 2:\n"
            "  429 RESOURCE_EXHAUSTED\n"
            "  Fix: Your API quota is exhausted. Wait until midnight or use a new key.\n\n"
            "Type END when done."
        ),
    },
]

PHASE_2A_QUESTIONS = [
    {
        "key": "q6",
        "phase": "Phase 2 — Batch A: Usage and Configuration",
        "text": "Q6. List every major feature with a one-line description of what it does.",
        "hints": [],
        "multiline": True,
        "required": False,
        "rtfm": (
            "List each feature on its own line with a one-line description.\n\n"
            "Example:\n"
            "  Progressive interview — asks questions in 3 phases to capture project context\n"
            "  Codebase scanner — reads source files and sends them to the AI\n"
            "  Collision detection — asks before overwriting an existing README.md\n"
            "  --reset flag — clears saved API key so user can rotate credentials\n\n"
            "Type END when done."
        ),
    },
    {
        "key": "q7",
        "phase": "Phase 2 — Batch A: Usage and Configuration",
        "text": "Q7. Walk me through the primary workflow — from launch to first result.",
        "hints": [
            "    What does the user see, type, and receive at each step?",
        ],
        "multiline": True,
        "required": False,
        "rtfm": (
            "Walk through the exact sequence a user follows.\n\n"
            "Example:\n"
            "  1. User runs `writeme` in their project directory\n"
            "  2. Tool prompts for Gemini API key on first run\n"
            "  3. Phase 1 interview begins — 5 questions\n"
            "  4. User chooses depth layers\n"
            "  5. Tool scans codebase\n"
            "  6. README is generated and written to disk\n\n"
            "Type END when done."
        ),
    },
    {
        "key": "q8",
        "phase": "Phase 2 — Batch A: Usage and Configuration",
        "text": "Q8. Are there different user roles, modes, or permission levels?",
        "hints": [
            "    If yes, what can each do? If no, just say 'none'.",
        ],
        "multiline": False,
        "required": False,
        "rtfm": (
            "Does your app have different types of users with different access levels?\n\n"
            "Examples:\n"
            "  'Admin can delete users, regular user can only read'\n"
            "  'Guest mode is read-only, logged-in users can post'\n"
            "  'none' — if everyone has the same access\n\n"
            "Most CLI tools just say 'none'."
        ),
    },
    {
        "key": "q9",
        "phase": "Phase 2 — Batch A: Usage and Configuration",
        "text": "Q9. List every configuration option in this format:",
        "hints": [
            "    VARIABLE_NAME | what it controls | default value | valid values | required?",
            "    One line per variable.",
        ],
        "multiline": True,
        "required": False,
        "rtfm": (
            "List every environment variable or config option your app reads.\n\n"
            "Format: VARIABLE_NAME | purpose | default | valid values | required?\n\n"
            "Example:\n"
            "  API_KEY | Gemini API key | none | any valid key string | required\n"
            "  MODEL | Gemini model to use | gemini-2.5-flash | any model name | optional\n"
            "  MAX_FILE_SIZE_KB | max file size to scan | 50 | any positive integer | optional\n\n"
            "Type END when done."
        ),
    },
    {
        "key": "q9b",
        "phase": "Phase 2 — Batch A: Usage and Configuration",
        "text": "Q9b. How does the app load these variables? Check all that apply:",
        "hints": [
            "  - .env file read by a library (e.g. python-dotenv)",
            "  - Shell environment variables set before launch",
            "  - Config file (.yaml, .toml, .json, .ini)",
            "  - Cloud secrets manager",
            "  - Hardcoded defaults with env override",
            "  - Other — describe",
        ],
        "multiline": True,
        "required": False,
        "rtfm": (
            "This tells users HOW to set their config values.\n\n"
            "Examples:\n"
            "  '.env file via python-dotenv' → user creates a .env file\n"
            "  'Shell env vars' → user runs export API_KEY=abc before launching\n"
            "  'Config JSON at ~/.config/app/config.json' → app stores it automatically\n\n"
            "Pick all that apply and describe if using multiple."
            "Type END when done."
        ),
    },
    {
        "key": "q10",
        "phase": "Phase 2 — Batch A: Usage and Configuration",
        "text": "Q10. Which config values are sensitive (passwords, tokens, API keys)?",
        "hints": [
            "     Where are they stored and how are they protected?",
        ],
        "multiline": False,
        "required": False,
        "rtfm": (
            "Name every variable that would cause harm if committed to git.\n\n"
            "Example:\n"
            "  'API_KEY is sensitive. Stored in ~/.config/writeme/config.json.\n"
            "   Protected by OS file permissions. Never written to project directory.\n"
            "   .gitignore prevents .env.local from being committed.'"
        ),
    },
    {
        "key": "q11",
        "phase": "Phase 2 — Batch A: Usage and Configuration",
        "text": "Q11. What happens if a required config value is missing?",
        "hints": [
            "     Does the app crash immediately with a clear message, or fail downstream?",
            "     If you are not certain, say so.",
        ],
        "multiline": False,
        "required": False,
        "rtfm": (
            "Name every variable that would cause harm if committed to git.\n\n"
            "Example:\n"
            "  'API_KEY is sensitive. Stored in ~/.config/writeme/config.json.\n"
            "   Protected by OS file permissions. Never written to project directory.\n"
            "   .gitignore prevents .env.local from being committed.'"
        ),
    },
]

PHASE_2B_QUESTIONS = [
    {
        "key": "q12",
        "phase": "Phase 2 — Batch B: Architecture",
        "text": "Q12. Paste the output of `tree` or equivalent from your project root.",
        "hints": [
            "     Windows: tree /F",
            "     Linux/Mac: find . -not -path '*/.*' | sort",
        ],
        "multiline": True,
        "required": False,
        "rtfm": (
            "Run this command in your terminal and paste the output here.\n\n"
            "Windows:\n"
            "  tree /F\n\n"
            "Linux/Mac:\n"
            "  find . -not -path '*/.*' | sort\n\n"
            "Expected output looks like:\n"
            "  .\n"
            "  ./cli.py\n"
            "  ./config.py\n"
            "  ./gemini.py\n"
            "  ./pyproject.toml\n\n"
            "Type END when done."
        ),
    },
    {
        "key": "q13",
        "phase": "Phase 2 — Batch B: Architecture",
        "text": "Q13. For each folder in that tree, write its single responsibility in one sentence.",
        "hints": [],
        "multiline": True,
        "required": False,
        "rtfm": (
            "For each folder (not file), write what it owns.\n\n"
            "Example:\n"
            "  src/ — all application source code\n"
            "  tests/ — unit and integration tests\n"
            "  docs/ — static documentation files\n"
            "  scripts/ — one-off utility scripts not part of the main app\n\n"
            "If your project has no subfolders, say 'No subdirectories — flat layout'.\n\n"
            "Type END when done."
        ),
    },
    {
        "key": "q14",
        "phase": "Phase 2 — Batch B: Architecture",
        "text": "Q14. Starting from the moment a user triggers the primary action —",
        "hints": [
            "     name every function, module, or service that executes, in exact order.",
            "     Include every database query. Format as a numbered list.",
        ],
        "multiline": True,
        "required": False,
        "rtfm": (
            "Trace exactly what happens when a user does the main thing your app does.\n\n"
            "Example for a CLI tool:\n"
            "  1. User runs `writeme` in terminal\n"
            "  2. cli.main() is called\n"
            "  3. config.get_api_key() loads key from ~/.config/writeme/config.json\n"
            "  4. interview.run_interview() starts the question flow\n"
            "  5. gemini.generate_readme() sends prompt to Gemini API\n"
            "  6. writer.write_readme() writes output to README.md\n\n"
            "Name actual functions — not 'the app processes the request'.\n\n"
            "Type END when done."
        ),
    },
    {
        "key": "q15",
        "phase": "Phase 2 — Batch B: Architecture",
        "text": "Q15. How do the major components communicate?",
        "hints": [
            "     (function calls, HTTP, serial port, message queue, shared DB, events, other)",
        ],
        "multiline": False,
        "required": False,
        "rtfm": (
            "Describe how each part of your system talks to the other parts.\n\n"
            "Examples:\n"
            "  'All modules use direct Python function calls. No HTTP between components.\n"
            "   Only external call is HTTPS to the Gemini API.'\n\n"
            "  'Frontend calls backend via REST API. Backend writes to PostgreSQL.\n"
            "   Background jobs communicate via Redis queue.'"
        ),
    },
    {
        "key": "q16",
        "phase": "Phase 2 — Batch B: Architecture",
        "text": "Q16. What are the non-obvious design decisions in this project?",
        "hints": [
            "     Things that look strange but were deliberate — and why.",
        ],
        "multiline": True,
        "required": False,
        "rtfm": (
            "Think about choices you made that a new contributor might question.\n\n"
            "Example:\n"
            "  'We store the API key in ~/.config instead of .env because users run\n"
            "   this tool across many projects and re-entering the key each time is bad UX.'\n\n"
            "  'We inject the full codebase into the AI prompt instead of summarising it\n"
            "   because summaries cause hallucinations in the generated README.'\n\n"
            "If nothing is non-obvious, say so.\n\n"
            "Type END when done."
        ),
    },
]

PHASE_3A_QUESTIONS = [
    {
        "key": "q17",
        "phase": "Phase 3 — Group A: Security",
        "text": "Q17. What sensitive data does this project handle?",
        "hints": [
            "     (passwords, tokens, PII, financial data, session state)",
        ],
        "multiline": False,
        "required": False,
        "rtfm": (
            "List every type of sensitive data your app touches.\n\n"
            "Examples:\n"
            "  'Gemini API key — stored locally'\n"
            "  'User passwords — hashed with bcrypt'\n"
            "  'Credit card numbers — never stored, passed directly to Stripe'\n"
            "  'None — this app handles no sensitive data'"
        ),
    },
    {
        "key": "q18",
        "phase": "Phase 3 — Group A: Security",
        "text": "Q18. Describe your authentication and authorisation model.",
        "hints": [
            "     Who can do what, and how is it enforced in code?",
        ],
        "multiline": False,
        "required": False,
        "rtfm": (
            "Authentication = proving who you are.\n"
            "Authorisation = what you are allowed to do.\n\n"
            "Examples:\n"
            "  'No auth — local CLI tool, OS controls access'\n"
            "  'JWT tokens — issued on login, verified on every API request'\n"
            "  'API key in header — checked against database on each request'\n\n"
            "If your app has no auth, say 'none — local tool only'."
        ),
    },
    {
        "key": "q19",
        "phase": "Phase 3 — Group A: Security",
        "text": "Q19. What is the network exposure?",
        "hints": [
            "     (local only / LAN / internet-facing / behind auth proxy)",
        ],
        "multiline": False,
        "required": False,
        "rtfm": (
            "Describe what network access your app has or requires.\n\n"
            "Examples:\n"
            "  'Local only — no inbound connections, one outbound HTTPS call to Gemini API'\n"
            "  'Internet-facing — runs on port 8080, behind nginx reverse proxy'\n"
            "  'LAN only — accessible on local network, not exposed to internet'"
        ),
    },
    {
        "key": "q20",
        "phase": "Phase 3 — Group A: Security",
        "text": "Q20. Paste your .gitignore file in full.",
        "hints": [],
        "multiline": True,
        "required": False,
        "rtfm": (
            "Run this and paste the output:\n\n"
            "  cat .gitignore\n\n"
            "If you don't have a .gitignore yet, here is a minimal Python one:\n\n"
            "  __pycache__/\n"
            "  *.py[oc]\n"
            "  .venv\n"
            "  .env\n"
            "  .env.local\n"
            "  dist/\n"
            "  build/\n"
            "  *.egg-info\n\n"
            "Type END when done."
        ),
    },
    {
        "key": "q21",
        "phase": "Phase 3 — Group A: Security",
        "text": "Q21. Run the dependency audit for your stack and paste the output.",
        "hints": [
            "     Python:  pip install pip-audit && pip-audit",
            "     Node:    npm audit",
            "     Rust:    cargo audit",
            "     If skipping, type SKIP — a warning block will be added to the README.",
        ],
        "multiline": True,
        "required": False,
        "skippable_flag": "q21_skipped",
        "rtfm": (
            "A dependency audit checks if any of your installed packages have known\n"
            "security vulnerabilities (CVEs).\n\n"
            "Run the correct command for your stack:\n\n"
            "  Python:  pip install pip-audit && pip-audit\n"
            "  Node:    npm audit\n"
            "  Rust:    cargo audit\n\n"
            "Paste the full output — including any warnings.\n"
            "If you get 'No known vulnerabilities found', paste that.\n"
            "If you cannot run it right now, type SKIP.\n\n"
            "Type END when done."
        ),
    },
    {
        "key": "q22",
        "phase": "Phase 3 — Group A: Security",
        "text": "Q22. What are the known security limitations or assumptions a deployer must understand?",
        "hints": [],
        "multiline": True,
        "required": False,
        "rtfm": (
            "List anything a person deploying this project must know about its security.\n\n"
            "Examples:\n"
            "  'API key stored in plaintext JSON — relies on OS file permissions'\n"
            "  'No rate limiting on the API endpoint — deployer must add their own'\n"
            "  'Assumes database is not internet-accessible'\n"
            "  'Passwords hashed with bcrypt cost factor 10 — may need tuning for production'\n\n"
            "If there are no known limitations, say 'none known'.\n\n"
            "Type END when done."
        ),
    },
]

PHASE_3B_QUESTIONS = [
    {
        "key": "q23",
        "phase": "Phase 3 — Group B: Deployment",
        "text": "Q23. What is the deployment target?",
        "hints": [
            "     (local only / VPS / cloud VM / container / managed service / embedded / other)",
        ],
        "multiline": False,
        "required": False,
        "rtfm": (
            "Where does this project run when it is being used for real?\n\n"
            "Examples:\n"
            "  'Local machine only — developer installs and runs it themselves'\n"
            "  'VPS — deployed to a DigitalOcean droplet running Ubuntu'\n"
            "  'Container — Docker image pushed to AWS ECR, run on ECS'\n"
            "  'Managed service — deployed to Railway via git push'"
        ),
    },
    {
        "key": "q24",
        "phase": "Phase 3 — Group B: Deployment",
        "text": "Q24. Is this containerised?",
        "hints": [
            "     If yes, paste your Dockerfile or docker-compose.yml.",
            "     If no, describe every difference between local dev and production.",
        ],
        "multiline": True,
        "required": False,
        "rtfm": (
            "If containerised, paste your Dockerfile or docker-compose.yml here.\n\n"
            "If not containerised, describe what is different between your laptop\n"
            "and where this runs in production. For example:\n\n"
            "  'Not containerised. No differences — local and production are identical.\n"
            "   Users install via pip and run locally.'\n\n"
            "  'Not containerised. Production uses gunicorn instead of uvicorn.\n"
            "   DATABASE_URL points to RDS instead of localhost.\n"
            "   DEBUG=False in production.'\n\n"
            "Type END when done."
        ),
    },
    {
        "key": "q25",
        "phase": "Phase 3 — Group B: Deployment",
        "text": "Q25. Are there any production-specific setup steps that differ from Phase 1?",
        "hints": [],
        "multiline": False,
        "required": False,
        "rtfm": (
            "Are there extra steps needed when deploying to production that were\n"
            "not in the local setup you described in Phase 1?\n\n"
            "Examples:\n"
            "  'Run database migrations: python manage.py migrate'\n"
            "  'Set environment variables in the hosting dashboard'\n"
            "  'Enable HTTPS via certbot after first deploy'\n"
            "  'none — production setup is identical to local'"
        ),
    },
]

PHASE_3C_QUESTIONS = [
    {
        "key": "q26",
        "phase": "Phase 3 — Group C: Changelog and Maintenance",
        "text": "Q26. Run `git log --oneline -20` and paste the full output.",
        "hints": [],
        "multiline": True,
        "required": False,
        "rtfm": (
            "Run this in your terminal and paste the result:\n\n"
            "  git log --oneline -20\n\n"
            "Expected output looks like:\n"
            "  a1b2c3d feat(cli): add --reset flag\n"
            "  e4f5g6h fix(config): handle missing key gracefully\n"
            "  i7j8k9l feat(scanner): skip sensitive files\n\n"
            "This is used to generate your Changelog section.\n"
            "If you have no commits yet, type SKIP.\n\n"
            "Type END when done."
        ),
    },
    {
        "key": "q27",
        "phase": "Phase 3 — Group C: Changelog and Maintenance",
        "text": "Q27. Is this project open to contributions?",
        "hints": [
            "     If yes: branching strategy, PR process, linter/style config.",
        ],
        "multiline": True,
        "required": False,
        "rtfm": (
            "Tell contributors how to help.\n\n"
            "Example:\n"
            "  Yes, open to contributions.\n"
            "  Branching: fork the repo, create a feature branch from main.\n"
            "  PR process: open a PR against main with a clear description.\n"
            "              One feature or fix per PR.\n"
            "  Code style: PEP8. Run ruff or flake8 before submitting.\n\n"
            "If closed to contributions, just say 'not open to contributions'.\n\n"
            "Type END when done."
        ),
    },
    {
        "key": "q28",
        "phase": "Phase 3 — Group C: Changelog and Maintenance",
        "text": "Q28. How should bugs be reported and features requested?",
        "hints": [],
        "multiline": False,
        "required": False,
        "rtfm": (
            "Tell users where to go when something breaks or they want a new feature.\n\n"
            "Examples:\n"
            "  'GitHub Issues — include error message, OS, Python version, steps to reproduce'\n"
            "  'Email work.you@gmail.com with subject line [BUG] or [FEATURE]'\n"
            "  'Discord server — link: discord.gg/yourserver'"
        ),
    },
    {
        "key": "q29",
        "phase": "Phase 3 — Group C: Changelog and Maintenance",
        "text": "Q29. Who maintains this project and how can they be reached?",
        "hints": [],
        "multiline": False,
        "required": False,
        "rtfm": (
            "Name the maintainer and give at least one contact method.\n\n"
            "Example:\n"
            "  'Utkarsh Kamat — work.utkarshkamat@gmail.com — GitHub: ushiecodes'\n\n"
            "This appears in the License & Credits section of the README."
        ),
    },
    {
        "key": "q30",
        "phase": "Phase 3 — Group C: Changelog and Maintenance",
        "text": "Q30. What license applies?",
        "hints": [
            "     List any third-party code or assets requiring attribution.",
        ],
        "multiline": False,
        "required": False,
        "rtfm": (
            "Common choices:\n"
            "  MIT — permissive, anyone can use, modify, distribute\n"
            "  Apache 2.0 — permissive with patent protection\n"
            "  GPL 3.0 — copyleft, derivative works must also be open source\n\n"
            "Also list any third-party libraries that require attribution.\n\n"
            "Example:\n"
            "  'MIT License. Dependencies: google-genai (Apache 2.0),\n"
            "   python-dotenv (BSD), platformdirs (MIT).'"
        ),
    },
]

# ---------------------------------------------------------------------------
# CORE PRIMITIVES
# ---------------------------------------------------------------------------


def _print_controls():
    print_controls()
    
def _handle_quit(all_answers: dict):
    print("\nAre you sure you want to quit?")
    print("Your current progress will be used to generate a partial README.")
    print("[Y] Quit and generate with current answers")
    print("[N] Continue the questionnaire")
    choice = input("> ").strip().upper()
    if choice == "Y":
        return QUIT_SENTINEL
    return CONTINUE_SENTINEL


def _read_single(prompt_key: str, required: bool = False, rtfm: str = "") -> str:
    while True:
        response = input("> ").strip()

        if not response:
            if required:
                print("  → This question is required. Please provide an answer.")
                continue
            print("  → Empty answer. Using generic answer.")
            return GENERIC_ANSWERS[prompt_key]

        upper = response.upper()

        if upper == RTFM_KEYWORD:
            if rtfm:
                print_rtfm(rtfm)
            else:
                print_info("No additional help available for this question.")
            continue

        if upper == SKIP_KEYWORD:
            if required:
                print("  → This question is required and cannot be skipped.")
                continue
            print("  → Question skipped.")
            return SKIP_KEYWORD

        if upper == TLDR_KEYWORD:
            if required:
                print("  → This question is required and cannot be skipped.")
                continue
            print("  → Using generic answer.")
            return GENERIC_ANSWERS[prompt_key]

        if upper == QUIT_KEYWORD:
            return QUIT_KEYWORD

        return response


def _read_multiline(prompt_key: str, required: bool = False, rtfm: str = "") -> str:
    print(
        "  (Type END on a new line to submit, SKIP to skip, RTFM for help, QUIT to exit)"
    )
    while True:
        lines = []
        while True:
            line = input()
            upper = line.strip().upper()

            if upper == "END":
                break

            if upper == RTFM_KEYWORD:
                if rtfm:
                    print("\n" + "─" * 60)
                    print(rtfm)
                    print("─" * 60 + "\n")
                    print("  (Continue typing your answer, or type END to submit)")
                else:
                    print("  → No additional help available for this question.")
                continue  # do not add RTFM to lines, keep collecting

            if upper == SKIP_KEYWORD:
                if required:
                    print("  → This question is required and cannot be skipped.")
                    lines = []
                    break
                print("  → Question skipped.")
                return SKIP_KEYWORD

            if upper == TLDR_KEYWORD:
                if required:
                    print("  → This question is required and cannot be skipped.")
                    lines = []
                    break
                print("  → Using generic answer.")
                return GENERIC_ANSWERS[prompt_key]

            if upper == QUIT_KEYWORD:
                return QUIT_KEYWORD

            lines.append(line)

        result = "\n".join(lines).strip()

        if not result:
            if required:
                print("  → This question is required. Please provide an answer.")
                print("  (Type END on a new line to submit)")
                continue
            print("  → Empty answer. Using generic answer.")
            return GENERIC_ANSWERS[prompt_key]

        return result


# ---------------------------------------------------------------------------
# GENERIC QUESTION RUNNER
# Iterates over a question list and collects answers into all_answers.
# Returns all_answers on success.
# Returns None if the user quit with Y.
# ---------------------------------------------------------------------------


def _run_questions(questions: list, all_answers: dict):
    for q in questions:
        while True:
            print(f"\n{q['text']}")
            for hint in q.get("hints", []):
                print(hint)

            required = q.get("required", False)
            rtfm = q.get("rtfm", "")

            if q["multiline"]:
                result = _read_multiline(q["key"], required=required, rtfm=rtfm)
            else:
                result = _read_single(q["key"], required=required, rtfm=rtfm)

            if result == QUIT_KEYWORD:
                quit_result = _handle_quit(all_answers)
                if quit_result is CONTINUE_SENTINEL:
                    continue
                if quit_result is QUIT_SENTINEL:
                    return QUIT_SENTINEL  # propagate up cleanly
            
            if result == SKIP_KEYWORD:
                if "skippable_flag" in q:
                    all_answers[q["skippable_flag"]] = True
                break

            if "skippable_flag" in q:
                all_answers[q["skippable_flag"]] = (result == GENERIC_ANSWERS[q["key"]])

            all_answers[q["key"]] = result
            break

    return all_answers


# ---------------------------------------------------------------------------
# PHASE RUNNERS
# ---------------------------------------------------------------------------


def run_phase_one(all_answers: dict):
    print_phase_header("PHASE 1 — Publishable Draft")
    _print_controls()
    result = _run_questions(PHASE_1_QUESTIONS, all_answers)
    if result is QUIT_SENTINEL:
        return QUIT_SENTINEL
    print_success("Phase 1 complete.")
    return all_answers


def run_phase_two(all_answers: dict):
    print_phase_header("PHASE 2 — Depth Layer")
    _print_controls()

    result = _run_questions(PHASE_2A_QUESTIONS, all_answers)
    if result is QUIT_SENTINEL:
        return QUIT_SENTINEL

    print_phase_header("Batch A complete. Moving to Batch B: Architecture.")
    _print_controls()

    result = _run_questions(PHASE_2B_QUESTIONS, all_answers)
    if result is QUIT_SENTINEL:
        return QUIT_SENTINEL

    print_success("Phase 2 complete.")
    return all_answers


def run_phase_three(all_answers: dict):
    print_phase_header("PHASE 3 — Completion Layer")
    _print_controls()

    result = _run_questions(PHASE_3A_QUESTIONS, all_answers)
    if result is QUIT_SENTINEL:
        return QUIT_SENTINEL

    print_phase_header("Group B: Deployment")
    _print_controls()

    result = _run_questions(PHASE_3B_QUESTIONS, all_answers)
    if result is QUIT_SENTINEL:
        return QUIT_SENTINEL

    print_phase_header("Group C: Changelog and Maintenance")
    _print_controls()

    result = _run_questions(PHASE_3C_QUESTIONS, all_answers)
    if result is QUIT_SENTINEL:
        return QUIT_SENTINEL

    print_success("Phase 3 complete.")
    return all_answers


# ---------------------------------------------------------------------------
# LAYER PROMPT
# ---------------------------------------------------------------------------


def _ask_layer_prompt() -> str:
    print("\nYour README draft is ready and publishable as-is.")
    print("\nTwo optional depth layers are available:")
    print("  Layer 2 — usage guide, configuration reference, architecture")
    print("  Layer 3 — security, deployment, changelog, contributing guide")
    print("\nType 'more' for both, 'layer 2', 'layer 3', or 'done' to finish.")
    return input("> ").strip().lower()


def _parse_layer_intent(response: str) -> list:
    depth_keywords = [
        "more",
        "both",
        "everything",
        "all layers",
        "complete both",
        "full",
    ]
    layer2_keywords = ["layer 2", "usage", "architecture", "config", "depth"]
    layer3_keywords = ["layer 3", "security", "deploy", "changelog", "contributing"]

    if any(k in response for k in depth_keywords):
        return ["layer2", "layer3"]

    layers = []
    if any(k in response for k in layer2_keywords):
        layers.append("layer2")
    if any(k in response for k in layer3_keywords):
        layers.append("layer3")
    return layers


# ---------------------------------------------------------------------------
# INTERVIEW CONTROLLER
# ---------------------------------------------------------------------------


def run_interview() -> dict | None:
    all_answers = {}

    result = run_phase_one(all_answers)
    if result is QUIT_SENTINEL:
        return None  # user quit — signal to caller to cancel generation
    all_answers = result

    response = _ask_layer_prompt()

    if response == "done":
        return all_answers

    layers = _parse_layer_intent(response)

    if not layers:
        print_info("Intent unclear. Do you want to add more depth, or is the draft sufficient?")
        clarification = console.input("[bold cyan]>[/bold cyan] ").strip().lower()
        if clarification == "done" or "no" in clarification or "sufficient" in clarification:
            return all_answers
        elif "yes" in clarification or "more" in clarification or "depth" in clarification:
            layers = ["layer2", "layer3"]
        else:
            return all_answers

    if "layer2" in layers:
        result = run_phase_two(all_answers)
        if result is QUIT_SENTINEL:
            return None
        all_answers = result

        if "layer3" not in layers:
            response = _ask_layer_prompt()
            if response == "done":
                return all_answers
            new_layers = _parse_layer_intent(response)
            if "layer3" in new_layers:
                layers.append("layer3")

    if "layer3" in layers:
        result = run_phase_three(all_answers)
        if result is QUIT_SENTINEL:
            return None
        all_answers = result

    return all_answers


# ---------------------------------------------------------------------------
# FORMAT ANSWERS
# Converts the answers dict into a labeled string for Gemini
# ---------------------------------------------------------------------------


def format_answers(answers: dict) -> str:
    lines = ["=== DEVELOPER INTERVIEW ANSWERS ===\n"]

    for key, label in ANSWER_LABELS.items():
        if key in answers and key != "q21_skipped":
            lines.append(f"[{label}]")
            lines.append(answers[key] or "(not provided)")
            lines.append("")

    if answers.get("q21_skipped"):
        lines.append("[Q21. Dependency audit]")
        lines.append("SKIPPED — insert warning block in Security section.")
        lines.append("")

    return "\n".join(lines)
