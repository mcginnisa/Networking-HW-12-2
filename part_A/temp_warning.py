def send_email(text):
    import socket
    import smtplib
    import os
    import sys
    from secrets import sender_address
    from secrets import sender_password
    from secrets import sender_server
    from secrets import sender_port
    from secrets import recipient_address 
    try:
        message = "From: " + sender_address + "\nTo: " + recipient_address + "\nSubject: Device Information\n\n" + text 

        server = smtplib.SMTP(sender_server, sender_port)
        server.ehlo()
        server.starttls()
        server.login(sender_address, sender_password)
        server.sendmail(sender_address, recipient_address, message)
        server.close()
        print("Message sent:\n", message)

    except:
        print("failed to send email")

def send_sms(text):
    from twilio.rest import Client
    #import numpy as np
    #generaterandomintegervalues
    #from random import seed
    #from random import randint

    account_sid='AC96bfff1c6422104b584ad9788ea2ece8'
    auth_token='3e3839be893f6f2eee47d408cf983f75'
    client=Client(account_sid,auth_token)

    #Generateamessage: x=generatearandomnumberusingrandomfunction y=somethinghere–needtofixit
    #fullMessage=text=('the big test')

    message=client.messages \
        .create(
            body=text,
            from_='+13476953808',
            to='+17075839017'
        )
    #print(message.sid)#thiswouldbesomehtinglike:85a11ef34d8ea1d9b4



def get_raspi_temp():
    import subprocess

    

    #subprocess.call("rm temp.txt", shell=True)

    subprocess.call("/opt/vc/bin/vcgencmd measure_temp | cut -f2 -d'=' > temp.txt", shell=True)


    with open('temp.txt') as textfile:
        temp = float(textfile.read().split("'")[0])

    #if temp > threshold_temp:
        #print(temp)
        #print('TOO HOT!!!')


    subprocess.call("rm temp.txt", shell=True)

    return temp


threshold_temp = 40
current_temp = get_raspi_temp()

message = "Your RasPi temperature is " + str(current_temp)
print(message)

if current_temp > threshold_temp:
    print('TOO HOT!!!!! sending email and sms') 
    send_email("warning! " + message)
    send_sms("warning! " + message)
    







