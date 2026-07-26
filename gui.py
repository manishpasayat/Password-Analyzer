import customtkinter as ctk

class PasswordAnalyzerGUI:

    def __init__(self):

        # Appearance
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        # Main Window
        self.app = ctk.CTk()
        self.app.title("Password Analyzer")
        self.app.geometry("700x500")
        self.app.resizable(False, False)

        # Title
        self.title = ctk.CTkLabel(
            self.app,
            text="Password Analyzer",
            font=("Arial", 28, "bold")
        )

        self.title.pack(pady=30)# Label for password input
        self.password_label = ctk.CTkLabel(
        self.app,
        text="Enter Password",
        font=("Arial", 16)
)

        self.password_label.pack(pady=(20, 10))

        # Password Entry Box
        self.password_entry = ctk.CTkEntry(
        self.app,
        width=350,
        height=40,
        placeholder_text="Type your password here...",
        show="*"
)

        self.password_entry.pack()
        
        self.analyze_button = ctk.CTkButton(
        self.app,
        text="Analyze Password",
        width=200,
        height=40,
        command=self.analyze_password

)

        self.analyze_button.pack(pady=25)
        
        self.result_label = ctk.CTkLabel(
        self.app,
        text="Result will appear here",
        font=("Arial", 18, "bold"),
        text_color="white"
)

        self.result_label.pack(pady=20)
                         

    def run(self):
       self.app.mainloop()

    def analyze_password(self):
        password = self.password_entry.get()
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

        if score <= 3:
            strength = "Weak"
        elif score <= 6:
            strength = "Moderate"
        elif score <= 8:
            strength = "Strong"
        else:
            strength = "Very Strong"

        result += f"\nScore: {score}/10"
        result += f"\nStrength: {strength}"

        self.result_label.configure(
            text=result,
            text_color="white"
        )