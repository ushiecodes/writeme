# WriteMe — AI-powered README generator

> WriteMe is an AI-powered CLI tool for developers who want to generate complete, production-grade README files without spending time writing them manually. It solves the problem of projects shipping with poor or missing documentation by interviewing the developer about their project, scanning the codebase, and using Google Gemini to generate a comprehensive README.md automatically.

![Version](https://img.shields.io/badge/version-0.1.0-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey)
![Status](https://img.shields.io/badge/status-Alpha-orange)

---
## What This Does

WriteMe provides a comprehensive solution for generating high-quality READMEs for developer projects, offering a range of features to streamline the documentation process:

*   **Progressive 3-phase interview** — Guides the user through 30 questions across 3 optional depth layers to capture full project context.
*   **Codebase scanner** — Reads the entire project directory and feeds source code directly to Gemini for a more accurate README.
*   **AI-powered generation** — Sends interview answers and codebase to Gemini 2.5 Flash with the v5 system prompt to generate a production-grade README.
*   **README writer** — Creates a new `README.md` or overwrites/appends an existing one with collision detection.
*   **API key management** — Stores the Gemini API key securely in the user config directory, prompting once and never again.
*   **Sensitive file protection** — Automatically skips `.env` files, keys, certificates, and credentials during codebase scanning.
*   **Token budget management** — Truncates large files and prioritises key source files to stay within Gemini's context window.
*   **Retry logic** — Automatically retries on 429 rate limit errors with exponential backoff.
*   **SKIP keyword** — Skips a question entirely, sending no answer to Gemini for that question.
*   **TLDR keyword** — Sends a generic answer to Gemini, allowing it to infer context from the codebase.
*   **RTFM keyword** — Shows detailed help and examples for the current question.
*   **QUIT keyword** — Exits the interview with confirmation, cancelling README generation.
*   **`--reset` flag** — Clears the saved API key so the user can rotate credentials.
*   **`--version` flag** — Prints the current installed version.
*   **Rich terminal UI** — Features styled panels, colored output, and an ASCII logo banner for an improved user experience.

## Requirements

To run WriteMe, ensure you have:

*   **Python 3.12+**
*   The following Python packages (automatically installed via `pip install writeme`):
    *   `google-genai>=1.67.0`
    *   `python-dotenv>=1.2.2`
    *   `platformdirs>=4.0.0`
    *   `rich>=14.3.3`
    *   `pip-audit>=2.10.0`
    *   `pyasn1>=0.6.3`
    *   `pathspec>=1.0.4`

## Setup

Follow these steps to get WriteMe up and running from a clean slate:

1.  Clone the repository:
    ```bash
    git clone https://github.com/ushiecodes/writeme.git
    ```
2.  Navigate into the project directory:
    ```bash
    cd writeme
    ```
3.  Install the project dependencies using pip:
    ```bash
    pip install writeme
    ```
4.  Run the WriteMe CLI tool. On the first run, you will be prompted to enter your Google Gemini API key.
    ```bash
    writeme
    ```

## Usage

The primary workflow for using WriteMe involves launching the CLI tool in your project directory, answering a series of questions, and then letting the AI generate your `README.md` file.

1.  User navigates to their project directory in the terminal.
2.  User runs `writeme`.
3.  The tool displays a banner and an information panel.
4.  The tool checks for a saved Gemini API key in `~/.config/writeme/config.json`.
5.  If no key exists, the user is prompted to enter their Gemini API key, which is then saved for future use.
6.  The Phase 1 interview begins, asking 5 initial questions about the project.
7.  The user answers questions; they can type `SKIP`, `TLDR`, `RTFM`, or `QUIT` at any time for specific interactions.
8.  A layer prompt appears, allowing the user to choose to complete "done" (finish), "layer 2" (add usage, config, architecture), "layer 3" (add security, deployment, changelog, contributing), or "more" (both layer 2 and 3).
9.  If Layer 2 is chosen, Batch A (Q6-Q11) and then Batch B (Q12-Q16) questions are asked.
10. If Layer 3 is chosen, Groups A (Q17-Q22), B (Q23-Q25), and C (Q26-Q30) questions are asked.
11. The interview completes, and the tool scans the project codebase.
12. Sensitive files, binary files, and oversized files are automatically skipped.
13. Interview answers and the codebase are assembled into a single prompt.
14. The prompt is sent to Gemini 2.5 Flash with the v5 system prompt as a system instruction.
15. Gemini generates the `README.md` content and returns it.
16. The tool strips any markdown code fences from the response.
17. If `README.md` already exists in the current directory, the user is asked to overwrite, append, or cancel.
18. The generated `README.md` is written to the current working directory.
19. The user sees a final success message: "Done. Your README is ready."

## Configuration Reference

WriteMe uses the following configuration options:

| Variable           | Purpose                                                 | Default          | Valid Values                                      | Required |
| :----------------- | :------------------------------------------------------ | :--------------- | :------------------------------------------------ | :------- |
| `API_KEY`          | 🔑 Gemini API key used to authenticate requests         | `none`           | any valid Gemini API key string                   | required |
| `MODEL`            | Gemini model used for generation                        | `gemini-2.5-flash` | any model returned by `client.models.list()`      | optional |
| `MAX_FILE_SIZE_KB` | maximum size of a single file the scanner will read     | `150`            | any positive integer                              | optional |
| `MAX_TOTAL_CHARS`  | maximum total characters sent to Gemini from codebase scan | `400000`         | any positive integer                              | optional |

These variables are loaded in the following order of precedence:
1.  **Config file:** `API_KEY` is primarily stored and loaded from a JSON file at `~/.config/writeme/config.json`.
2.  **.env file:** A local `.env.local` file (for development only) can also provide `API_KEY` via `python-dotenv`.
3.  **Hardcoded defaults with environment override:** `MODEL`, `MAX_FILE_SIZE_KB`, and `MAX_TOTAL_CHARS` have hardcoded defaults in the source, but can be overridden by environment variables set before launch.

## Architecture

### Folder Tree

```
.
├── .gitignore                   # Specifies intentionally untracked files to ignore.
├── cli.py                       # Entry point, argument parsing, orchestrates the full run sequence.
├── config.py                    # API key storage, retrieval, and reset logic.
├── display.py                   # All Rich terminal UI rendering, panels, banner, and styled output.
├── gemini.py                    # Assembles the prompt and handles all Gemini API communication.
├── interview.py                 # Runs the 3-phase question flow and formats answers for Gemini.
├── LICENSE                      # Contains the project's open-source license.
├── prompt.py                    # Stores the v5 system prompt as a single string constant.
├── pyproject.toml               # Package metadata, dependencies, and CLI entry point definition.
├── README.md                    # The project's primary documentation file.
├── scanner.py                   # Walks the project directory, filters sensitive and binary files,
|                                  enforces token budget, formats codebase for Gemini.
├── writer.py                    # Writes or updates README.md with collision detection and output cleaning.
└── __init__.py                  # Marks the directory as a Python package.

```

### Critical Execution Path

This sequence describes the critical path from a user running `writeme` to the final `README.md` being generated:

1.  User runs `writeme` in terminal.
2.  `cli.main()` is called via the `pyproject.toml` entry point.
3.  `argparse` parses `--reset` or `--version` flags if present.
4.  `display.print_banner()` renders the ASCII logo panel.
5.  `config.load_api_key()` checks `~/.config/writeme/config.json` for a saved key.
6.  `display.print_info_box()` renders the info panel with running directory and API key status.
7.  `config.get_api_key()` prompts for key if not found, saves via `config.save_api_key()`.
8.  `interview.run_interview()` starts the phase controller.
9.  `interview.run_phase_one()` asks Q1-Q5 via `input()` and collects answers into a dict.
10. `interview._ask_layer_prompt()` shows the styled layer options panel.
11. `interview._parse_layer_intent()` parses the user response.
12. `interview.run_phase_two()` asks Q6-Q16 if layer 2 was chosen.
13. `interview.run_phase_three()` asks Q17-Q30 if layer 3 was chosen.
14. `run_interview()` returns the complete answers dict or `None` if user quit.
15. `gemini.generate_readme()` is called with the answers dict.
16. `config.get_api_key()` loads the saved API key.
17. `genai.Client()` initialises the Gemini client.
18. `scanner.scan_codebase()` walks the current directory with `os.walk()`.
19. `scanner` applies `IGNORED_DIRS`, `ALWAYS_IGNORE`, `IGNORED_FILES`, `IGNORED_SUFFIXES`, `IGNORED_PREFIXES`, `TEXT_EXTENSIONS` whitelist, and `is_binary_file()` check.
20. `scanner` reads each allowed file with `filepath.read_text()`.
21. `scanner.format_codebase_for_prompt()` assembles priority files first then remaining files within token budget.
22. `interview.format_answers()` converts the answers dict into a labeled plain text string.
23. The full prompt is assembled combining `formatted_answers` and `codebase_context`.
24. `gemini._call_with_retry()` sends the prompt to Gemini with the v5 system prompt as system instruction.
25. `client.models.generate_content()` makes the API call to Gemini 2.5 Flash.
26. On 429 error, exponential backoff waits and retries up to 3 times.
27. `response.text` is returned to `generate_readme()`.
28. `writer.write_readme()` receives the generated markdown.
29. `writer._clean_output()` finds the first top-level heading and strips everything before it.
30. If `README.md` exists, user is prompted to overwrite, append, or cancel.
31. `Path.write_text()` writes the final `README.md` to the current directory.
32. `cli.main()` calls `display.print_success()` with "Done. Your README is ready."

### Component Communication Model

All modules communicate via direct Python function calls and return values. The only external communication is an outbound HTTPS call to the Gemini API at `generativelanguage.googleapis.com` via the `google-genai` SDK. Rich display functions from `display.py` are called throughout all modules for consistent terminal output. There is no inter-process communication, message queue, or shared database communication within the application itself.

### Design Decision Log

1.  **API key stored in `~/.config/writeme/config.json` instead of per-project `.env` files:** This allows the user to set their Gemini API key once and use it across all projects without re-entering it each time, improving the user experience for a global CLI tool.
2.  **Codebase injected directly into the Gemini prompt instead of summarising it:** This approach significantly reduces the risk of hallucination and ensures that the generated README accurately reflects the actual code and structure, rather than relying solely on the developer's memory or description.
3.  **Progressive 3-phase interview with optional depth layers:** This design prevents user overwhelm by breaking down the extensive questionnaire into manageable phases. Phase 1 provides a publishable draft, allowing users to choose additional depth only if needed for comprehensive documentation.
4.  **`QUIT_SENTINEL` pattern for quit handling:** This allows for a clear quit confirmation while preserving any answers already collected. It cleanly signals to `cli.py` to cancel README generation without losing previously entered data.
5.  **Plain text format for answers sent to Gemini instead of JSON or TOML:** This was chosen to reduce token count and because Gemini generally handles labeled plain text more effectively for this specific use case, minimizing parsing errors or misinterpretations.
6.  **`SKIP` and `TLDR` are distinct keywords:** `SKIP` stores nothing for a given question, instructing Gemini to infer entirely from the codebase. `TLDR` sends a generic placeholder answer, providing Gemini with an explicit fallback signal for inference, which can be useful when specific details are known but concise.
7.  **`TEXT_EXTENSIONS` whitelist in `scanner`:** Blocks binary files from being sent to Gemini by default, without relying solely on extension matching. The `is_binary_file()` null-byte sniff acts as an additional safety net.
8.  **Priority file bucketing before token budget loop:** Ensures key files like `cli.py`, `pyproject.toml` always appear in the prompt even on large codebases, preventing important architectural context from being excluded due to token budget starvation.
9.  **All terminal output routed through `display.py` Rich functions:** Ensures consistent styling across all modules and centralizes UI management, making it easy to restyle the entire terminal interface from one file.

## Security

### Data Handling and Storage

WriteMe handles the **Gemini API key** as its only sensitive data. This key is stored in plaintext JSON at `~/.config/writeme/config.json` on the user's local machine. The security of this key relies on the operating system's file permissions for the user's home directory. WriteMe does not handle passwords, personally identifiable information (PII), financial data, or session state.

### Authentication Model

There is no authentication or authorisation model within WriteMe itself. It operates as a local CLI tool, and access to its functionality is entirely controlled by the operating system user running the application. The only credential involved is the Gemini API key, which is read by `config.get_api_key()` at runtime to authenticate requests to the Google Gemini API.

### Network Exposure

WriteMe is a local-only application. It does not open any inbound network ports, run a server, or expose any services to the local area network (LAN) or the internet. Its only network interaction is a single outbound HTTPS call to the Google Gemini API at `generativelanguage.googleapis.com` to facilitate README generation.

### Safe to Commit / Never Commit

**Safe to commit:**
*   All application source code files (`.py`)
*   `pyproject.toml`
*   `LICENSE`
*   `README.md` (the generated output, and this documentation itself)

**Never commit:**
Files listed in `.gitignore` should never be committed to the repository. This includes:
*   Python-generated files (`__pycache__/`, `*.py[oc]`, `build/`, `dist/`, `wheels/`, `*.egg-info`)
*   Virtual environments (`.venv`, `.env.local`)
*   `uv` package lock files (`.python-version`, `uv.lock`)
*   Any other files containing credentials, secrets, or local environment variables (e.g., your Gemini API key, `.env` files).

### `.gitignore` Contents

```
# Python-generated files
__pycache__/
*.py[oc]
build/
dist/
wheels/
*.egg-info
.ruff_cache/

# Virtual environments
.venv
.env.local

# uv packages
.python-version
uv.lock

# OS / Editors
.DS_Store
Thumbs.db
.idea/
.vscode/
```

### Dependency Audit Output

```
No known vulnerabilities found
Name    Skip Reason
------- ----------------------------------------------------------------------
writeme Dependency not found on PyPI and could not be audited: writeme (0.1.0)
```

### Known Security Limitations and Assumptions

*   The Gemini API key is stored in plaintext JSON at `~/.config/writeme/config.json`. Its security relies on the operating system's file permissions for the user's home directory.
*   The tool reads the entire project codebase and sends it to the Google Gemini API. **Do not run this tool on codebases containing sensitive data** beyond what is already covered by the sensitive file filters (e.g., highly confidential algorithms, proprietary business logic that cannot leave the local machine without approval).
*   The sensitive file scanner covers common patterns but is not exhaustive. Users should **verify their `.gitignore` file and scanner configurations cover all sensitive files** before running WriteMe on projects containing highly sensitive data.
*   One known vulnerability exists in a transitive dependency: `pyasn1 0.6.2` (`CVE-2026-30922`). This is addressed by upgrading `pyasn1` to version `0.6.3` or higher, which is captured in the changelog.

## Deployment

WriteMe is a local-only CLI tool. It is not containerized, and there are no differences between local development and production environments. Users install it via `pip install writeme` and run `writeme` in their project directory. No production-specific setup steps are required beyond the initial installation.

## Troubleshooting

### `ModuleNotFoundError: No module named 'google'`
**Cause:** Required Python dependencies, specifically the `google-genai` library, are not installed or are not accessible in your Python environment.
**Fix:**
```bash
pip install writeme
```

### `google.genai.errors.ClientError: 429 RESOURCE_EXHAUSTED`
**Cause:** You have exceeded the free tier quota for the Gemini API.
**Fix:**
Wait until midnight Pacific time for your quota to reset. Alternatively, generate a fresh API key at `aistudio.google.com/apikey` and clear your saved key by running:
```bash
writeme --reset
```
Then, re-run `writeme` and enter the new API key when prompted.

### `RuntimeError: Gemini rate limit hit after all retries. Wait a few minutes and try again, or use a different API key.`
**Cause:** The daily free tier limit for the Gemini API has been exhausted, even after WriteMe's internal retry logic.
**Fix:**
Wait for the daily quota to reset (typically at midnight Pacific time). If you need to proceed immediately, generate a fresh API key at `aistudio.google.com/apikey` and reset your current key:
```bash
writeme --reset
```
Then, re-run `writeme` and enter the fresh API key.

## Changelog
Changelog generated from `git log --oneline -20`.
### [0.1.0] — 2026-03-21
#### Added
- Enhanced prompt and message display with Rich text and dedicated helpers.
- Implemented comprehensive file filtering using .gitignore.
- Improved console output with Rich tables.
- Enhanced CLI output with banner and styling.
- Added Rich-based console display module.
- Added `QUIT_SENTINEL` for explicit exit handling in interviews.
- Integrated `ruff` and `twine` for dev workflow, cleaned up imports and CLI entry.
- Added `pip-audit` and build dev dependencies.
- Improved CLI info display and API key handling.
- Consolidated display functions for phase and controls printing.
- Added MIT license.
- Refined scanner file filtering and size limits.
- Improved configuration module's use of display functions for API key messages.
- Improved writer module's use of display functions for user output.
#### Fixed
- Reliably found the first top-level heading in generated output.
- Handled skipped interviews and improved prompts.
#### Security
- Updated `pyasn1` dependency to address `CVE-2026-30922`.

## Contributing

Yes, WriteMe is open to contributions! We welcome developers to help improve the tool.

**Branching Strategy:**
Fork the repository, then create a feature branch from `main` for your changes.

**Pull Request Process:**
1.  Open a Pull Request (PR) against the `main` branch.
2.  Provide a clear and concise description of your changes.
3.  Ensure each PR focuses on a single feature or bug fix.

**Code Style:**
Adhere to PEP8 standards. Before submitting a PR, run a linter like `ruff` to ensure your code complies with the project's style guidelines.

**Bug Reporting:**
Report bugs via GitHub Issues at [https://github.com/ushiecodes/writeme/issues](https://github.com/ushiecodes/writeme/issues). Please include:
*   The exact error message.
*   Your operating system.
*   Your Python version.
*   Detailed steps to reproduce the bug.

**Feature Requests:**
Submit feature requests via GitHub Issues. Describe the problem your proposed feature solves, rather than just the solution itself.

## License & Credits

This project is licensed under the **MIT License**.

**Maintainer:**
Utkarsh Kamat
*   Email: work.utkarshkamat@gmail.com
*   GitHub: [ushiecodes](https://github.com/ushiecodes)

**Third-party Libraries:**
WriteMe uses the following third-party libraries, installed via `pip` and listed in `pyproject.toml`, each under its respective open-source license:
*   `google-genai` (Apache 2.0 License)
*   `python-dotenv` (BSD License)
*   `platformdirs` (MIT License)
*   `rich` (MIT License)
*   `pip-audit` (Apache 2.0 License)
*   `pyasn1` (BSD 3-Clause License)
*   `pathspec` (MIT License)
