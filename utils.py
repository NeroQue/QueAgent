from google.genai import types

def generate_content(client, model, messages, verbose, system_prompt, available_functions):
    """Generate content using the Gemini API"""

    config = types.GenerateContentConfig(
        tools=[available_functions], 
        system_instruction=system_prompt
    )

    response = client.models.generate_content(
        model=model,
        contents=messages,
        config=config
    )

    if response.function_calls:
        for function_call_part in response.function_calls:
            print(f"Calling function: {function_call_part.name}({function_call_part.args})")
    else:
        print(response.text)

    if verbose:
        print("\nDebug information:")
        print("User prompt:", messages[0].parts[0].text)
        print("Prompt tokens:", response.usage_metadata.prompt_token_count)
        print("Response tokens:", response.usage_metadata.candidates_token_count)
