import string
import tkinter as tk
from tkinter import messagebox

def check_password():
    password = password_entry.get()
    upper_case = any([1 if c in string.ascii_uppercase else 0 for c in password])
    lower_case = any([1 if c in string.ascii_lowercase else 0 for c in password])
    special = any([1 if c in string.punctuation else 0 for c in password])
    digits = any([1 if c in string.digits else 0 for c in password])
    characters = [upper_case, lower_case, special, digits]
    length = len(password)
    score = 0

    with open('commonn.txt', 'r') as f:
        common = f.read().splitlines()
    
    if password in common:
        messagebox.showwarning("Weak Password", "Password was found in a common list. Score 0 / 7")
        return

    if length > 8:
        score += 1
    if length > 12:
        score += 1
    if length > 17:
        score += 1
    if length > 20:
        score += 1

    length_text = f"Password length is {length}, adding {score} points!"

    if sum(characters) > 1:
        score += 1
    if sum(characters) > 2:
        score += 1
    if sum(characters) > 3:
        score += 1

    char_text = f"Password has {sum(characters)} different character types, adding {sum(characters) - 1} points!"

    if score < 4:
        result = f"The password is quite weak! Score: {score} / 7"
    elif score == 4:
        result = f"The password is ok! Score: {score} / 7"
    elif 4 < score < 6:
        result = f"The password is decent! Score: {score} / 7"
    else:
        result = f"The password is strong! Score: {score} / 7"

    result_label.config(text=f"{length_text}\n{char_text}\n\n{result}")

# Create the main window
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("400x300")

# Create and place widgets
tk.Label(root, text="Enter the Password:").pack(pady=10)
password_entry = tk.Entry(root, show="*", width=30)
password_entry.pack(pady=5)

check_button = tk.Button(root, text="Check Password", command=check_password)
check_button.pack(pady=10)

result_label = tk.Label(root, text="", wraplength=350, justify="center")
result_label.pack(pady=10)

# Start the GUI event loop
root.mainloop()