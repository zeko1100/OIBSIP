import tkinter as tk
from tkinter import messagebox
import random
import string

class PasswordGenerator:
    def __init__(self, window):
        self.window = window
        self.window.title("Password Generator")

        # Label and entry for password length
        self.length_label = tk.Label(window, text="Password Length:", font=('Arial', 12))
        self.length_label.grid(row=0, column=0, padx=10, pady=10)

        self.length_entry = tk.Entry(window, width=10)
        self.length_entry.grid(row=0, column=1, padx=10, pady=10)

        # Checkbuttons for character inclusion options
        self.include_uppercase = tk.BooleanVar()
        self.include_numbers = tk.BooleanVar()
        self.include_symbols = tk.BooleanVar()

        self.uppercase_check = tk.Checkbutton(window, text="Include Uppercase Letters", variable=self.include_uppercase)
        self.uppercase_check.grid(row=1, column=0, columnspan=2, sticky="w", padx=10)

        self.numbers_check = tk.Checkbutton(window, text="Include Numbers", variable=self.include_numbers)
        self.numbers_check.grid(row=2, column=0, columnspan=2, sticky="w", padx=10)

        self.symbols_check = tk.Checkbutton(window, text="Include Symbols", variable=self.include_symbols)
        self.symbols_check.grid(row=3, column=0, columnspan=2, sticky="w", padx=10)

        # Button to generate the password
        self.generate_button = tk.Button(window, text="Generate Password", command=self.generate_password)
        self.generate_button.grid(row=4, column=0, columnspan=2, pady=10)

        # Label to display the generated password
        self.password_display = tk.Label(window, text="Your Password Will Appear Here", font=('Arial', 12))
        self.password_display.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

    def generate_password(self):
        try:
            length = int(self.length_entry.get())
            if length <= 0:
                raise ValueError

            char_pool = string.ascii_lowercase  # Start with lowercase letters

            if self.include_uppercase.get():
                char_pool += string.ascii_uppercase

            if self.include_numbers.get():
                char_pool += string.digits

            if self.include_symbols.get():
                char_pool += string.punctuation

            if not char_pool:
                self.password_display.config(text="Error: No character types selected")
                return

            password = ''.join(random.choice(char_pool) for _ in range(length))
            self.password_display.config(text=f"Generated Password: {password}")

        except ValueError:
            messagebox.showwarning("Input Error", "Please enter a valid number for password length")

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGenerator(root)
    root.mainloop()
