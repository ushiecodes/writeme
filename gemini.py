import time
from google import genai
from google.genai.errors import ClientError
from prompt import SYSTEM_PROMPT
from interview import format_answers
from scanner import scan_codebase, format_codebase_for_prompt
from config import get_api_key


def generate_readme(answers: dict) -> str:
    api_key = get_api_key()
    client = genai.Client(api_key=api_key)

    print("Scanning codebase...")
    scan_result = scan_codebase(".")
    codebase_context = format_codebase_for_prompt(scan_result)

    formatted_answers = format_answers(answers)

    full_prompt = f"""
{formatted_answers}

=== ACTUAL CODEBASE ===
{codebase_context}

Using both the interview answers AND the codebase above, generate a complete README.md following the system instructions exactly.
"""

    print("Generating README...")
    response = _call_with_retry(client, full_prompt)
    return response

