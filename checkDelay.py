import requests
import time
import sys

url = 'http://iot.rodsum.com/api/getlocationdetection'


beacon_list = ['Staff_03', 'Staff_04', 'Staff_06', 'Staff_08', 'Staff_10', 'Staff_01', 'Staff_02', 'Staff_05', 'Staff_07', 'Staff_09']
bridge_list = ['vh_WIFI_Bridge_01', 'vh_WIFI_Bridge_02', 'vh_WIFI_Bridge_03', 'vh_WIFI_Bridge_04']

while 1:
    for b in bridge_list:
        n = {
            'b': b,
            'df': str(int(time.time())-100),
            'dt': str(int(time.time())),
            }

        d = requests.post(url, data = n)
        data = d.json()

        try:
            m=[]
            for e in data:
                m.append(e['datetime'])
            m.sort()
            print(b + ' delay: ' + str(int(time.time())-int(m[-1])))
        
        except:
            print('no data')
    print('current unix time: ' + str(int(time.time())))
    time.sleep(10)