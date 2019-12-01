
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


send_sms('YOU PRESSED THE BUTTON!')
