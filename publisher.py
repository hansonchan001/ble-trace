import paho.mqtt.client as mqtt
from kafka import KafkaProducer
import json
import traceback
import time

mqttBroker ="47.243.55.194"
username = "ble"
password = "vhsoft"
client = mqtt.Client("tracy_safety_bell")
client.username_pw_set(username, password)

client.connect(mqttBroker, port=1883) 
topic="iotdata/m5watch"
client.publish(topic="iotdata/m5watch")

def publish():
    
    while True:
        msg = str({'hi':9})
        
        result = client.publish(topic, msg)
        
        status = result[0]
        if status == 0:
            print(f"Send `{msg}` to topic `{topic}`")
        else:
            print(f"Failed to send message to topic {topic}")
        time.sleep(1)
        

publish()
