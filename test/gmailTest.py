from email.message import EmailMessage
import smtplib

recipient = "musabtree@hotmail.com"
sender = "cyber.talha0@gmail.com"
message = "Hello world!"

email = EmailMessage()
email["From"] = sender
email["To"] = recipient
email["Subject"] = "Test Email"
email.set_content(message)

smtp = smtplib.SMTP("smtp.gmail.com", port=587)
smtp.starttls()
smtp.login(sender, "qlyk rwjf lvhj nnql")
smtp.sendmail(sender, recipient, email.as_string())
smtp.quit()
