import os


def write_file(working_directory, file_path, content):
    abs_working = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(abs_working, file_path))

    if not abs_file_path.startswith(abs_working):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

    try:
        directory = os.path.dirname(abs_file_path)
        if not os.path.exists(directory):
            os.makedirs(directory)

        with open(abs_file_path, "w") as file:
            file.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f'Error: {str(e)}'
