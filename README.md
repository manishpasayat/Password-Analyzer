# Password Analyzer

A desktop application developed in Python to evaluate password security and encourage better password practices. The application analyzes passwords based on multiple security rules, estimates their strength, and provides recommendations for creating stronger passwords. It also includes a secure password generator for users who need a reliable password instantly.

---

## Overview

Weak passwords are one of the most common causes of compromised accounts. This project was developed to help users understand the quality of their passwords by performing several security checks and presenting the results through a simple graphical interface.

The application is built using **Python** and **CustomTkinter**, providing a modern desktop experience.

---

## Features

- Analyze password strength
- Check minimum password length
- Detect uppercase and lowercase letters
- Verify the presence of numbers
- Detect special characters
- Calculate password entropy
- Identify commonly used passwords
- Provide suggestions to improve weak passwords
- Generate strong random passwords
- Show or hide password input
- Copy generated passwords to the clipboard
- Maintain a history of recently generated passwords
- User-friendly graphical interface

---

## Technologies Used

- Python 3.13
- CustomTkinter
- Tkinter
- Math Module
- Random Module
- String Module

---

## Project Structure

```
Password_Analyzer/

 gui.py
 main.py
 requirements.txt
.gitignore
README.md
```

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/manishpasayat/Password-Analyzer.git
```

### 2. Open the project directory

```bash
cd Password-Analyzer
```

### 3. Install the required package

```bash
pip install customtkinter
```

### 4. Run the application

```bash
python main.py
```

---

## How It Works

The application evaluates a password using multiple security parameters.

It checks:

- Password length
- Uppercase letters
- Lowercase letters
- Numbers
- Special characters

A score is assigned based on these checks. The application then classifies the password strength and estimates its entropy to provide a better understanding of its resistance to brute-force attacks.

If the password is weak or commonly used, personalized suggestions are displayed to help the user improve it.

---

## Future Improvements

Some features that can be added in future versions include:

- Password breach detection using public databases
- Export password analysis reports
- Password expiration reminders
- Multi-language support
- Dark and light theme switching
- Password storage using encryption

---

## Learning Outcomes

This project helped me gain practical experience in:

- Python GUI development
- Object-Oriented Programming
- Password security principles
- User interface design
- Git and GitHub version control
- Building complete desktop applications

---

## Author

**Manish Kumar Pasayat**

B.Tech – Computer Science and Engineering (Cyber Security)

---

## License

This project is created for educational and learning purposes.