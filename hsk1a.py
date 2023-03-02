import keras
import paho.mqtt.client as mqtt
from kafka import KafkaProducer
from kafka.errors import kafka_errors
import traceback
import json
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
reportNumber = 50
m = {}

bridge = {
    "iotdata/event/vh_WIFI_Bridge_10": 'bridge_10',
    "iotdata/event/vh_WIFI_Bridge_09": 'bridge_9',
    "iotdata/event/vh_WIFI_Bridge_03": 'bridge_3',
    "iotdata/event/vh_WIFI_Bridge_04": 'bridge_4',
}

device = {
    'D28A744F4C81': 'staff_10','E8ABCCA7945D': 'staff_03',
    'C5CD4CF0E65C': 'staff_04','FF45CE6F4BD8': 'staff_06',
    'F1B636C0956E': 'staff_08','C729D2661CE4': 'staff_02',
    'C61777F0D7F8': 'staff_09','E21174FAF5B8': 'staff_01',
    'E5F45951535D': 'staff_05','E05F56833E68': 'staff_07',
    
    #'F2391DA65371': 'staff_20','DE1377101DC2': 'staff_13',
    #'D6D75A64E478': 'staff_14','C331BACD0387': 'staff_16',
    #'E305AEB86016': 'staff_15','C5D353F2F12B': 'staff_12',
    #'E5A7A9941FEA': 'staff_18','FF6915C61E14': 'staff_11',
    #'D49C69CBE18E': 'staff_19','C682D6D4DFFD': 'staff_17',
    
}

#load pre-trained model to do classification
model = keras.models.load_model('models/model_03021050')

producer=KafkaProducer(
        bootstrap_servers = ['47.243.55.194:9092'], 
        key_serializer=lambda k:json.dumps(k).encode(), 
        value_serializer=lambda v: json.dumps(v).encode()
    )

for wb in bridge.values():
        m[wb] = {}

def on_message(client, userdata, message):

    global m, l, count, reportNumber
    income_msg = str(message.payload.decode("ISO-8859-1"))
    wb = bridge[str(message.topic)]

    try:
        data = json.loads(income_msg)
        rssi1m = data['ibeacon']['rssi1m']
        rssi = data['rssi']
        N = 4 #low strength
        distance = round(10**((int(rssi1m)-int(rssi))/(10*N)), 2)
        
        #if wb not in m.keys():
        #    m[wb] = {}

        staff = device[data['mac']]

        if staff not in m[wb].keys():
            m[wb][staff] = []
            m[wb][staff].append(distance)
        else:
            m[wb][staff].append(distance)
        
        #print(m)

    except:
        #filter out events besides "detect"
        #print("not detect event")
        pass

    count += 1
    try:
        if count % reportNumber == 0: 
            try:
                for b in m:
                    for s in m[b].keys():
                        try:
                            a = round(sum(m[b][s])/len(m[b][s]), 2)
                            m[b][s] = a
                        except:
                            pass
            except:
                pass

            m_sorted = dict(sorted(m.items(), key=lambda x:x[0]))
            k = {}
            for i in m_sorted:
                a = dict(sorted(m[i].items(), key=lambda x:x[0]))
                k[i] = a

            p={}
            for bg in k:
                for staff in k[bg]:
                    if staff not in p:
                        p[staff] = []

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
            reportNumber = 10+len(list(m[list(bridge.values())[0]]))*8
            for wb in bridge.values():
                m[wb] = {}
        
            ######  send MQ message to Kafka    ########

            message =  {
                "ZoneCode": "HSK1A01",
                "TotalNumber": str(len(in_zone)),
                "TagList": in_zone,
                "Timestamp": int(time.time())
            }

            future = producer.send(
                'DEVBLE',
                key='mytopic',   
                value = message,
                partition=0
            )

            print("send {}\n".format(str(message)))

            try:
                future.get(timeout=10)
            except :
                traceback.format_exc()
            
            #### finsihed sending MQ message to Kafka #######
    
    except:
        pass
    
    

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

client.subscribe(topic="iotdata/event/vh_WIFI_Bridge_10")
client.subscribe(topic="iotdata/event/vh_WIFI_Bridge_09")
client.subscribe(topic="iotdata/event/vh_WIFI_Bridge_03")
client.subscribe(topic="iotdata/event/vh_WIFI_Bridge_04")



while True:
    client.on_message=on_message
    time.sleep(0.2)
    

