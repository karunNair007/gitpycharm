from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib,ssl


kk=MIMEMultipart()
kk['From']='karun@agaramtech.com'
kk['To']='karun@agaramtech.com'
kk['CC']='karun@agaramtech.com'
kk['Subject']='test mail'
content="""
helooooo Guyz this is automation of email concept
"""
kk.attach(MIMEText(content,'plain'))
filepath="D:\check\Excel\kk.xlsx"
filereadbinary=open(filepath,"rb")
payload=MIMEBase("application","octate-stream")
payload.set_payload(filereadbinary.read())
encoders.encode_base64(payload)
kk.attach(payload)

kk.attach(MIMEText(content,'plain'))
filepath="D:\check\Excel\kk1.xlsx"
filereadbinary=open(filepath,"rb")
payload=MIMEBase("application","octate-stream")
payload.set_payload(filereadbinary.read())
encoders.encode_base64(payload)
kk.attach(payload)

server=smtplib.SMTP("smtp.gmail.com",587)
server.starttls(context=ssl.create_default_context())
server.login("karun@agaramtech.com","Krishna007")
server.sendmail("karun@agaramtech.com","karun@agaramtech.com",str(kk))
server.quit()
