import requests
import datetime
import time
import json
import pandas as pd

url = 'http://iot.rodsum.com/api/getlocationdetection'

staff_list = ['Staff_03', 'Staff_04', 'Staff_06', 'Staff_08', 'Staff_10']
bridge_list = ['vh_WIFI_Bridge_02', 'vh_WIFI_Bridge_04']

#count = 0
l = []
j = '[]'
json_file = json.loads(j)
with open('record.json', 'w') as outfile:
    outfile.write(j)
try: 
    while (1):

        window_in_seconds = 5
        dt = str(int(time.time()-22))
        df = str(int(dt)-window_in_seconds)
        #print('dt: ', dt)
        #print('df: ', df)

        p = {}
        for staff in staff_list:
            p[staff] = []

        for bridge in bridge_list:

            data_keys = {'b': bridge,'df':df,'dt':dt}
            x = requests.post(url, data=data_keys)
            data = x.json()

            for staff in staff_list:
                n = []

                for element in data:
                    if staff == element['asset_name']:
                        n.append(float(element['radius']))
                try:
                    distance = round(sum(n)/len(n), 2)
                    p[staff].append(distance)
                except:
                    p[staff].append(0)

        with open('record.json', 'r+') as outfile:
            z = json.load(outfile)
        z.append(p)
        test = json.dumps(z, indent=2)
        with open('record.json', 'w') as outfile:
            outfile.write(test)

        print(p)
        for x in list(p.values()):
            l.append(x)
        print(l)
        print(" ")
        time.sleep(15)

except KeyboardInterrupt:
    #count += 1
    pd.DataFrame(l).to_excel('data_128/without_1.xlsx')

finally:
    print('data stored in excel file.')

