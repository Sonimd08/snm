import smtplib
from email.message import EmailMessage
def sendmail(to,subject,body):
    server=smtplib.SMTP_SSL('smtp.gmail.com',465)
    server.login('mohammadrajia8@gmail.com','etyk tceb wirh enfb')
    msg=EmailMessage()
    msg['From']='mohammadrajia8@gmail.com'
    msg['To']=to
    msg['SUBJECT']=subject
    msg.set_content(body)
    server.send_message(msg)
    server.close()