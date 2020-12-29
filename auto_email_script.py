import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from datetime import datetime
import time

date = time.strftime("%Y%m%d")
email_user = 'example@gmail.com'
email_password = 'password'
email_send = 'example1@gmail.com'
email_send1 = 'example2@gmail.com'
email_send2 = 'example3@gmail.com'
subject = date+' Environmental Data'

msg = MIMEMultipart()
msg['From'] = email_user
msg['To'] = email_send
msg['Subject'] = subject
filename=date+'.png'
attachment  =open(filename,'rb')

part = MIMEBase('application','octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition',"attachment; filename= "+filename)

msg.attach(part)
text = msg.as_string()
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(email_user,email_password)
server.sendmail(email_user,email_send,text)
server.sendmail(email_user,email_send1,text)
server.sendmail(email_user,email_send2,text)
server.quit()