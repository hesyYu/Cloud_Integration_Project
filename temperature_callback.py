#!/usr/bin/env python
# -*- coding: utf-8 -*-
import paho.mqtt.client as mqtt
import time, threading, ssl, random
from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_temperature_v2 import BrickletTemperatureV2
# client, user and device details
serverUrl   = "hogoowatt.eu-latest.cumulocity.com"
port        = 1883
clientId    = "10000000efcabae1"
device_name = "temperature sensor_hyesu"
agent_model = "TF Temp Sensor"
tenant      = "hogoowatt"
username    = "hogoowatt@naver.com"
password    = "Dkagh11."
receivedMessages = []
#for getTemp()
HOST = "localhost"
PORT = 4223
UID = "HaY"

ipcon = IPConnection()
t = BrickletTemperatureV2(UID, ipcon)
ipcon.connect(HOST, PORT)

# display all incoming messages
def on_message(client, userdata, message):
    print("Received operation " + str(message.payload))
    if (message.payload.startswith("510")):
        print("Simulating device restart...")
        publish("s/us", "501,c8y_Restart");
        print("...restarting...")
        time.sleep(1)
        publish("s/us", "503,c8y_Restart");
        print("...done...")
# send temperature measurement
def sendMeasurements():
    try:
        tf_temp = str(t.get_temperature()/100.0)
        print("Sending temperature measurement : [mqtt channel|msg] " + "s/us" + "|211," + tf_temp)
        publish("s/us", "211," + tf_temp)
        thread = threading.Timer(7, sendMeasurements)
        thread.daemon=True
        thread.start()
        while True: time.sleep(100)
    except (KeyboardInterrupt, SystemExit):
        print 'Received keyboard interrupt, quitting ...'

# publish a message
def publish(topic, message, waitForAck = False):
    mid = client.publish(topic, message, 2)[1]
    if (waitForAck):
        while mid not in receivedMessages:
            time.sleep(0.25)
def on_publish(client, userdata, mid):
    receivedMessages.append(mid)

# connect the client to Cumulocity and register a device
client = mqtt.Client(clientId)
client.username_pw_set(tenant + "/" + username, password)
client.on_message = on_message
client.on_publish = on_publish
client.connect(serverUrl, port)
client.loop_start()

publish("s/us", "100," + device_name + ",c8y_MQTTDevice", True)
print("s/us", "100," + device_name + ",c8y_MQTTDevice")
publish("s/us", "110," + clientId + "," + agent_model + ",Rev1.0")
print("s/us", "110," + clientId + "," + agent_model + ",Rev1.0")
publish("s/us", "114,c8y_Restart")
print("s/us", "114,c8y_Restart")

print "Device registered successfully!"

client.subscribe("s/ds")

sendMeasurements()


