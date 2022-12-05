import requests
import datetime
import time
import json

url = 'http://iot.rodsum.com/api/getlocationdetection'

dt = str(int(time.mktime(datetime.datetime.now().timetuple())))
window_in_seconds = 30
df = str(int(dt)-window_in_seconds)

beacon_list = ['Staff_03', 'Staff_04', 'Staff_06', 'Staff_08', 'Staff_10']
bridge_list = ['vh_WIFI_Bridge_02', 'vh_WIFI_Bridge_04']

n = {
    'b':bridge_list[0],
    'df' :df,
    'dt': dt
    }

d = requests.post(url, data = n)

data = d.json()

print(data)