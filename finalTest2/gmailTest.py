from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import smtplib
import os

# Hardcode the directory path
directory_path = "/Downloads/IOT-Anti-Theft-flooring-system/finalTest2"

def send_email_with_filename(filename):
    recipient = "musabtree@hotmail.com"
    sender = "cyber.talha0@gmail.com"
    subject = "Test Email with Image"
    text = "Hello world, this is an email with an image!"

    # Create a multipart message
    message = MIMEMultipart()
    message["From"] = sender
    message["To"] = recipient
    message["Subject"] = subject

    # Attach the text part
    message.attach(MIMEText(text, "plain"))

    # Create the full path to the image using the provided filename and hardcoded path
    full_path = os.path.join(directory_path, filename)

    # Attach the image
    with open(full_path, 'rb') as img_file:
        img = MIMEImage(img_file.read(), name=os.path.basename(full_path))
    message.attach(img)

    # Send the email
    smtp = smtplib.SMTP("smtp.gmail.com", port=587)
    smtp.starttls()
    smtp.login(sender, "qlyk rwjf lvhj nnql")  # Use your App Password here
    smtp.send_message(message)
    smtp.quit()
