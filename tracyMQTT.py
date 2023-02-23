import keras
import paho.mqtt.client as mqtt
from kafka import KafkaProducer
from kafka.errors import kafka_errors
import traceback
import json
import requests
import time
import numpy as np
import random

#mqtt client details
mqttbroker = 'iot.rodsum.com'
port = 1883
username = 'vhsoft'
password = 'soft_vh'
client_id = f'python-mqtt-{random.randint(0, 1000)}'

count = 0
m = {}

bridge = {
    "iotdata/event/vh_WIFI_Bridge_05": 'bridge_5',
    "iotdata/event/vh_WIFI_Bridge_06": 'bridge_6',
    "iotdata/event/vh_WIFI_Bridge_07": 'bridge_7',
    "iotdata/event/vh_WIFI_Bridge_08": 'bridge_8',
}

device = {
    'F2391DA65371': 'staff_20','DE1377101DC2': 'staff_13',
    'D6D75A64E478': 'staff_14','C331BACD0387': 'staff_16',
    'E305AEB86016': 'staff_15','C5D353F2F12B': 'staff_12',
    'E5A7A9941FEA': 'staff_18','FF6915C61E14': 'staff_11',
    'D49C69CBE18E': 'staff_19','C682D6D4DFFD': 'staff_17',
}

#load pre-trained model to do classification
model = keras.models.load_model('models/model_0223_0.91')

for wb in bridge.values():
        m[wb] = {}

def on_message(client, userdata, message):

    global m, l, count
    income_msg = str(message.payload.decode("ISO-8859-1"))
    wb = bridge[str(message.topic)]

    try:
        data = json.loads(income_msg)
        rssi1m = data['ibeacon']['rssi1m']
        rssi = data['rssi']
        N = 4 #low strength
        distance = round(10**((int(rssi1m)-int(rssi))/(10*N)), 2)

        staff = device[data['mac']]

        if staff not in m[wb].keys():
            m[wb][staff] = []
            m[wb][staff].append(distance)
        else:
            m[wb][staff].append(distance)

    except:
        pass
    
    #this line decide the window time by numebr of staff
    #reportNumber = len(list(m[list(bridge.values())[0]]))*30
    reportNumber = 100

    count += 1
    if count % reportNumber == 0: 

        #print(m)
        for b in m:
            for s in m[b].keys():
                try:
                    a = round(sum(m[b][s])/len(m[b][s]), 2)
                    m[b][s] = a
                except:
                    pass

        m_sorted = dict(sorted(m.items(), key=lambda x:x[0]))

        k = {}
        for i in m_sorted:
            a = dict(sorted(m[i].items(), key=lambda x:x[0]))
            k[i] = a
        #print(k, '\n')
        
        p={}
        for bg in k:
            for staff in k[bg]:
                if staff not in p:
                    p[staff] = []
                
                #p[staff].append(k[bg][staff])
        
        for bg in k:
            for staff in p:
                try:
                    p[staff].append(k[bg][staff])
                except:
                    p[staff].append(0)

        p = dict(sorted(p.items()))

        for staff, positions in p.items():
            print(staff, positions)
        
        in_zone = []
        for staff, positions in p.items():
            if 0 in positions:
                continue
            else:
                try:
                    result = model.predict(np.array([positions]))
                    if result > 0.5:
                        in_zone.append(staff)
                except:
                    print("cannot input to model")
        print(len(in_zone), in_zone)

        count = 0
        for wb in bridge.values():
            m[wb] = {}
        #print(m)
    
    

def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

client = mqtt.Client(client_id)
client.username_pw_set(username, password)
client.on_connect = on_connect
client.connect(mqttbroker, port)
client.loop_start()

client.subscribe(topic="iotdata/event/vh_WIFI_Bridge_05")
client.subscribe(topic="iotdata/event/vh_WIFI_Bridge_06")
client.subscribe(topic="iotdata/event/vh_WIFI_Bridge_07")
client.subscribe(topic="iotdata/event/vh_WIFI_Bridge_08")



while True:
    client.on_message=on_message
    time.sleep(0.2)
    

