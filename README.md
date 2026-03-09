# Email Sender

A lightweight and interactive **Python command-line email sender** that allows users to send emails directly from the terminal.  
This tool supports **SMTP authentication, multiple recipients, and file attachments**, making it useful for quick email automation from a CLI environment.

The project is designed to demonstrate practical usage of Python's email and SMTP libraries while providing a simple and effective terminal-based workflow.

---

## Features

• Interactive command-line interface  
• Send emails using SMTP servers  
• Support for multiple recipients  
• Attach multiple files to emails  
• Secure password input using hidden terminal input  
• Compatible with Gmail using App Password authentication  
• Lightweight and easy to run from the terminal  

---

## Requirements

Python 3.x

Install the required dependency:

pip install rich

---

## How to Run

Run the program from the terminal:

python email_sender.py

You will be prompted to enter the required information:

• SMTP server  
• SMTP port  
• Sender email address  
• Email password or app password  
• Recipient email addresses  
• Email subject  
• Email message  
• Optional file attachments  

After entering the required details, the program will connect to the SMTP server and send the email.

---

## Example SMTP Settings (Gmail)

SMTP Server:
smtp.gmail.com

Port:
587

These settings are commonly used when sending emails through Gmail.

---

## Gmail App Password Setup

Gmail does not allow scripts or external applications to log in using your normal password.  
Instead, you must generate an **App Password**.

Steps to generate an App Password:

1. Open your Google Account settings.
2. Go to the **Security** section.
3. Enable **2-Step Verification** if it is not already enabled.
4. Navigate to **App Passwords**.
5. Select **Mail** as the application.
6. Generate a new password.
7. Use the generated password in this program instead of your regular Gmail password.

---

## Attachments

Attachments can be added by entering file paths separated by commas.

Example:

report.pdf,image.png,notes.txt

The program will automatically attach the files to the email before sending.

---

## Project Structure

email-sender

email_sender.py  
README.md

---

## Use Cases

This tool can be used for:

• Sending quick emails directly from the terminal  
• Automating email notifications in scripts  
• Sending reports or files through automation workflows  
• Learning how SMTP email systems work in Python  
• Practicing command-line application development  

---

## Educational Purpose

This project demonstrates several important Python concepts:

• SMTP email communication  
• MIME email message construction  
• Secure password handling  
• Command-line user interaction  
• File attachment handling  
• Error handling in network applications  

---

## License

This project is open source and available for learning, experimentation, and educational purposes.
