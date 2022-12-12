import pandas as pd
import numpy as np
import datetime 
import sys

x = pd.read_excel(sys.argv[1] + '.xlsx')
x = pd.DataFrame(x)

df = x.loc[(x != 0).any(axis=1)]
df = df.loc[(df != 0).all(1)]

fileName = str(datetime.datetime.now().strftime('%H%M%S'))
pd.DataFrame(df).to_excel('processedData/processed_in_' + fileName + '.xlsx', index=False)
