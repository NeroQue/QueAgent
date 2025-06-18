from google.genai import types
from functions.call_function import call_function

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
            function_call_result = call_function(function_call_part, verbose)
            
            if not hasattr(function_call_result, 'parts') or not function_call_result.parts:
                raise RuntimeError("Function call result missing parts")
            
            if not hasattr(function_call_result.parts[0], 'function_response'):
                raise RuntimeError("Function call result missing function_response")
            
            if not hasattr(function_call_result.parts[0].function_response, 'response'):
                raise RuntimeError("Function call result missing response")
            
            if verbose:
                print(f"-> {function_call_result.parts[0].function_response.response}")
    else:
        print(response.text)

    if verbose:
        print("\nDebug information:")
        print("User prompt:", messages[0].parts[0].text)
        print("Prompt tokens:", response.usage_metadata.prompt_token_count)
        print("Response tokens:", response.usage_metadata.candidates_token_count)
