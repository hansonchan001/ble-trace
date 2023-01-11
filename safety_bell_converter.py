import paho.mqtt.client as mqtt
from kafka import KafkaProducer
import json
import traceback
import time

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
        #time.sleep(3)
    except :
        traceback.format_exc()

#mqttBroker ="broker.hivemq.com"ZE
mqttBroker ="47.243.55.194"
username = "ble"
password = "vhsoft"
client = mqtt.Client("tracy_safety_bell")
client.username_pw_set(username, password)
client.connect(mqttBroker, port=1883) 
client.loop_start()
client.subscribe(topic="iotdata/m5watch")

producer=KafkaProducer(
        bootstrap_servers = ['47.243.55.194:9092'],
        key_serializer=lambda k:json.dumps(k).encode(), 
        value_serializer=lambda v: json.dumps(v).encode()
    )

while True:
    client.on_message=on_message 
    