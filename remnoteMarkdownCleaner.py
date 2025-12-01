import tkinter as tk
from tkinter import filedialog, messagebox
import os


def remove_carets(file_path):
    """Remove all occurrences of '^^^' from the specified file."""
    try:
        # Read the file content
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()

        # Remove all occurrences of '^^^'
        modified_content = content.replace('^^^', '')

        # Write back to the same file
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(modified_content)

        messagebox.showinfo("Success", "All instances of '^^^' have been removed!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred:\n{str(e)}")


def select_file():
    """Open file dialog and process selected file."""
    file_path = filedialog.askopenfilename(
        title="Select Markdown File",
        filetypes=[("Markdown Files", "*.md"), ("All Files", "*.*")]
    )

    if file_path:
        remove_carets(file_path)


# Create the main application window
root = tk.Tk()
root.title("Markdown Caret Remover")
root.geometry("300x150")
root.resizable(False, False)

# Create and place widgets
frame = tk.Frame(root, padx=20, pady=20)
frame.pack(expand=True)

label = tk.Label(frame, text="Select a Markdown file to remove '^^^'")
label.pack(pady=(0, 10))

button = tk.Button(frame, text="Choose File", command=select_file,
                   bg="#4CAF50", fg="white", padx=10, pady=5)
button.pack()

# Add a label with instructions
info = tk.Label(frame, text="This will edit the file directly",
                font=("Arial", 8), fg="gray")
info.pack(pady=(10, 0))

# Start the GUI event loop
root.mainloop()
