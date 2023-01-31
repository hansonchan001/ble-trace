import paho.mqtt.client as mqtt
import time

mqttbroker = 'aiotrak.rec-gt.com'
port = 1880
username = 'tswh'
password = '1Wo=[6vA0m'
client = mqtt.Client("tracy_safety_bell")
 
topic="rgt/868474041800804/out"

def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)


def publish():
    
    while True:
        msg = 'D3:1'
        
        result = client.publish(topic, msg)
        
        status = result[0]
        if status == 0:
            print(f"Send `{msg}` to topic `{topic}`")
        else:
            print(f"Failed to send message to topic {topic}")
        time.sleep(1)
        
client.on_connect=on_connect
client.connect(mqttbroker, port=1880)
client.publish(topic=topic)

publish()