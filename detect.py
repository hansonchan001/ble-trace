import keras
import paho.mqtt.client as mqtt
from kafka import KafkaProducer
from kafka.errors import kafka_errors
import traceback
import json

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

