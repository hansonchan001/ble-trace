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

count = 0
m = {}

topics = {
    'topic_1' : "iotdata/event/vh_WIFI_Bridge_01",
    'topic_2' : "iotdata/event/vh_WIFI_Bridge_02",
    'topic_3' : "iotdata/event/vh_WIFI_Bridge_03",
    'topic_4' : "iotdata/event/vh_WIFI_Bridge_04",
}

# generate client ID with pub prefix randomly
client_id = f'python-mqtt-{random.randint(0, 1000)}'


device_mac = {
    'D28A744F4C81': 'staff_10','E8ABCCA7945D': 'staff_03',
    'C5CD4CF0E65C': 'staff_04','FF45CE6F4BD8': 'staff_06',
    'F1B636C0956E': 'staff_08','C729D2661CE4': 'staff_02',
    'C61777F0D7F8': 'staff_09','E21174FAF5B8': 'staff_01',
    'E5F45951535D': 'staff_05','E05F56833E68': 'staff_07',
}

def on_message(client, userdata, message):

    global m, count
    
    income_msg = str(message.payload.decode("utf-8"))
    topic = str(message.topic)
    data = json.loads(income_msg)

    try:
        rssi1m = data['ibeacon']['rssi1m']
        rssi = data['rssi']
        N = 4 #low strength
        distance = round(10**((int(rssi1m)-int(rssi))/(10*N)), 2)

        if device_mac[data['mac']] not in m:
            m[device_mac[data['mac']]] = []
            if topic == topics['topic_1']:
                print(data)
            m[device_mac[data['mac']]].append(distance)
            
        else:
            m[device_mac[data['mac']]].append(distance)

    except:
        print(" ")


    example = {
                "ZoneCode": "HSK1A01",
                "TotalNumber": "6",
                "TagList":[
                                "staff_01",
                                "staff_02",
                                "staff_03",
                        ],
                "Timestamp": "1669252729"
            }

    count += 1
    if count % 50 == 0:
        for x in m:
           m[x] = round(sum(m[x])/len(m[x]), 2)
        m_sorted = dict(sorted(m.items(), key=lambda x:x[0]))
        print(int(time.time())-int(data['ts']))
        print(m)
        count = 0
        m = {}

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

client.subscribe(topic=topics['topic_1'])
client.subscribe(topic=topics['topic_2'])
client.subscribe(topic=topics['topic_3'])
client.subscribe(topic=topics['topic_4'])

while True:
    client.on_message=on_message 
    