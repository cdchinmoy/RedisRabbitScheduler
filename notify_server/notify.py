from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import email.message
import smtplib

# create message object instance
msg = MIMEMultipart()
password = "Chinmoy123!@#"

def send_mail(data):
    receiver_list = data['receiver_list']
    print(data)
    msg = email.message.Message()
    msg['From'] = "chinmoy.ogmait@gmail.com"
    # msg['To'] = receiver_list
    msg['Subject'] = data['subject']

    body = data['mail_body']
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(body)
    #create server
    server = smtplib.SMTP('smtp.gmail.com: 587')
    
    server.starttls()
    
    # Login Credentials for sending the mail
    server.login(msg['From'], password)
    
    # send the message via the server.
    server.sendmail(msg['From'], receiver_list, msg.as_string())
    
    server.quit()
    
    print("successfully sent email")