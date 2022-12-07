import requests
import datetime
import time

url = 'http://iot.rodsum.com/api/getlocationdetection'

staff_list = ['Staff_03', 'Staff_04', 'Staff_06', 'Staff_08', 'Staff_10']
bridge_list = ['vh_WIFI_Bridge_02', 'vh_WIFI_Bridge_04']

while (1):

    window_in_seconds = 5
    dt = str(int(time.time()-22))
    df = str(int(dt)-window_in_seconds)
    print('dt: ', dt)
    print('df: ', df)

    for v in bridge_list:

        a = {'b': v,'df':df,'dt':dt}
        x = requests.post(url, data=a)
        data = x.json()
        print(v + ' ' + str(datetime.datetime.now().strftime('%H:%M:%S')))

        for b in staff_list:
            e = []
            for t in data:
                if b == t['asset_name']:
                    e.append(float(t['radius']))
            #print(b+str(e))
            try:  
                s = sum(e)/len(e)
                print(b, round(s, 2))
            except:
                print(b)
        
        print(" ")
    time.sleep(15)
    
