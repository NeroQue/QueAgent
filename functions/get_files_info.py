import os


def get_files_info(working_directory, directory=None):
    if directory is None:
        directory = "."

    abs_working = os.path.abspath(working_directory)

    if directory == ".":
        abs_directory = abs_working
    elif not os.path.isabs(directory):
        abs_directory = os.path.abspath(os.path.join(working_directory, directory))
    else:
        abs_directory = os.path.abspath(directory)

    if not abs_directory.startswith(abs_working):
        return f"Error: Cannot list '{directory}' as it is outside the permitted working directory"
    elif not os.path.isdir(abs_directory):
        return f"Error: '{directory}' is not a directory"
    else:
        try:
            files = os.listdir(abs_directory)
            string = ""
            for file in files:
                pathname = os.path.join(abs_directory, file)
                size = os.path.getsize(pathname)
                is_dir = os.path.isdir(pathname)
                file_string = f"- {file}: file_size={size} bytes, is_dir={is_dir}\n"
                string += file_string
        except OSError as e:
            return f"Error: {e}"
        return string