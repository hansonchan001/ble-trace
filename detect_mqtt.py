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
username = 'rswdemo'
password = 'demorsw'
client_id = f'python-mqtt-{random.randint(0, 1000)}'

count = 0
m = {}

bridge = {
    "iotdata/event/vh_WIFI_Bridge_01": 'bridge_1',
    "iotdata/event/vh_WIFI_Bridge_02": 'bridge_2',
    "iotdata/event/vh_WIFI_Bridge_03": 'bridge_3',
    "iotdata/event/vh_WIFI_Bridge_04": 'bridge_4',
}

device = {
    'D28A744F4C81': 'staff_10','E8ABCCA7945D': 'staff_03',
    'C5CD4CF0E65C': 'staff_04','FF45CE6F4BD8': 'staff_06',
    'F1B636C0956E': 'staff_08','C729D2661CE4': 'staff_02',
    'C61777F0D7F8': 'staff_09','E21174FAF5B8': 'staff_01',
    'E5F45951535D': 'staff_05','E05F56833E68': 'staff_07',
}

#load pre-trained model to do classification
model = keras.models.load_model('models/model_8')

producer=KafkaProducer(
        bootstrap_servers = ['47.243.55.194:9092'], 
        key_serializer=lambda k:json.dumps(k).encode(), 
        value_serializer=lambda v: json.dumps(v).encode()
    )

def on_message(client, userdata, message):

    global m, l, count
    income_msg = str(message.payload.decode("utf-8"))
    wb = bridge[str(message.topic)]

    try:
        data = json.loads(income_msg)
        rssi1m = data['ibeacon']['rssi1m']
        rssi = data['rssi']
        N = 4 #low strength
        distance = round(10**((int(rssi1m)-int(rssi))/(10*N)), 2)
        
        if wb not in m.keys():
            m[wb] = {}

        staff = device[data['mac']]

        if staff not in m[wb].keys():
            m[wb][staff] = []
            m[wb][staff].append(distance)
        else:
            m[wb][staff].append(distance)
        

    except:
        print("no data")

    count += 1
    if count % 150 == 0: 
        print('delay: ', str(int(time.time())-int(data['ts'])))
        for b in m:
            for s in m[b].keys():
                a = round(sum(m[b][s])/len(m[b][s]), 2)
                m[b][s] = a


        m_sorted = dict(sorted(m.items(), key=lambda x:x[0]))

        k = {}
        for i in m_sorted:
            a = dict(sorted(m[i].items(), key=lambda x:x[0]))
            k[i] = a
        print(k, '\n')
        
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
                
        print(p, '\n')
        count = 0
        m = {}

        in_zone = []

        for staff, positions in p.items():
            result = model.predict(np.array([positions]))
            if result > 0.5:
                in_zone.append(staff)


        ######  send MQ message to Kafka    ########

        message =  {
            "ZoneCode": "HSK1A01",
            "TotalNumber": str(len(in_zone)),
            "TagList": in_zone,
            "Timestamp": str(int(time.time()))
        }

        future = producer.send(
            'DEVBLE',
            key='mytopic',
            value = message,
            partition=0
        )

        print("send {}".format(str(message)))

        try:
            future.get(timeout=10)
        except :
            traceback.format_exc()

        #### finsihed sending MQ message to Kafka #######
    

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

client.subscribe(topic="iotdata/event/vh_WIFI_Bridge_01")
client.subscribe(topic="iotdata/event/vh_WIFI_Bridge_02")
client.subscribe(topic="iotdata/event/vh_WIFI_Bridge_03")
client.subscribe(topic="iotdata/event/vh_WIFI_Bridge_04")

while True:

    client.on_message=on_message  

    

