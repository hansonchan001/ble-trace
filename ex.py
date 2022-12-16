import requests
import datetime
import time
import json

beacon_list = ['Staff_03', 'Staff_04', 'Staff_06', 'Staff_08', 'Staff_10']
bridge_list = ['vh_WIFI_Bridge_02']

url = 'http://iot.rodsum.com/api/getlocationdetection'

window_in_seconds = 100

dt = str(int(time.time()))
df = str(int(dt)-window_in_seconds)

while 1: 
    for b in bridge_list:

        n = {
            'b':b,
            'df' :df,
            'dt': dt
            }

        d = requests.post(url, data = n)

        data = d.json()
        s = []
        for e in data:
            if e['asset_name'] == 'Staff_06':
                s.append(float(e['radius']))
                #print(e['radius'])
        try:
            print('mean: ', round(sum(s)/len(s), 2))  
        except:
            print(" ")
    
    time.sleep(2)