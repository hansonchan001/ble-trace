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
    #print('dt: ', dt)
    #print('df: ', df)
    

    for staff in staff_list:
        n = []
        
        for bridge in bridge_list:
            
            a = {'b': bridge,'df':df,'dt':dt}
            x = requests.post(url, data=a)
            data = x.json()
            
            #print(bridge + ' ' + str(datetime.datetime.now().strftime('%H:%M:%S')))

            e = []
            for element in data:
                if staff == element['asset_name']:
                    e.append(float(element['radius']))
                
            distance =  sum(e)/len(e)
            n.append(round(distance, 2))  
        
        print(staff, ' ', n)

    print(" ")
    time.sleep(15)
    
