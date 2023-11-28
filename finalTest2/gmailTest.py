from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import smtplib
import os

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

# Attach the image
image_path = 'path/to/your/image.jpg'
with open(image_path, 'rb') as img_file:
    img = MIMEImage(img_file.read(), name=os.path.basename(image_path))
message.attach(img)

# Send the email
smtp = smtplib.SMTP("smtp.gmail.com", port=587)
smtp.starttls()
smtp.login(sender, "qlyk rwjf lvhj nnql")  # Use your App Password here
smtp.send_message(message)
smtp.quit()
