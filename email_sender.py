import smtplib
import os
from getpass import getpass
from email.message import EmailMessage
from rich.console import Console
from rich.panel import Panel

console = Console()

# Default placeholders
DEFAULT_SMTP = "smtp.gmail.com"
DEFAULT_PORT = 587


def get_user_input():

    console.print(Panel("CLI Email Sender", style="cyan"))

    smtp_server = console.input(
        f"SMTP server (default {DEFAULT_SMTP}): "
    ).strip() or DEFAULT_SMTP

    port_input = console.input(
        f"SMTP port (default {DEFAULT_PORT}): "
    ).strip()

    port = int(port_input) if port_input else DEFAULT_PORT

    sender = console.input("Sender email: ").strip()

    password = getpass("Email password or app password: ")

    recipients = console.input(
        "Recipients (comma separated): "
    ).strip().split(",")

    subject = console.input("Subject: ").strip()

    console.print("Enter email message. Finish with an empty line.")

    lines = []
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)

    body = "\n".join(lines)

    attachments_input = console.input(
        "Attachment file paths (comma separated, optional): "
    ).strip()

    attachments = []

    if attachments_input:
        attachments = [a.strip() for a in attachments_input.split(",")]

    return smtp_server, port, sender, password, recipients, subject, body, attachments


def build_email(sender, recipients, subject, body, attachments):

    msg = EmailMessage()

    msg["From"] = sender
    msg["To"] = ", ".join(recipients)
    msg["Subject"] = subject

    msg.set_content(body)

    for file_path in attachments:

        if not os.path.exists(file_path):
            console.print(f"[red]Attachment not found: {file_path}[/red]")
            continue

        with open(file_path, "rb") as f:
            data = f.read()
            filename = os.path.basename(file_path)

        msg.add_attachment(
            data,
            maintype="application",
            subtype="octet-stream",
            filename=filename,
        )

    return msg


def send_email(server, port, sender, password, message):

    try:

        with smtplib.SMTP(server, port) as smtp:

            smtp.starttls()

            smtp.login(sender, password)

            smtp.send_message(message)

        console.print("[green]Email sent successfully![/green]")

    except Exception as e:

        console.print(f"[red]Failed to send email:[/red] {e}")


def main():

    (
        smtp_server,
        port,
        sender,
        password,
        recipients,
        subject,
        body,
        attachments,
    ) = get_user_input()

    email_msg = build_email(
        sender, recipients, subject, body, attachments
    )

    send_email(smtp_server, port, sender, password, email_msg)


if __name__ == "__main__":
    main()
