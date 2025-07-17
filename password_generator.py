import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import random
import pyperclip


# Function to generate password
def generate_password():
    try:
        length = int(length_entry.get())
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number for length.")
        return

    if length < 4:
        messagebox.showerror("Error", "Password length should be at least 4 characters.")
        return

    password = []
    characters = ""

    if use_uppercase.get():
        characters += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if use_lowercase.get():
        characters += "abcdefghijklmnopqrstuvwxyz"
    if use_digits.get():
        characters += "0123456789"
    if use_symbols.get():
        characters += "!@#$%^&*()-_=+"

    if characters == "":
        messagebox.showerror("Error", "Please select at least one character set.")
        return

    password = [random.choice(characters) for _ in range(length)]
    generated_password.set("".join(password))

# Function to copy password to clipboard
def copy_to_clipboard():
    pyperclip.copy(generated_password.get())
    messagebox.showinfo("Copied", "Password copied to clipboard!")

# Main app window
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x350")
root.resizable(False, False)

# Header frame
header_frame = tk.Frame(root, bg="#4A90E2", height=50)
header_frame.pack(fill="x")

header_label = tk.Label(header_frame, text="Password Generator", font=("Helvetica", 16), fg="white", bg="#4A90E2")
header_label.pack(pady=10)

# Main content frame
content_frame = tk.Frame(root, padx=20, pady=20)
content_frame.pack(fill="both", expand=True)

# Password Length Label and Entry
length_label = tk.Label(content_frame, text="Password Length:", font=("Arial", 12))
length_label.grid(row=0, column=0, sticky="w", pady=5)
length_entry = tk.Entry(content_frame, font=("Arial", 12), width=5)
length_entry.grid(row=0, column=1, pady=5)
length_entry.insert(0, "8")

# Character Set Options
use_uppercase = tk.BooleanVar(value=True)
use_lowercase = tk.BooleanVar(value=True)
use_digits = tk.BooleanVar(value=True)
use_symbols = tk.BooleanVar()

uppercase_check = tk.Checkbutton(content_frame, text="Include Uppercase", variable=use_uppercase, font=("Arial", 10))
uppercase_check.grid(row=1, column=0, columnspan=2, sticky="w", pady=2)

lowercase_check = tk.Checkbutton(content_frame, text="Include Lowercase", variable=use_lowercase, font=("Arial", 10))
lowercase_check.grid(row=2, column=0, columnspan=2, sticky="w", pady=2)

digits_check = tk.Checkbutton(content_frame, text="Include Digits", variable=use_digits, font=("Arial", 10))
digits_check.grid(row=3, column=0, columnspan=2, sticky="w", pady=2)

symbols_check = tk.Checkbutton(content_frame, text="Include Symbols", variable=use_symbols, font=("Arial", 10))
symbols_check.grid(row=4, column=0, columnspan=2, sticky="w", pady=2)

# Generate Button
generate_button = tk.Button(content_frame, text="Generate Password", command=generate_password, font=("Arial", 12), bg="#4A90E2", fg="white")
generate_button.grid(row=5, column=0, columnspan=2, pady=15)

# Display generated password
generated_password = tk.StringVar()
password_display = ttk.Entry(content_frame, textvariable=generated_password, font=("Arial", 12), state='readonly', width=30)
password_display.grid(row=6, column=0, columnspan=2, pady=5)

# Copy to Clipboard Button
copy_button = tk.Button(content_frame, text="Copy to Clipboard", command=copy_to_clipboard, font=("Arial", 12), bg="#4A90E2", fg="white")
copy_button.grid(row=7, column=0, columnspan=2, pady=10)

# Run the Tkinter event loop
root.mainloop()
