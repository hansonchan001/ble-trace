import paho.mqtt.client as mqtt
import time
import random

#mqttbroker = '47.243.181.95'
mqttbroker = 'iot.rodsum.com'
port = 1883

topics = {
    'topic_1' : "iotdata/event/vh_WIFI_Bridge_01",
    'topic_2' : "iotdata/event/vh_WIFI_Bridge_02",
    'topic_3' : "iotdata/event/vh_WIFI_Bridge_03",
    'topic_4' : "iotdata/event/vh_WIFI_Bridge_04",
}

# generate client ID with pub prefix randomly
client_id_1 = f'python-mqtt-{random.randint(0, 1000)}'
client_id_2 = f'python-mqtt-{random.randint(0, 1000)}'
client_id_3 = f'python-mqtt-{random.randint(0, 1000)}'
client_id_4 = f'python-mqtt-{random.randint(0, 1000)}'

username = 'rswdemo'
password = 'demorsw'

device_mac = {
    'D28A744F4C81': 'staff_10',
    'E8ABCCA7945D': 'staff_03',
    'C5CD4CF0E65C': 'staff_04',
    'FF45CE6F4BD8': 'staff_06',
    'F1B636C0956E': 'staff_08',
    'C729D2661CE4': 'staff_02',
    'C61777F0D7F8': 'staff_09',
    'E21174FAF5B8': 'staff_01',
    'E5F45951535D': 'staff_05',
    'E05F56833E68': 'staff_07',

}



def on_message_2(client, userdata, message):
    income_msg = str(message.payload.decode("utf-8"))
    if 'report' in income_msg:
        mac = income_msg[income_msg.find('mac')+6:income_msg.find('mac')+18]
        #print("received message: " ,device_mac[mac], 'vh_WIFI_Bridge_02')
        if device_mac[mac] not in bridge_02:
            bridge_02.append(device_mac[mac])

def on_message_4(client, userdata, message):
    income_msg = str(message.payload.decode("utf-8"))
    if 'report' in income_msg:
        mac = income_msg[income_msg.find('mac')+6:income_msg.find('mac')+18]
        #print("received message: " ,device_mac[mac], 'vh_WIFI_Bridge_04')
        if device_mac[mac] not in bridge_04:
            bridge_04.append(device_mac[mac])

def on_message_1(client, userdata, message):
    income_msg = str(message.payload.decode("utf-8"))
    if 'report' in income_msg:
        mac = income_msg[income_msg.find('mac')+6:income_msg.find('mac')+18]
        #print("received message: " ,device_mac[mac], 'vh_WIFI_Bridge_01')
        if device_mac[mac] not in bridge_01:
            bridge_01.append(device_mac[mac])

def on_message_3(client, userdata, message):
    income_msg = str(message.payload.decode("utf-8"))
    if 'report' in income_msg:
        mac = income_msg[income_msg.find('mac')+6:income_msg.find('mac')+18]
        #print("received message: " ,device_mac[mac], 'vh_WIFI_Bridge_03')
        if device_mac[mac] not in bridge_03:
            bridge_03.append(device_mac[mac])

def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)
    

client_1 = mqtt.Client(client_id_1)
client_1.username_pw_set(username, password)
client_1.on_connect = on_connect
client_1.connect(mqttbroker, port)
client_1.loop_start()

client_2 = mqtt.Client(client_id_2)
client_2.username_pw_set(username, password)
client_2.on_connect = on_connect
client_2.connect(mqttbroker, port)
client_2.loop_start()

client_3 = mqtt.Client(client_id_3)
client_3.username_pw_set(username, password)
client_3.on_connect = on_connect
client_3.connect(mqttbroker, port)
client_3.loop_start()

client_4 = mqtt.Client(client_id_4)
client_4.username_pw_set(username, password)
client_4.on_connect = on_connect
client_4.connect(mqttbroker, port)
client_4.loop_start()

client_1.subscribe(topic=topics['topic_1'])
client_2.subscribe(topic=topics['topic_2'])
client_3.subscribe(topic=topics['topic_3'])
client_4.subscribe(topic=topics['topic_4'])

while True:
    bridge_01 = []
    bridge_02 = []
    bridge_03 = []
    bridge_04 = []
    client_1.on_message=on_message_1 
    client_2.on_message=on_message_2 
    client_3.on_message=on_message_3 
    client_4.on_message=on_message_4 
    time.sleep(5)