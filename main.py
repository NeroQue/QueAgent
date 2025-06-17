import os
import sys
from google import genai
from google.genai import types
from dotenv import load_dotenv

from schemas import get_schemas
from utils import generate_content


def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    # Get all arguments after the script name
    args = sys.argv[1:]

    system_prompt = """
You are a helpful AI coding agent.

When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

- List files and directories
- Read file contents
- Execute Python files with optional arguments
- Write or overwrite files

All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
"""

    if not args:
        print("Error: Please provide a prompt!")
        sys.exit(1)

    verbose = "--verbose" in args
    if verbose:
        args.remove("--verbose")

    user_prompt = " ".join(args)

    model = "gemini-2.0-flash-001"
    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]

    # Get all available function declarations
    available_functions = get_schemas()

    generate_content(client, model, messages, verbose, system_prompt, available_functions)


if __name__ == "__main__":
    main()