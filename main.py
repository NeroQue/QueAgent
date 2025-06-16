import os
import sys
from google import genai
from google.genai import types
from dotenv import load_dotenv


def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    # Get all arguments after the script name
    args = sys.argv[1:]

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
    generate_content(client, model, messages, verbose)


def generate_content(client, model, messages, verbose):
    response = client.models.generate_content(model=model, contents=messages)

    print(response.text)

    if verbose:
        print("\nDebug information:")
        print("User prompt:", messages[0].parts[0].text)
        print("Prompt tokens:", response.usage_metadata.prompt_token_count)
        print("Response tokens:", response.usage_metadata.candidates_token_count)


if __name__ == "__main__":
    main()