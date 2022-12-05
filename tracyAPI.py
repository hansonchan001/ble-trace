import requests
import datetime
import time
import json

url = 'http://iot.rodsum.com/api/getlocationdetection'

dt = str(int(time.mktime(datetime.datetime.now().timetuple())))
window_in_seconds = 100
df = str(int(dt)-window_in_seconds)

beacon_list = ['Staff_03', 'Staff_04', 'Staff_06', 'Staff_08', 'Staff_10']
bridge_list = ['vh_WIFI_Bridge_02', 'vh_WIFI_Bridge_04']

for v in bridge_list:
    n = {'b':v,'df' :df,'dt': dt}

    d = requests.post(url, data = n)
    data = d.json()

    for e in data:
        e["time"] = str(datetime.datetime.fromtimestamp(int(e['datetime'])).strftime('%H:%M:%S'))
    data_json = json.dumps(data, indent=4)
    bridge_name = v +'.json'
    with open(bridge_name, 'w') as outfile:
        outfile.write(data_json)

""" for device in beacon_list:

    f = []
    for r in data_x:
        if r['asset_name'] == device:
            f.append(r)

    f_json = json.dumps(f, indent=4)

    json_name = device + '.json'

    with open(json_name, 'w') as outfile:
        outfile.write(f_json)
 """





