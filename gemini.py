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


def _call_with_retry(client, prompt: str, retries: int = 3) -> str:
    for attempt in range(retries):
        try:
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                config={"system_instruction": SYSTEM_PROMPT},
                contents=prompt
            )
            return response.text

        except ClientError as e:
            if "429" in str(e):
                wait = 2 ** (attempt + 1)
                print(f"Rate limited. Waiting {wait} seconds before retry {attempt + 1}/{retries}...")
                time.sleep(wait)
                if attempt == retries - 1:
                    raise RuntimeError(
                        "Gemini rate limit hit after all retries. "
                        "Wait a few minutes and try again, or use a different API key."
                    ) from e
            else:
                raise
