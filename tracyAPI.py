import requests
import datetime
import time
import json

url = 'http://iot.rodsum.com/api/getlocationdetection'

window_in_seconds = 120

dt = str(int(time.time()))
df = str(int(dt)-window_in_seconds)

beacon_list = ['Staff_03', 'Staff_04', 'Staff_06', 'Staff_08', 'Staff_10', 'Staff_01', 'Staff_02', 'Staff_05', 'Staff_07', 'Staff_09']
bridge_list = ['vh_WIFI_Bridge_01', 'vh_WIFI_Bridge_02', 'vh_WIFI_Bridge_03', 'vh_WIFI_Bridge_04']

n = {'b':bridge_list[2],'df' :df,'dt': dt}
d = requests.post(url, data = n)
data = d.json()

m=[]
for e in data:
    m.append(e['datetime'])
m.sort()

print('now: ', str(int(time.time())))
print('last timestamp: ', m[-1])
print('delay: ', str(int(time.time())-int(m[-1])))




