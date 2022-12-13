import requests
import datetime
import time
import json
import pandas as pd

url = 'http://iot.rodsum.com/api/getlocationdetection'

staff_list = ['Staff_03', 'Staff_04', 'Staff_06', 'Staff_08', 'Staff_10', 'Staff_01', 'Staff_02', 'Staff_05', 'Staff_07', 'Staff_09']
bridge_list = ['vh_WIFI_Bridge_01', 'vh_WIFI_Bridge_02', 'vh_WIFI_Bridge_03', 'vh_WIFI_Bridge_04']


count = 0

try: 
    while (1):

        #window_in_seconds = 5
        dt = str(int(time.time()))
        df = str(int(dt)-100)
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

        """ with open('record.json', 'r+') as outfile:
            z = json.load(outfile)
        z.append(p)
        test = json.dumps(z, indent=2)
        with open('record.json', 'w') as outfile:
            outfile.write(test) """
        for keys, values in p.items():
            print(keys, str(values))
        for x in list(p.values()):
            l.append(x)
        #print(l)
        count += 1
        print(count)
        print(" ")
        time.sleep(10)

except KeyboardInterrupt:
    file_name = str(datetime.datetime.now().strftime('%H%M'))
    pd.DataFrame(l).to_excel('data_1213/' + file_name + '.xlsx', index=False)

finally:
    print('\ndata stored in excel file.')