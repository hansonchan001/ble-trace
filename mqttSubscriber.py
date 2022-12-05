import paho.mqtt.client as mqtt
import time
import random

mqttbroker = 'iot.rodsum.com'
port = 1883
topic = "iotdata/event/vh_WIFI_Bridge_04"

# generate client ID with pub prefix randomly
client_id = f'python-mqtt-{random.randint(0, 1000)}'
username = 'rswdemo'
password = 'demorsw'

def on_message(client, userdata, message):
    income_msg = str(message.payload.decode("utf-8"))
    print("received message: " ,income_msg)

def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

client = mqtt.Client(client_id)
client.username_pw_set(username, password)
client.connect(mqttbroker, port)
client.on_connect = on_connect

client.loop_start()

while True:
    client.subscribe(topic=topic)
    client.on_message=on_message 
    
