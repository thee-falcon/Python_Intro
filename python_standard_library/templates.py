# learn how to send emails in python, useful if you have a database of customers and you want to send them various emails based on theier interests

# we have email package in python standard library, in this package we have a sub package called mime.
# mime stands for multipurpose internet mail extensions, and this is standard that defines the format for email messages
# in the package mime, we have a sub package that is multi part that exposes a class called MIMEMultipart
# with this object, we can send email message that includes both html and plain text content
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from pathlib import Path
from string import Template
import smtplib

template = Template(Path("template.html").read_text())
# with this method we can replace parameters dynamically
# template.substitute()


message = MIMEMultipart()
message["from"] = "The-falcon"
message["to"] = "test_user_10@gmail.com"
message["subject"] = "This is a test"
body = template.substitute({"name": "Omar"})
message.attach(MIMEText(body, "html"))

try:
    with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
        # start the SMTP connection with a greeting 👋🏻
        smtp.ehlo()
        # upgrade the connection to a secure TLS-encrypted channel
        smtp.starttls()
        # log in to the SMTP server using the email and password
        smtp.login("omar.makran.test@gmail.com", "password123")
        # to send the message
        smtp.send_message(message)
        print("Sent...") # just for debugging
except Exception as e:
    print(f"An error occurred: {e}") 