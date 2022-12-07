import pandas as pd
import json

with open('record_127.json') as json_file:
    data = json.load(json_file)

df = pd.DataFrame(data)

df.to_excel('within.xlsx')