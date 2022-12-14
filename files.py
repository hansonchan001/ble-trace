import pandas as pd
import json

x = pd.read_excel('data_128/within_1.xlsx')
n = []
for i in range(len(x)):
    n.append([1,0])
x['label'] = n
x.to_excel('data_128/processed.xlsx', index=False)
