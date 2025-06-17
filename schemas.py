from google.genai import types

def get_schemas():
    """Return all available schemas for function declarations"""

    schema_get_files_info = types.FunctionDeclaration(
        name="get_files_info",
        description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
        parameters=types.Schema(
            type=types.Type.OBJECT,
            properties={
                "directory": types.Schema(
                    type=types.Type.STRING,
                    description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
                ),
            },
        ),
    )

    # All available function declarations should be added to this list
    function_declarations = [
        schema_get_files_info,
    ]

    return types.Tool(function_declarations=function_declarations)
