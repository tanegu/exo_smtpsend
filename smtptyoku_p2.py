import smtplib
from email.mime.text import MIMEText
 
SMTP_SERVER="****.mail.protection.outlook.com"
SMTP_PORT=25
 
MAIL_ACCOUNT_SEND="****1@****"
MAIL_ACCOUNT_RCPT="****2@****"
 
MAIL_SUBJECT="This is Subject"
MAIL_BODY="This is Body"
 
def create_message():
  msg = MIMEText(MAIL_BODY)
 
  msg['Subject'] = MAIL_SUBJECT
  msg['From'] = MAIL_ACCOUNT_SEND
  msg['To'] = MAIL_ACCOUNT_RCPT
  return msg
 
if __name__ == '__main__':
  smtp = smtplib.SMTP(SMTP_SERVER,SMTP_PORT)
  smtp.connect(SMTP_SERVER)
  smtp.ehlo()
  smtp.starttls()
  msg = create_message()
  smtp.sendmail(MAIL_ACCOUNT_SEND, MAIL_ACCOUNT_RCPT, msg.as_string())
  smtp.quit()
