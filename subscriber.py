import paho.mqtt.client as mqtt
import time
import random
import json
import numpy as np

mqttbroker = 'iot.rodsum.com'
port = 1883
username = 'vhsoft'
password = 'soft_vh'
client_id = f'python-mqtt-{random.randint(0, 1000)}'

count = 0
m = []

topics = {
    'topic_1' : "iotdata/event/vh_WIFI_Bridge_01",
    'topic_2' : "iotdata/event/vh_WIFI_Bridge_02",
    'topic_3' : "iotdata/event/vh_WIFI_Bridge_03",
    'topic_4' : "iotdata/event/vh_WIFI_Bridge_04",
    'topic_10' : "iotdata/event/vh_WIFI_Bridge_10",
}

# generate client ID with pub prefix randomly
client_id = f'python-mqtt-{random.randint(0, 1000)}'


device_mac = {
    'D28A744F4C81': 'staff_10','E8ABCCA7945D': 'staff_03',
    'C5CD4CF0E65C': 'staff_04','FF45CE6F4BD8': 'staff_06',
    'F1B636C0956E': 'staff_08','C729D2661CE4': 'staff_02',
    'C61777F0D7F8': 'staff_09','E21174FAF5B8': 'staff_01',
    'E5F45951535D': 'staff_05','E05F56833E68': 'staff_07',
    'D958E9F155DD': 'staff_21'
}

def on_message(client, userdata, message):
    global m
    income_msg = str(message.payload.decode("utf-8"))
    #topic = str(message.topic)
    data = json.loads(income_msg)
    #print(income_msg)
    try:
        m.append(data['rssi'])
        print(data['rssi'],np.std(m))
    except:
        pass

def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

#get data with only one client
client = mqtt.Client(client_id)
client.username_pw_set(username, password)
client.on_connect = on_connect
client.connect(mqttbroker, port)
client.loop_start()
client.subscribe(topic=topics['topic_10'])


while True:
    client.on_message=on_message 
    time.sleep(0.1)