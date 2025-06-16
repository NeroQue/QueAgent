import os
import subprocess


def run_python_file(working_directory, file_path):
    try:
        abs_working = os.path.abspath(working_directory)
        abs_file_path = os.path.abspath(os.path.join(abs_working, file_path))

        if not abs_file_path.startswith(abs_working):
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        if not os.path.exists(abs_file_path):
            return f'Error: File "{file_path}" not found.'
        if not abs_file_path.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file.'

        completed_process = subprocess.run(["python", abs_file_path], timeout=30, capture_output=True, cwd=abs_working)
        
        stdout = completed_process.stdout.decode("utf-8")
        stderr = completed_process.stderr.decode("utf-8")
        
        result = ""
        if stdout:
            result += f'STDOUT:{stdout}'
        if stderr:
            result += f'STDERR:{stderr}'
        
        if completed_process.returncode != 0:
            result += f'Process exited with code {completed_process.returncode}'
        
        if not result:
            result = "No output produced."
            
        return result
    
    except Exception as e:
        return f"Error executing Python file: {e}"