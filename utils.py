from google.genai import types
from functions.call_function import call_function

def generate_content(client, model, messages, verbose, system_prompt, available_functions):
    """Generate content using the Gemini API with agent loop"""
    
    config = types.GenerateContentConfig(
        tools=[available_functions], 
        system_instruction=system_prompt
    )
    
    # Initialize loop variables
    max_iterations = 20
    iteration = 0
    function_was_called = False
    
    while iteration < max_iterations:
        iteration += 1
        if verbose:
            print(f"\nIteration {iteration} of {max_iterations}")
        
        # Generate content with current message history
        response = client.models.generate_content(
            model=model,
            contents=messages,
            config=config
        )
        
        # Process candidate responses and add to conversation
        for candidate in response.candidates:
            if hasattr(candidate, 'content') and candidate.content:
                # Add model's response to the conversation
                messages.append(candidate.content)
        
        function_was_called = False
        
        # Process function calls if any
        if response.function_calls:
            function_was_called = True
            for function_call_part in response.function_calls:
                # Call the function
                function_call_result = call_function(function_call_part, verbose)
                
                # Validate function call result
                if not hasattr(function_call_result, 'parts') or not function_call_result.parts:
                    raise RuntimeError("Function call result missing parts")
                
                if not hasattr(function_call_result.parts[0], 'function_response'):
                    raise RuntimeError("Function call result missing function_response")
                
                if not hasattr(function_call_result.parts[0].function_response, 'response'):
                    raise RuntimeError("Function call result missing response")
                
                # Add function call result to conversation
                messages.append(types.Content(
                    role="tool",
                    parts=[function_call_result.parts[0]]
                ))
                
                if verbose:
                    print(f"-> {function_call_result.parts[0].function_response.response}")
        
        # If no function was called, we're done
        if not function_was_called:
            # Print final response
            print(response.text)
            break
    
    # If we've reached max iterations, let the user know
    if iteration >= max_iterations and function_was_called:
        print("Reached maximum number of iterations. Agent may not have completed the task.")
    
    if verbose:
        print("\nDebug information:")
        print("User prompt:", messages[0].parts[0].text)
        print("Prompt tokens:", response.usage_metadata.prompt_token_count)
        print("Response tokens:", response.usage_metadata.candidates_token_count)
        print(f"Total iterations: {iteration}")
