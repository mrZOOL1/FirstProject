import os

def create_lorem_txt(file_path):
    
    lorem_text = """Lorem ipsum dolor sit amet, consectetur adipiscing elit.
    Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
    Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
    Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.
    Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."""

    # Ensure the directory exists
    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    # Write the Lorem Ipsum text to the file
    with open(file_path, 'w') as file:
        file.write(lorem_text)

if __name__ == "__main__":
    # Define the path to save the file
    file_path = r'C:\Temp\openme.txt'
    
    # Create the .txt file with Lorem Ipsum text
    create_lorem_txt(file_path)
