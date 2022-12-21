import keras
import paho.mqtt.client as mqtt
from kafka import KafkaProducer
from kafka.errors import kafka_errors
import traceback
import json
import requests
import time
import numpy as np

url = 'http://iot.rodsum.com/api/getlocationdetection'

staff_list = ['Staff_01', 'Staff_02', 'Staff_04', 'Staff_05', 'Staff_06', 'Staff_07', 'Staff_08', 'Staff_09', 'Staff_03', 'Staff_10']
bridge_list = ['vh_WIFI_Bridge_01', 'vh_WIFI_Bridge_02', 'vh_WIFI_Bridge_03', 'vh_WIFI_Bridge_04']

#load pre-trained model to do classification
model = keras.models.load_model('models/model_8')

producer=KafkaProducer(
        bootstrap_servers = ['47.243.55.194:9092'], 
        key_serializer=lambda k:json.dumps(k).encode(), 
        value_serializer=lambda v: json.dumps(v).encode()
    )

while True:

    dt = str(int(time.time()))
    df = str(int(dt)-80)
    
    p = {}
    for staff in staff_list:
        p[staff] = []

    for bridge in bridge_list:
        data_keys = {'b': bridge,'df':df,'dt':dt}
        x = requests.post(url, data=data_keys)
        data = x.json()
        
        for staff in staff_list:
            n = []  ##create a list to contain the radius data of one staff
            
            #find all the radius data under the staff and get average
            for element in data:
                if staff == element['asset_name']:
                    n.append(float(element['radius']))
            try:
                distance = round(sum(n)/len(n), 2)
                p[staff].append(distance)
            except:
                p[staff].append(0)

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
    

