import datetime
import time



while True:
    dt = str(int(time.time())-22)
    window_in_seconds = 5
    df = str(int(dt)-window_in_seconds)
    print(str(df) +" "+ str(dt))

    time.sleep(2)