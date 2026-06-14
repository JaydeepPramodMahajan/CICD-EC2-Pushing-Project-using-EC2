import requests

def check_website(url):
    try:
        response=requests.get(url)
        print(response.status_code)
        if response.status_code==200:
            return True
        else:
            return False
        
    except:
        return False
#--------------------------------------------------------------
import smtplib
from email.mime.text import MIMEText#To send in the text part
from email.mime.multipart import MIMEMultipart #TO the send the attcahent
from dotenv import load_dotenv#TO add the Enviromental variabke in OS
import os

load_dotenv()
def send_mail(Sender_email,password,receiver_mail,Subject,body):
    message=MIMEMultipart()
    message['From'] = Sender_email
    message['To'] = receiver_mail
    message['Subject']=Subject

    message.attach(MIMEText(body,'plain'))
    try:
        server= smtplib.SMTP('smtp.gmail.com',587)
        server.starttls()#Start TLS connection
        server.login(Sender_email,password)
        text=message.as_string()
        server.sendmail(Sender_email,receiver_mail,text)
        print("Sended Succesfully")
    except:
        print("Failed")
    
url=("https://fakesstoreapi.com/")
if not check_website(url):
    Sender_email=os.getenv("Sender_Mail")
    print(Sender_email)
    Subject="About Website"
    body=os.getenv("Body")
    receiver_mail=os.getenv("Receiver_Mail")
    password=os.getenv("Sender_Password")
    send_mail(Sender_email,password,receiver_mail,Subject,body)
    print("Sended Succesfully")
else:
    print("website is up")