import requests
import datetime
import time
import json

url = 'http://iot.rodsum.com/api/getlocationdetection'

staff_list = ['Staff_01', 'Staff_02','Staff_03', 'Staff_04',  'Staff_05','Staff_06','Staff_07', 'Staff_08','Staff_09','Staff_10']
bridge_list = ['vh_WIFI_Bridge_01', 'vh_WIFI_Bridge_02', 'vh_WIFI_Bridge_03', 'vh_WIFI_Bridge_04']

while(1):
    
    df = str(int(time.time())-80)
    dt = str(int(time.time()))
    print('dt"',dt)
    print('df: ',df)
    n = {}
    for v in bridge_list:

        a = {
            'b': v,
            'df':df,
            'dt':dt
        }

        x = requests.post(url, data=a)
        data = x.json()

        b = []
        for t in data:
            if t['asset_name'] not in b:
                b.append(t['asset_name'])
        b.sort()

        n[v] = b
    
    print(n)

 
    for c in staff_list:
        z = []
        for a in bridge_list:
            if c in n[a] and a not in z:
                z.append(a)
        print(c, ' is under: ' , z)
    
    print(" ")
    
    time.sleep(15)










