import pandas as pd
import numpy as np
import datetime 
from os import walk
import sys

#turn all files to list then drop zero at once

input_dir = sys.argv[1]
output_dir = sys.argv[2]

f = []
for (dirpath, dirnames, filenames) in walk(input_dir):
    f.extend(filenames)

x = []
for file in f:
    a = pd.read_excel(input_dir + '/' + file).values.tolist()
    x += a

x = pd.DataFrame(x)
x = x.loc[(x != 0).any(axis=1)]
df = x.loc[(x != 0).all(1)]
df = df.dropna(axis=0, how='any')

fileName = str(datetime.datetime.now().strftime('%m%d%H%M'))
pd.DataFrame(df).to_excel('processed_' + output_dir +'/'+ fileName + '.xlsx', index=False)

x = np.array(df)
print(df)
print(df.shape)