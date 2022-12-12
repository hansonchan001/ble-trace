import pandas as pd
import numpy as np

y = pd.read_excel('processedData/processed_out_1100.xlsx')
a = pd.read_excel('processedData/processed_in_110223.xlsx')
b = pd.read_excel('processedData/processed_in_110226.xlsx')
c = pd.read_excel('processedData/processed_in_110232.xlsx')
#x = pd.read_excel('input_1407.xlsx')

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

#241 data for outside, 439 data for inside
x_out = changeToList(y)
x_in = changeToList(a)+changeToList(b)+changeToList(c)

x = x_in + x_out
x = np.array(x)
print(x)
print(x.shape)

y = []
for i in range(len(x_in)):
    y.append([1,0])
for g in range(len(x_out)):
    y.append([0,1])
y = np.array(y)
print(y)
print(y.shape)