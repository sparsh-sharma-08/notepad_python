# notepad_python
Version 1.0

# Project Overview:
This Python-based text editor allows users to perform basic file operations such as:

1) Writing to a file
2) Appending text to an existing file
3) Reading the contents of a file
4) Renaming a file
-> The program interacts with the user via a text-based menu and handles various file errors gracefully, providing informative messages when things go wrong (such as permission issues or missing files).

# Features:
- Write to a File: Allows users to create a new file or overwrite an existing one with new content.
- Append to a File: Adds new content to the end of an existing file without removing its previous contents.
- Read from a File: Displays the content of an existing file.
- Rename a File: Allows users to rename an existing file.
- Graceful Error Handling: Catches common file-related errors (e.g., file not found, permission denied) and displays helpful error messages.

# Requirements:
Python 3.x (compatible with Python 3.x versions)
Operating system with file management capabilities (Windows, macOS, or Linux)

# How to Use:
Clone or download this project to your local machine.

Open the terminal or command prompt and navigate to the project folder.

Run the Python script using the following command:

bash
Copy code
python text_editor.py
The program will display a menu with the following options:

1: Write text to a file.
2: Append text to an existing file.
3: Read the content of a file.
4: Rename an existing file.
5: Exit the program.
Input the desired choice and follow the prompts to perform the corresponding operation.

# Error Handling:
The program includes error handling for the following situations:

1) File Not Found: When trying to read or append to a file that doesn't exist.
2) Permission Errors: When there is an issue with file permissions, such as when trying to write or rename a file that is locked.
3) Invalid Inputs: When the user enters a non-numeric value in the menu options.
