# import customtkinter as ctk


# ctk.set_appearance_mode("dark")
# ctk.set_default_color_theme("blue")

# app = ctk.CTk()
# app.title("Password Analyzer")
# app.geometry("700x500")
# app.resizable(False, False)


# title = ctk.CTkLabel(
#     app,
#     text="Password Analyzer",
#     font=("Arial", 28, "bold")
# )

# title.pack(pady=30)


# app.mainloop()


from gui import PasswordAnalyzerGUI


app = PasswordAnalyzerGUI()
app.run()