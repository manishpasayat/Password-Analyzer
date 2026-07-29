import customtkinter as ctk
import math
import random 
import string
from tkinter import messagebox


class PasswordAnalyzerGUI:

    def __init__(self):

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        self.app = ctk.CTk()
        self.app.title("Password Analyzer v1.0")
        self.app.geometry("900x850")
        self.app.resizable(True, True)

        self.title = ctk.CTkLabel(
            self.app,
            text="Password Analyzer",
            font=("Arial", 28, "bold")
        )


        self.title.pack(pady=30)
        self.password_label = ctk.CTkLabel(
        self.app,
        text="Enter Password",
        font=("Arial", 16)
)

        self.password_label.pack(pady=(20, 10))

        self.password_entry = ctk.CTkEntry(
        self.app,
        width=500,
        height=40,
        placeholder_text="Type your password here...",
        show="*"
)

        self.password_entry.pack()
        self.show_password = ctk.CTkCheckBox(
            self.app,
            text="Show Password",
            command=self.toggle_password
)

        self.show_password.pack(pady=10)

        self.button_frame = ctk.CTkFrame(
        self.app,
            fg_color="transparent"
)
        self.button_frame.pack(pady=20)

        self.analyze_button = ctk.CTkButton(
        self.button_frame,
        text="Analyze Password",
        width=180,
        height=40,
        command=self.analyze_password
)
        self.analyze_button.pack(
            side="left",
            padx=10
)
        self.generate_button = ctk.CTkButton(
        self.button_frame,
        text="Generate Password",
        width=180,
        height=40,
        command=self.generate_password

)
        self.generate_button.pack(
            side="left",
            padx=10
)
        self.copy_button = ctk.CTkButton(
            self.button_frame,
            text="📋 Copy Password",
            width=180,
            height=40,
            command=self.copy_password
)
        self.copy_button.pack(
            side="left",
            padx=10
)
        self.clear_button = ctk.CTkButton(
        self.button_frame,
        text="🗑 Clear",
        width=180,
        height=40,
        command=self.clear_all
)
        self.clear_button.pack(side="left", padx=10)
        self.history_title = ctk.CTkLabel(
        self.app,
            text="Generated Password History",
            font=("Arial", 18, "bold")
)
        self.history_title.pack(pady=(20, 5))
        self.history_box = ctk.CTkTextbox(
        self.app,
            width=650,
            height=120,
            font=("Consolas", 13)
)
        self.history_box.pack(pady=10)
        self.history_box.insert("1.0", "No passwords generated yet.")
        self.history_box.configure(state="disabled")
        self.result_title = ctk.CTkLabel(
        self.app,
            text="Analysis Results",
            font=("Arial", 18, "bold")
)
        self.result_title.pack(pady=(10, 5))
        
        self.result_box = ctk.CTkTextbox(
        self.app,
        width=650,
        height=280,
        font=("Consolas", 14)
)
        self.result_box.pack(pady=20)
        self.result_box.insert("1.0", "Result will appear here...")
        self.result_box.configure(state="disabled")

        self.history = []
        self.footer = ctk.CTkLabel(
        self.app,
        text="Password Analyzer v1.0\nDeveloped by Manish Kumar Pasayat",
        font=("Arial",12)
)       
        self.footer.pack(pady=15)

    def run(self):
       self.app.mainloop()

    def analyze_password(self):
        password = self.password_entry.get()
        common_passwords = [
                            "password",
                            "123456",
                            "123456789",
                            "qwerty",
                            "admin",
                            "welcome",  
                            "abc123",
                            "password123",  
                            "letmein",  
                            "football"
                        ]
        score = 0
        result = ""

        if len(password) >= 8:
            score+=2
            result += "✅ Length: Good\n"
        else:
            result += "❌ Length: Minimum 8 characters required\n"

        if any(char.isupper() for char in password):
            score+=2
            result += "✅ Contains Uppercase Letter\n"
        else:
            result += "❌ Missing Uppercase Letter\n"

        if any(char.islower() for char in password):
            score+=2
            result += "✅ Contains Lowercase Letter\n"
        else:
            result += "❌ Missing Lowercase Letter\n"

        
        if any(char.isdigit() for char in password):
            score+=2
            result += "✅ Contains Number\n"
        else:
            result += "❌ Missing Number\n"

        
        special_characters = "!@#$%^&*()-_=+[]{}|\\:;\"'<>,.?/"

        if any(char in special_characters for char in password):
            score += 2
            result += "✅ Contains Special Character\n"
        else:
            result += "❌ Missing Special Character\n"

        if score <= 2:
            strength = "Weak"
        elif score <= 5:
            strength = "Moderate"
        elif score <= 8:
            strength = "Strong"
        else:
            strength = "Very Strong"

        result += f"\nScore: {score}/10"
        result += f"\nStrength: {strength} 🟢"
        if strength == "Weak":
            strength_color = "red"
        elif strength == "Moderate":
            strength_color = "orange"
        elif strength == "Strong":
            strength_color = "green"
        else:
            strength_color = "cyan"
        result += "\n\nSuggestions:\n"

        if len(password) < 8:
            result += "• Use at least 8 characters.\n"

        if not any(char.isupper() for char in password):
            result += "• Add an uppercase letter.\n"

        if not any(char.islower() for char in password):
            result += "• Add a lowercase letter.\n"

        if not any(char.isdigit() for char in password):
            result += "• Add a number.\n"

        if not any(char in special_characters for char in password):
            result += "• Add a special character.\n"

        if score == 10:
            result += "Excellent! Your password follows all recommended checks."
        pool = 0

        if any(char.islower() for char in password):
            pool += 26

        if any(char.isupper() for char in password):
            pool += 26

        if any(char.isdigit() for char in password):
            pool += 10

        if any(char in special_characters for char in password):
            pool += len(special_characters)

        if pool > 0:
            entropy = len(password) * math.log2(pool)
        else:
            entropy = 0

        result += f"\nEntropy: {entropy:.2f} bits"

        if entropy < 40:
            result += "\nEntropy Rating: Low"

        elif entropy < 60:
            result += "\nEntropy Rating: Medium"

        elif entropy < 80:
            result += "\nEntropy Rating: High"

        else:
            result += "\nEntropy Rating: Excellent"

       
        if password.lower() in common_passwords:
            score = max(0, score - 4)

            result += "\n\n⚠ WARNING!"
            result += "\nThis password is commonly used."
            result += "\nIt is vulnerable to dictionary attacks."
            result += "\nChoose a unique password."


        self.result_box.configure(state="normal")
        self.result_box.delete("1.0", "end")
        self.result_box.insert("end", result)
        self.result_box.configure(state="disabled")

    def generate_password(self):

        lowercase = string.ascii_lowercase
        uppercase = string.ascii_uppercase
        digits = string.digits
        symbols = "!@#$%^&*()-_=+[]{}|\\:;\"'<>,.?/"

       
        password = [
            random.choice(lowercase),
            random.choice(uppercase),
            random.choice(digits),
            random.choice(symbols)
        ]


        all_characters = lowercase + uppercase + digits + symbols

        for _ in range(12):
            password.append(random.choice(all_characters))


        random.shuffle(password)

        password = "".join(password)

        self.password_entry.delete(0, "end")
        self.password_entry.insert(0, password)

        self.analyze_password()
       
        self.history.append(password)

        if len(self.history) > 5:
            self.history.pop(0)
        history_text = ""

        for pwd in reversed(self.history):
            history_text += f"{pwd}\n"
        self.history_box.configure(state="normal")
        self.history_box.delete("1.0", "end")
        self.history_box.insert("1.0", history_text)
        self.history_box.configure(state="disabled")


    def toggle_password(self):
        if self.show_password.get() == 1:
            self.password_entry.configure(show="")
        else:
            self.password_entry.configure(show="*")

    def copy_password(self):

        password = self.password_entry.get()

        if password == "":
            messagebox.showwarning(
                "Warning",
                "There is no password to copy."
            )
            return

        self.app.clipboard_clear()
        self.app.clipboard_append(password)

        messagebox.showinfo(
            "Success",
            "Password copied to clipboard!"
        )
    def clear_all(self):

        self.password_entry.delete(0, "end")

        self.result_box.configure(state="normal")
        self.result_box.delete("1.0", "end")
        self.result_box.insert("1.0", "Result will appear here...")
        self.result_box.configure(state="disabled")

        self.history.clear()

        self.history_box.configure(state="normal")
        self.history_box.delete("1.0", "end")
        self.history_box.insert("1.0", "No passwords generated yet.")
        self.history_box.configure(state="disabled")