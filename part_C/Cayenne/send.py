import cayenne.client#Cayenne MQTT Client
import time# Cayenne authentication info.This should be obtained from the Cayenne Dashboard.
import numpy as np




def get_raspi_temp():
    import subprocess

    subprocess.call("/opt/vc/bin/vcgencmd measure_temp | cut -f2 -d'=' > temp.txt", shell=True)


    with open('temp.txt') as textfile:
        temp = float(textfile.read().split("'")[0])

    subprocess.call("rm temp.txt", shell=True)

    return temp





MQTT_USERNAME  = "762048d0-13bf-11ea-8221-599f77add412"
MQTT_PASSWORD  = "f0d07c0e97b0053d60202c86f746c55cdc87cde6"
MQTT_CLIENT_ID = "2d0276d0-13c6-11ea-84bb-8f71124cfdfb"# The callback for when a message is received from Cayenne.

def on_message(message):
    print("message received: "+ str(message))# If there is an error processing the message return an error string, otherwise return nothing.

client = cayenne.client.CayenneMQTTClient()
client.on_message = on_message
client.begin(MQTT_USERNAME, MQTT_PASSWORD, MQTT_CLIENT_ID)

# For a secure connection use port 8883 when calling client.begin:
# client.begin(MQTT_USERNAME, MQTT_PASSWORD, MQTT_CLIENT_ID, port=8883)

i=0
timestamp = 0
while True:
    client.loop()
    if (time.time() > timestamp + 4):
        client.virtualWrite(1, np.random.randint(1,100), "number", "rand")
        client.virtualWrite(2, get_raspi_temp(), "temp", "c")
        timestamp = time.time()
        i = i+1
