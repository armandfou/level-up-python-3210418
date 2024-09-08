import smtplib

# Import the email modules we'll need
from email.message import EmailMessage

# Open the plain text file whose name is in textfile for reading.
def send_mail(receiverAdress, subject, content):
  msg = EmailMessage()
  msg.set_content(content)
  sender = "armand.fouquiau@orange.fr"
  msg['Subject'] = subject
  msg['From'] = sender
  msg['To'] = receiverAdress
  with smtplib.SMTP_SSL('smtp.orange.fr', 465) as smtp_server:
    smtp_server.login(sender, "")
    smtp_server.sendmail(sender,receiverAdress, msg.as_string())



send_mail('armand.fouquiau@orange.fr', 'Notification', 'Everything is awesome!')