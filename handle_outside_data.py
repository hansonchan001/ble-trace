import pandas as pd
import numpy as np
import datetime 
from os import walk

#turn all files to list then drop zero at once

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

f = []
for (dirpath, dirnames, filenames) in walk('data_outside_1213'):
    f.extend(filenames)

x = []
for file in f:
    a = pd.read_excel('data_outside_1213/'+file)
    x += changeToList(a)

x = pd.DataFrame(x)
x = x.loc[(x != 0).any(axis=1)]
df = x.loc[(x != 0).all(1)]

fileName = str(datetime.datetime.now().strftime('%H%M%S'))
pd.DataFrame(df).to_excel('processed_outside/' + fileName + '.xlsx', index=False)

x = np.array(x)
print(x)
print(x.shape)