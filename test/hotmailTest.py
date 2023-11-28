from email.message import EmailMessage
import smtplib

sender = "musabtree@hotmail.com"
recipient = "cyber.talha0@gmail.com"
message = "Hello world!"

email = EmailMessage()
email["From"] = sender
email["To"] = recipient
email["Subject"] = "Test Email"
email.set_content(message)

smtp = smtplib.SMTP("smtp-mail.outlook.com", port=587)
smtp.starttls()
smtp.login(sender, "sadderthanlife567")
smtp.sendmail(sender, recipient, email.as_string())
smtp.quit()
