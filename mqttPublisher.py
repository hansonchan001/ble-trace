import paho.mqtt.client as mqtt 
from random import randrange, uniform
import time

mqttBroker ="broker.hivemq.com" 

client = mqtt.Client("Temperature_Inside")
client.connect(mqttBroker) 

while True:
    #randNumber = uniform(20.0, 21.0)
    timestamp =  str(int(time.time()))
    client.publish("test", timestamp)
    print("Just published " + timestamp + " to topic DEVBLE")
    print()
    time.sleep(2)