import os


def rename_files_with_iterator(folder_path, input_types=None, base_name="image"):
    """
    Rename files in the folder by assigning a new name based on an iterator.

    Params:
    - folder_path (str): Path to the folder containing files to rename.
    - input_types (list or None): List of file extensions (e.g., ['txt', 'jpg']) to filter specific types. Default is None for all files.
    - base_name (str): Base name to use for renaming files. Default is "image".
    """
    if not os.path.exists(folder_path):
        print(f"Error: Folder path '{folder_path}' does not exist.")
        return

    if input_types:
        # Ensure input_types contains only extensions without a dot
        input_types = [f".{ext.strip().lower()}" for ext in input_types]

    files_renamed = 0
    counter = 1  # Start counter for the new file names

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        # Skip folders, optionally filter files by their extensions
        if os.path.isfile(file_path) and (input_types is None or os.path.splitext(filename)[1].lower() in input_types):
            ext = os.path.splitext(filename)[1]  # Extract file extension
            new_name = f"{base_name}-{counter}{ext}"  # Create the new name, e.g., "image-1.jpg"
            new_file_path = os.path.join(folder_path, new_name)

            # Rename the file
            os.rename(file_path, new_file_path)
            files_renamed += 1
            counter += 1  # Increment the counter
            print(f"Renamed: {filename} -> {new_name}")

    print(f"Total files renamed: {files_renamed}")


if __name__ == "__main__":
    # Specify the folder path
    folder_path = input("Enter the folder path: ")

    # Optionally specify file types
    input_types = input("Enter file types (comma-separated, e.g., txt,jpg) or leave empty for all files: ")
    input_types = input_types.split(',') if input_types.strip() else None

    # Enter base name for the new files
    base_name = input("Enter base name for files (default is 'image'): ").strip() or "image"

    # Perform the renaming
    rename_files_with_iterator(folder_path, input_types, base_name)