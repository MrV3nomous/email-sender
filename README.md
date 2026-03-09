Email Sender
A lightweight Python command-line email sender that allows users to send emails directly from the terminal.
The tool supports SMTP authentication, multiple recipients, message input, and file attachments, making it useful for quick email automation from a CLI environment.

Features
Interactive CLI prompts
Send emails using SMTP
Support for multiple recipients
Attach multiple files
Secure password input
Works with Gmail App Passwords
Lightweight and simple to run

Requirements
Python 3.x

Install dependencies: pip install rich

How to Run
Run the program from the terminal: python email_sender.py
You will be prompted to enter:
SMTP server
SMTP port
Sender email
App password
Recipients
Email subject
Email message
Optional attachments

Example SMTP Settings (Gmail)
SMTP Server: smtp.gmail.com
Port: 587

⚠️ Gmail requires an App Password, not your normal password.
Generating a Gmail App Password
Enable 2-Step Verification in your Google account.
Go to Google Account → Security → App Passwords.
Generate a password for Mail.
Use the generated password when the program asks for the email password.

Example Attachments
You can attach files by providing paths such as:
report.pdf,image.png,notes.txt
Multiple attachments should be separated by commas.

Project Structure
email-sender
│
├── email_sender.py
└── README.md

Use Cases
Sending quick emails from the terminal
Automating email notifications
Sending reports or files via scripts
Learning SMTP email automation in Python

License
This project is open source and available for learning and experimentation.
