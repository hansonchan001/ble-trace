import paho.mqtt.client as mqtt
from pykafka import KafkaClient
import time
import json

timeStamp = str(int(time.time()))
#mqtt_broker = "47.243.55.194"
mqttBroker = "broker.hivemq.com"
port = 9092
mqtt_client = mqtt.Client("BridgeMQTT2Kafka")
mqtt_client.connect(mqttBroker)

topic = "DEVBLE"
kafka_client = KafkaClient(hosts="47.243.55.194:9092")
kafka_topic = kafka_client.topics[topic]
kafka_producer = kafka_topic.get_sync_producer()



def on_message(client, userdata, message):
    
    example =  { 
            "TotalNumber": "6",
            "TagList":
            [
                "staff_01",
                "staff_02",
                "staff_03",
            ],
            "Timestamp": timeStamp,
            }

    msg_payload = str(message.payload)
    print("Received MQTT message: ", msg_payload)
    kafka_producer.produce(msg_payload.encode('ascii'))
    example_json = json.dumps(example)
    print("KAFKA: Just published " + example_json + " to topic DEVBLE")

    

mqtt_client.loop_start()
mqtt_client.subscribe("test")
mqtt_client.on_message = on_message
time.sleep(3)
print(timeStamp)
#mqtt_client.loop_end()