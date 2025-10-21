import os

def write_file(working_directory, file_path, content):
    abs_working_dir = os.path.abspath(working_directory)
    target_dir = os.path.abspath(os.path.join(working_directory, file_path))
    if not os.path.commonpath([abs_working_dir, target_dir]) == abs_working_dir:
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    try:
        os.makedirs(os.path.dirname(target_dir), exist_ok=True)
        with open(target_dir, "w") as f:
            f.write(content)
            return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f"Error: {e}"
    
