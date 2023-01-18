import pandas as pd
import numpy as np
import datetime 
import random
import math

di = 2.15   #initial distance to bridge (b1 in this case)
dh = 3     #horizontal interval between augmentated points
dv = 2.5    #vertical interval between augementated points
columns = 3
rows = 3
w = 5
h = 5

data = []
for i in range(rows):
    
    for j in range(columns):
        n = []
        d1 = math.sqrt((di+dh*j)**2 + (dv*i)**2)
        d2 = math.sqrt((w+di+dh*j)**2 + (dv*i)**2)
        d3 = math.sqrt((di+dh*j)**2 + (h-dv*i)**2)
        d4 = math.sqrt((w+di+dh*j)**2 + (h-dv*i)**2)
        n.append(round(d1, 2))
        n.append(round(d2, 2))
        n.append(round(d3, 2))
        n.append(round(d4, 2))
        #print(n)
        data.append(n)

print(data)

#  ^    ^    ^  *     *b1              b2
#  ^    ^    ^
#  ^    ^    ^
#  ^    ^    ^  *     *b3              b4


