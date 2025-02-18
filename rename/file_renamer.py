import os


def rename_files(folder_path, input_types=None, prefix="", suffix=""):
    """
    Rename files in the folder by adding a prefix or suffix to their original name.

    Params:
    - folder_path (str): Path to the folder containing files to rename.
    - input_types (list or None): List of file extensions (e.g., ['txt', 'jpg']) to filter specific types. Default is None for all files.
    - prefix (str): Text to add at the beginning of the file names.
    - suffix (str): Text to add at the end of the file names before the extension.
    """
    if not os.path.exists(folder_path):
        print(f"Error: Folder path '{folder_path}' does not exist.")
        return

    if input_types:
        # Ensure input_types contains only extensions without a dot
        input_types = [f".{ext.strip().lower()}" for ext in input_types]

    files_renamed = 0

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        # Skip folders, optionally filter files by their extensions
        if os.path.isfile(file_path) and (input_types is None or os.path.splitext(filename)[1].lower() in input_types):
            name, ext = os.path.splitext(filename)
            new_name = f"{prefix}{name}{suffix}{ext}"  # Create the new name with prefix and suffix
            new_file_path = os.path.join(folder_path, new_name)

            # Rename the file
            os.rename(file_path, new_file_path)
            files_renamed += 1
            print(f"Renamed: {filename} -> {new_name}")

    print(f"Total files renamed: {files_renamed}")


if __name__ == "__main__":
    # Specify folder path
    folder_path = input("Enter the folder path: ")

    # Optionally specify file types
    input_types = input("Enter file types (comma-separated, e.g., txt,jpg) or leave empty for all files: ")
    input_types = input_types.split(',') if input_types.strip() else None

    # Enter prefix or suffix (optional)
    prefix = input("Enter prefix (optional): ").strip()
    suffix = input("Enter suffix (optional): ").strip()

    # Perform the renaming
    rename_files(folder_path, input_types, prefix, suffix)