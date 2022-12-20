import paho.mqtt.client as mqtt
from pykafka import KafkaClient
import time
import random
import json

#mqttbroker = '47.243.55.194:9092'
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

def on_message(client, userdata, message):

    global m, count
    income_msg = str(message.payload.decode("utf-8"))
    wb = bridge[str(message.topic)]
    #print(income_msg)
    #print(wb)

    try:
        data = json.loads(income_msg)
        rssi1m = data['ibeacon']['rssi1m']
        rssi = data['rssi']
        N = 4 #low strength
        distance = round(10**((int(rssi1m)-int(rssi))/(10*N)), 2)
        
        if wb not in m.keys():
            m[wb] = {}

        staff = device[data['mac']]
        #print(m)
        #print(staff)
        #print(distance)
 
        k = {staff:[distance]}

        if staff not in m[wb].keys():
            m[wb][staff] = []
            m[wb][staff].append(distance)
        else:
            m[wb][staff].append(distance)


    except:
        print("no data")

    count += 1
    if count % 50 == 0: 
        #m_sorted = dict(sorted(m.items(), key=lambda x:x[0]))
        print(int(time.time())-int(data['ts']))
        for b in m:
            for s in m[b].keys():
                a = round(sum(m[b][s])/len(m[b][s]), 2)
                m[b][s] = a
        for b in m:
            print(b)
            print(m[b])
        count = 0
        m = {}

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
    