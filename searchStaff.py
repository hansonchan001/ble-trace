import requests
import datetime
import time
import json
import sys

bridge_list = ['vh_WIFI_Bridge_01', 'vh_WIFI_Bridge_02', 'vh_WIFI_Bridge_03', 'vh_WIFI_Bridge_04']

staff = {
    '1': 'Staff_01','2': 'Staff_02',
    '3': 'Staff_03','4': 'Staff_04',
    '5': 'Staff_05','6': 'Staff_06',
    '7': 'Staff_07','8': 'Staff_08',
    '9': 'Staff_09','10': 'Staff_10',
}

url = 'http://iot.rodsum.com/api/getlocationdetection'

window_in_seconds = 100

dt = str(int(time.time()))
df = str(int(dt)-window_in_seconds)

while 1: 
    for b in bridge_list:

        n = {'b':b,'df' :df,'dt': dt}
        d = requests.post(url, data = n)
        data = d.json()
        
        s = []
        for e in data:
            if e['asset_name'] == staff[str(sys.argv[1])]:
                s.append(float(e['radius']))
        try:
            print(b, ': ', round(sum(s)/len(s), 2))  
        except:
            print(' ')
    
    time.sleep(2)