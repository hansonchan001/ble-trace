import pandas as pd
from os import walk

#turn all files to list then drop zero at once

def handle_data(dir):
    f = []
    for (dirpath, dirnames, filenames) in walk(dir):
        f.extend(filenames)

    x = []
    for file in f:
        a = pd.read_excel(dir + '/' + file).values.tolist()
        x += a
    
    x = pd.DataFrame(x)
    x = x.loc[(x != 0).any(axis=1)]
    df = x.loc[(x != 0).all(1)]
    df = df.dropna(axis=0, how='any')
    
    return df.values.tolist()
