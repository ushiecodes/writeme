import os
from pathlib import Path

IGNORED_DIRS = {
    ".git", ".venv", "venv", "env", "__pycache__", "node_modules",
    ".mypy_cache", ".pytest_cache", "dist", "build", ".egg-info",
    "migrations", "static", "media", "coverage"
}

IGNORED_FILES = {
    # env files — all variants
    ".env",
    ".env.local",
    ".env.development",
    ".env.development.local",
    ".env.test",
    ".env.test.local",
    ".env.production",
    ".env.production.local",
    ".env.staging",
    ".env.staging.local",
    ".env.example",  # sometimes contains real values despite the name
    ".env.sample",
    ".envrc",        # direnv

    # secrets and credentials
    "secrets.json",
    "secrets.yaml",
    "secrets.yml",
    "credentials.json",
    "credentials.yaml",
    "credentials.yml",
    "serviceaccount.json",
    "service-account.json",

    # cloud provider credentials
    ".aws",
    "config.ini",

    # private keys and certs
    "id_rsa",
    "id_rsa.pub",
    "id_ed25519",
    "id_ed25519.pub",
    "id_ecdsa",
    "id_dsa",

    # terraform
    "terraform.tfvars",
    "terraform.tfvars.json",
    "override.tf",
    "override.tf.json",

    # docker
    ".docker/config.json",

    # database
    ".pgpass",
    "database.yml",   # Rails

    # ruby
    ".bundle/config",

    # node / npm
    ".npmrc",
    ".yarnrc",
    ".yarnrc.yml",

    # python
    "pip.conf",
    "pip.ini",

    # jetbrains / editors
    "*.xml",          # IntelliJ workspace files sometimes contain tokens

    # misc auth
    ".netrc",
    ".htpasswd",
    "authinfo",
    ".authinfo",
    "token",
    "token.json",
    "oauth_token",
}

IGNORED_SUFFIXES = {
    ".pem",
    ".key",
    ".cert",
    ".crt",
    ".cer",
    ".p12",
    ".pfx",
    ".jks",     # Java KeyStore
    ".keystore",
    ".asc",     # GPG
    ".gpg",
    ".pgp",
    ".ovpn",    # VPN config
}

IGNORED_PREFIXES = {
    ".env",     # catches any .env* variant not explicitly listed above
}

IGNORED_EXTENSIONS = {
    ".pyc", ".pyo", ".exe", ".dll", ".so", ".png", ".jpg",
    ".jpeg", ".gif", ".ico", ".svg", ".pdf", ".zip", ".tar",
    ".gz", ".lock", ".bin"
}

MAX_FILE_SIZE_KB = 500  # skip files larger than this
MAX_TOTAL_CHARS = 400_000

PRIORITY_FILES = {
    "main.py", "cli.py", "app.py", "index.py",
    "pyproject.toml", "setup.py", "requirements.txt",
    "Dockerfile", "docker-compose.yml", ".gitignore"
}

def scan_codebase(root: str = ".") -> dict:
    tree = []
    files = {}
    root_path = Path(root).resolve()

    for dirpath, dirnames, filenames in os.walk(root_path):
        dirnames[:] = [d for d in dirnames if d not in IGNORED_DIRS]

        for filename in filenames:
            filepath = Path(dirpath) / filename
            rel_path = str(filepath.relative_to(root_path))

            # skip ignored extensions
            if filepath.suffix in IGNORED_EXTENSIONS:
                continue

            # skip files that are too large
            if filepath.stat().st_size > MAX_FILE_SIZE_KB * 1024:
                continue

            # skip sensitive files silently
            if (
                filepath.name in IGNORED_FILES
                or filepath.suffix in IGNORED_SUFFIXES
                or any(filepath.name.startswith(p) for p in IGNORED_PREFIXES)
            ):
                continue

            tree.append(rel_path)

            try:
                content = filepath.read_text(encoding="utf-8", errors="ignore")
                files[rel_path] = content
            except Exception:
                files[rel_path] = "[unreadable]"

    # sort so priority files are included first within token budget
    files = dict(
        sorted(
            files.items(),
            key=lambda x: (0 if Path(x[0]).name in PRIORITY_FILES else 1, x[0])
        )
    )

    return {"tree": tree, "files": files}

def format_codebase_for_prompt(scan_result: dict) -> str:
    lines = []

    lines.append("=== PROJECT FILE TREE ===")
    for path in scan_result["tree"]:
        lines.append(f"  {path}")

    lines.append("\n=== FILE CONTENTS ===")

    total_chars = sum(len(line) for line in lines)

    for path, content in scan_result["files"].items():
        entry = f"\n--- {path} ---\n{content}"

        if total_chars + len(entry) > MAX_TOTAL_CHARS:
            truncated = f"\n--- {path} ---\n[TRUNCATED — file exceeds context budget]"
            lines.append(truncated)
            total_chars += len(truncated)
            continue

        lines.append(entry)
        total_chars += len(entry)

    return "\n".join(lines)
