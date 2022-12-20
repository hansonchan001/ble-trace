import keras
import paho.mqtt.client as mqtt
from kafka import KafkaProducer
from kafka.errors import kafka_errors
import traceback
import json
import requests
import time


url = 'http://iot.rodsum.com/api/getlocationdetection'

staff_list = ['Staff_03', 'Staff_04', 'Staff_06', 'Staff_08', 'Staff_10', 'Staff_01', 'Staff_02', 'Staff_05', 'Staff_07', 'Staff_09']
bridge_list = ['vh_WIFI_Bridge_01', 'vh_WIFI_Bridge_02', 'vh_WIFI_Bridge_03', 'vh_WIFI_Bridge_04']

model = keras.models.load_model('models/model_8')

while True:
    dt = str(int(time.time()))
    df = str(int(dt)-70)
    
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

    #for keys, values in p.items():
     #   print(keys, str(values))
    in_zone = []
    for staff, positions in p.items():
        result = model.predict(positions)
        if result > 0.5:
            in_zone.append(staff)
            print(staff, ' is  within the zone')
        else:
            print(staff, ' is out of the zone')

    ######  send MQ message to Kafka    ########
    producer=KafkaProducer(
        bootstrap_servers = ['47.243.55.194:9092'], 
        key_serializer=lambda k:json.dumps(k).encode(), 
        value_serializer=lambda v: json.dumps(v).encode()
    )
    
    example =  {
        "ZoneCode": "HSK1A01",
        "TotalNumber": "6",
        "TagList":
        [
            "staff_01",
            "staff_02",
            "staff_03",
        ],
        "Timestamp": "1669252729"
    }
    
    future = producer.send(
        'test',
        key='mytopic',
        value = example,
        partition=0
    )
    
    print("send {}".format(str(example)))
    
    try:
        future.get(timeout=10)
    except kafka_errors:
        traceback.format_exc()
    #### finsihed sending MQ message to Kafka #######
    

