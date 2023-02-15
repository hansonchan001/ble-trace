import requests
import time
import sys

url = 'http://iot.rodsum.com/api/getlocationdetection'


beacon_list = ['Staff_03', 'Staff_04', 'Staff_06', 'Staff_08', 'Staff_10', 'Staff_01', 'Staff_02', 'Staff_05', 'Staff_07', 'Staff_09']
bridge_list = ['vh_WIFI_Bridge_01', 'vh_WIFI_Bridge_02', 'vh_WIFI_Bridge_03', 'vh_WIFI_Bridge_04', 'vh_WIFI_Bridge_07']


n = {
    'b': bridge_list[int(sys.argv[1])-1],
    'df': str(int(time.time())-100),
    'dt': str(int(time.time())),
    }

d = requests.post(url, data = n)
data = d.json()

print(n)

for e in data:
    print(e)

print(str(int(time.time())))
