import paho.mqtt.client as mqtt
from pykafka import KafkaClient
import time
import random
import json
import pandas as pd
import datetime

#mqttbroker = '47.243.55.194:9092'
mqttbroker = 'iot.rodsum.com'
port = 1883
username = 'vhsoft'
password = 'soft_vh'
client_id = f'python-mqtt-{random.randint(0, 1000)}'

count = 0
m = {}
l = []

bridge = {
    "iotdata/event/vh_WIFI_Bridge_05": 'bridge_5',
    "iotdata/event/vh_WIFI_Bridge_06": 'bridge_6',
    "iotdata/event/vh_WIFI_Bridge_07": 'bridge_7',
    "iotdata/event/vh_WIFI_Bridge_08": 'bridge_8',
    
}


device = {
    #'D28A744F4C81': 'staff_10','E8ABCCA7945D': 'staff_03',
    #'C5CD4CF0E65C': 'staff_04','FF45CE6F4BD8': 'staff_06',
    #'F1B636C0956E': 'staff_08','C729D2661CE4': 'staff_02',
    #'C61777F0D7F8': 'staff_09','E21174FAF5B8': 'staff_01',
    #'E5F45951535D': 'staff_05','E05F56833E68': 'staff_07',
    
    'F2391DA65371': 'staff_20','DE1377101DC2': 'staff_13',
    'D6D75A64E478': 'staff_14','C331BACD0387': 'staff_16',
    'E305AEB86016': 'staff_15','C5D353F2F12B': 'staff_12',
    'E5A7A9941FEA': 'staff_18','FF6915C61E14': 'staff_11',
    'D49C69CBE18E': 'staff_19','C682D6D4DFFD': 'staff_17',
    
}


def on_message(client, userdata, message):

    global m, l, count
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

        if staff not in m[wb].keys():
            m[wb][staff] = []
            m[wb][staff].append(distance)
        else:
            m[wb][staff].append(distance)
        

    except:
        print("no data")

    count += 1
    if count % 100 == 0: 
        #print('delay: ', str(int(time.time())-int(data['ts'])))
        for b in m:
            for s in m[b].keys():
                a = round(sum(m[b][s])/len(m[b][s]), 2)
                m[b][s] = a


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

        for x in list(p.values()):
            l.append(x)

                
        print(p, '\n')
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

client.subscribe(topic="iotdata/event/vh_WIFI_Bridge_05")
client.subscribe(topic="iotdata/event/vh_WIFI_Bridge_06")
client.subscribe(topic="iotdata/event/vh_WIFI_Bridge_07")
client.subscribe(topic="iotdata/event/vh_WIFI_Bridge_08")

try:
    while True:
        client.on_message=on_message 
        time.sleep(0.2)

except KeyboardInterrupt:
    file_name = str(datetime.datetime.now().strftime('%m%d%H%M'))
    pd.DataFrame(l).to_excel('data_19jan/' + file_name + '_5x5_b6.xlsx', index=False)

finally:
    print('\ndata stored in excel file.')