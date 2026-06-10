import smtplib
from email.message import EmailMessage

from typing import List

from code_modules.connectors.base.connector import Connector


class GmailConnector(Connector):

    def __init__(self, credentials_path: str):
        self.credentials_path = credentials_path

    def health_check(self) -> dict:
        return {
            "status": "healthy",
            "connector": "gmail",
        }

    def get_messages(
        self,
        max_results: int = 10
    ) -> List[dict]:

        raise NotImplementedError

    def send_message(
        self,
        to: str,
        subject: str,
        body: str
    ) -> dict:

        raise NotImplementedError

def write_email(subject, body, to_email, sender_email, sender_password):
    """
    Composes and sends a plain-text email using a secure SMTP connection.
    """
    # 1. Initialize and build the email message object
    msg = EmailMessage()
    msg.set_content(body)
    msg["Subject"] = subject
    msg["From"] = sender_email
    msg["To"] = to_email

    # 2. Establish a secure connection to the SMTP server (e.g., Gmail)
    # Port 587 is the standard port for secure TLS-encrypted mail delivery
    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()  # Upgrade the connection to secure TLS encryption
            server.login(sender_email, sender_password)
            server.send_message(msg)
            print("Email sent successfully!")
            
    except Exception as e:
        print(f"An error occurred: {e}")

def send_email(server_name, sender, receiver, user_password):
    smtp_server = server_name
    port = 465 #
    sender_email = sender
    password = user_password
    receiver_email = receiver

    # 2. Create the Message
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = ""

    body = "This is an automated message sent from a Python script."
    message.attach(MIMEText(body, "plain"))

    # 3. Connect and Send
    try:
        with smtplib.SMTP_SSL(smtp_server, port) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message.as_string())
        print("Email sent successfully!")
    except Exception as e:
        print(f"Error occurred: {e}")
