import pandas as pd
import numpy as np
import datetime

# eliminate irregular data

dir = 'processed_inside/01121441.xlsx'

def changeToList(file):
    n = []
    for i in range(len(file)):
        c = []
        for j in range(len(file.iloc[0])):
            c.append(file[j][i])
            #print(x[i][j])
        b = np.array(c)
        n.append(b)

    return n

a = pd.read_excel(dir)
x = changeToList(a)

n = []
for i in x:
    if i[0] > i[1] or i[2] > i[3]:
        continue
    else:
        n.append(i)

x = pd.DataFrame(n)
x = x.loc[(x != 0).any(axis=1)]
df = x.loc[(x != 0).all(1)]
df = df.dropna(axis=0, how='any')

fileName = str(datetime.datetime.now().strftime('%m%d%H%M'))
pd.DataFrame(df).to_excel('processed_inside/' + fileName + '.xlsx', index=False)

print(df)
