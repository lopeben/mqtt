#!/usr/bin/env python3

# subscriber
import paho.mqtt.client as mqtt

client = mqtt.Client()
client.connect('192.168.55.105', 9999)

def on_connect(client, userdata, flags, rc):
    print("Connected to a broker!")
    client.subscribe("laboratory/dashboard/log")

def on_message(client, userdata, message):
    print(message.payload.decode())

while True:
    print("Subscriber")
    client.on_connect = on_connect
    client.on_message = on_message
    client.loop_forever()
    
