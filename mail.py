import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_otp_mail(email,otp):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login("likhithshankartpt@gmail.com","likhith@tpt")

    sender_email = "likhithshankartpt@gmail.com"
    receiver_email = email

    message = MIMEMultipart("alternative")
    message["Subject"] = "OTP"
    message["From"] = sender_email
    message["To"] = receiver_email
    text = """Hii There 
Your required otp is:{0}""".format(otp)
    part1 = MIMEText(text, "plain")
    message.attach(part1)
    server.sendmail(sender_email, receiver_email, message.as_string())
    server.quit()
