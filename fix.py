import os

def capitalize_filename(filename):
    """
    Capitalize the filename if it is not already capitalized.
    - Only works for filenames with a single word (no spaces, dashes, or underscores).
    """
    # Split the filename into name and extension
    name, ext = os.path.splitext(filename)
    
    if ext.lower() == '.txt':
        # Capitalize the filename if needed
        capitalized_name = name.capitalize()
        
        # Add the extension back
        new_filename = capitalized_name + ext
        
        return new_filename
    return filename

def fix_filenames_in_directory(directory):
    """
    Fix the capitalization of .txt files in the specified directory.
    """
    files_fixed = False
    for filename in os.listdir(directory):
        new_filename = capitalize_filename(filename)
        
        if new_filename != filename:
            old_path = os.path.join(directory, filename)
            new_path = os.path.join(directory, new_filename)
            
            # Rename the file
            os.rename(old_path, new_path)
            files_fixed = True
    
    return files_fixed

def find_desktop_path():
    """
    Try to find the Desktop directory path, including paths like OneDrive.
    """
    # Check common locations
    possible_paths = [
        os.path.join(os.path.expanduser("~"), "Desktop"),  # Default path
        os.path.join(os.path.expanduser("~"), "OneDrive", "Рабочий стол", "שולחן עבודה", "עבודה שולחן")  # OneDrive path
    ]
    
    for path in possible_paths:
        if os.path.isdir(path):
            return path
    raise FileNotFoundError("Desktop path not found.")

if __name__ == "__main__":
    # Automatically find the path to the Desktop directory
    desktop_path = find_desktop_path()
    
    # Check and fix filenames in the Desktop directory
    fix_filenames_in_directory(desktop_path)
