import paho.mqtt.client as mqtt
from kafka import KafkaProducer
import json
import traceback
import time

producer=KafkaProducer(
        bootstrap_servers = ['47.243.55.194:9092'],
        key_serializer=lambda k:json.dumps(k).encode(), 
        value_serializer=lambda v: json.dumps(v).encode()
    )

def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
            
        else:
            print("Failed to connect, return code %d\n", rc)

        client.subscribe("iotdata/m5watch")

def on_message(client, userdata, message):

    income_msg = str(message.payload.decode("utf-8"))
    print("received message: " ,income_msg)

    future = producer.send(
            'safety',
            key='mytopic',
            value = income_msg,
            partition=0
        )

    try:
        future.get(timeout=10)
        
    except :
        traceback.format_exc()


client = mqtt.Client("mqtt-test") # client ID "mqtt-test"
client.on_connect = on_connect
client.on_message = on_message
client.username_pw_set("ble", "vhsoft")
client.connect('47.243.55.194', 1883)
client.loop_forever()  # Start networking daemon



    