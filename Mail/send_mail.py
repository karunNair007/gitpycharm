import smtplib,ssl


ssl_context=ssl.create_default_context()
server=smtplib.SMTP("smtp.gmail.com",587)
server.starttls(context=ssl_context)
server.login("karun@agaramtech.com","Krishna007")
server.sendmail("karun@agaramtech.com","karun@agaramtech.com","test mail")
server.quit()