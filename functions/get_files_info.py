def get_files_info(working_directory, directory="."):
    relative_path = os.path.join(working_directory, directory)
    if not os.path.abspath(relative_path, working_directory):
        return f'Error: Cannot list {directory}" as it is outside the permitted working directory'

