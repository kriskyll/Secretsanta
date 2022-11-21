'''
Secret Santa, Christmas 2022

For personal use.
@kriskyll
'''
import smtplib
from email.message import EmailMessage
import os
from dotenv import load_dotenv
_ = load_dotenv

def send_email(to, subject, message):

    email_address = os.environ.get("EMAIL_ADDRESS")
    email_password = os.environ.get("EMAIL_PASSWORD")

    # create email
    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = email_address
    msg['To'] = to
    msg.set_content(message)

    # send email
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(email_address, email_password)
        smtp.send_message(msg)

def main():
    recipient = "kristian.kyllonen@gmail.com"
    subject = "Hei sinä siellä!"
    message = "Tässä vain testailen että noinkohan tää toimii!"

    send_email(recipient, subject, message)

main()