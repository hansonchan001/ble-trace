import requests
import datetime
import time
import json

beacon_list = ['Staff_03', 'Staff_04', 'Staff_06', 'Staff_08', 'Staff_10']
bridge_list = ['vh_WIFI_Bridge_02', 'vh_WIFI_Bridge_04']

url = 'http://iot.rodsum.com/api/getlocationdetection'

window_in_seconds = 100

dt = str(int(time.time()))
df = str(int(dt)-window_in_seconds)

for b in bridge_list:

    n = {
        'b':b,
        'df' :df,
        'dt': dt
        }

    d = requests.post(url, data = n)

    data = d.json()
    for e in data:
        if e['asset_name'] == 'Staff_03' or e['asset_name'] == 'Staff_09' or e['asset_name'] == 'Staff_10':
            print(e)
        elif e['asset_name'] == 'Staff_04':
            print(e)