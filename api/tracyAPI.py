import requests
import datetime
import time
import json

url = 'http://iot.rodsum.com/api/getlocationdetection'

window_in_seconds = 120

dt = str(int(time.time()))
df = str(int(dt)-window_in_seconds)

beacon_list = ['Staff_11', 'Staff_14', 'Staff_16', 'Staff_18', 'Staff_12', 'Staff_13', 'Staff_17', 'Staff_15', 'Staff_19', 'Staff_20', 'Staff_21']
bridge_list = ['vh_WIFI_Bridge_05', 'vh_WIFI_Bridge_06', 'vh_WIFI_Bridge_07', 'vh_WIFI_Bridge_08', 'vh_WIFI_Bridge_10']

n = {'b':bridge_list[4],'df' :df,'dt': dt}
d = requests.post(url, data = n)
data = d.json()

m = [e['datetime'] for e in data]
m.sort()

print('now: ', str(int(time.time())))
print('last timestamp: ', m[-1])
print('delay: ', str(int(time.time())-int(m[-1])))

a = [x['radius'] for x in data]
print(a)




