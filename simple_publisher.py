#!/usr/bin/env python3

# publisher
import time
import json
import paho.mqtt.client as mqtt
from datetime import datetime

client = mqtt.Client()
client.connect('192.168.55.105', 9999)


while True:
    print("Publisher")
  
    payload={}   
    payload['timestamp'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    data = json.dumps(payload)
    
    client.publish("laboratory/dashboard/log", data)
    
    time.sleep(60)
   
    
    