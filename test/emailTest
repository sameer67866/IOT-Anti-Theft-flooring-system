import smtplib

smtp_server = 'smtp.gmail.com'
smtp_port = 587
smtp_username = 'cyber.talha0@gmail.com'
smtp_password = 'Spike90122pro1'

from_email = 'cyber.talha0@gmail.com'
to_email = 'musabtree@hotmail.com'
subject = 'Hello World!'
body = 'This is a test email.'

message = f'Subject: {subject}\n\n{body}'

with smtplib.SMTP(smtp_server, smtp_port) as smtp:
    smtp.starttls()
    smtp.login(smtp_username, smtp_password)
    smtp.sendmail(from_email, to_email, message)
