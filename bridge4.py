import requests
import time

url = 'http://iot.rodsum.com/api/getlocationdetection'

n = {
    'b': 'vh_WIFI_Bridge_04',
    'df': str(int(time.time())-50),
    'dt': str(int(time.time())),
    }

d = requests.post(url, data = n)
data = d.json()

for e in data:
    print(e)

print(str(int(time.time())))