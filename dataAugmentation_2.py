import pandas as pd
import numpy as np
import math
import random

#                     (0.12, 1.5, 0.6, 1.8)                       (1.5, 0.18, 1.6, 0.7)
#  
#                     (0.8, 1.7, 0.18, 1.6)                       (1.7, 0.9, 1.5, 0.2 )

#       *   *   *   *   *   *   *   *   *   *   *   *   (0.19, 1.39, 0.82, 1.1)
#       *   *   *   *   *   *   *   *   *   *   *   *   
#       *   *   *   *   *   *   *   *   *   *   *   *   (1.26, 0.18, 1.11, 0.96)
#       *   *   *   -   -   -   -   -   -   *   *   *
#       *   *   *   -   -   -   -   -   -   *   *   *   (1.2, 1.12, 0.16, 0.9)
#       *   *   *   -   -   -   -   -   -   *   *   *
#       *   *   *   -   -   -   -   -   -   *   *   *   (1.31, 0.89, 0.97, 0.17)
#       *   *   *   -   -   -   -   -   -   *   *   *
#       *   *   *   -   -   -   -   -   -   *   *   *
#       *   *   *   *   *   *   *   *   *   *   *   *
#       *   *   *   *   *   *   *   *   *   *   *   *
#       *   *   *   *   *   *   *   *   *   *   *   *

# place the bridges at the corner of a 8*14/8*8 rectangle


di = 0.17  #initial distance to bridge
inside_columns = 6
inside_rows = 6
padding = 6
columns = padding*2 + inside_columns
rows = padding*2 + inside_rows
inside_w = 0.9
inside_h = 0.88
dv = inside_h/rows    #vertical interval between augementated points
dh = inside_w/columns     #horizontal interval between augmentated points

totalArea = []
insideArea = []

for i in range(rows):
    for j in range(columns):
        n = []
        d1 = math.sqrt(abs(dh*padding-dh*j)**2 + abs(dv*padding-dv*i)**2)+di
        d2 = math.sqrt(abs((inside_w+dh*padding)-dh*j)**2 + abs(dv*padding-dv*i)**2)+di
        d3 = math.sqrt(abs(dh*padding-dh*j)**2 + abs((inside_h+dv*padding)-dv*i)**2)+di
        d4 = math.sqrt(abs((inside_w+dh*padding)-dh*j)**2 + abs((inside_h+dv*padding)-dv*i)**2)+di
        n.append(round(d1, 2))
        n.append(round(d2, 2))
        n.append(round(d3, 2))
        n.append(round(d4, 2))
        totalArea.append(n)
#print(len(totalArea))
#print('')

for j in range(columns*padding+padding+1, columns*(padding+inside_rows)-padding+1, columns):
    for i in range(j, j+inside_rows):
        insideArea.append(totalArea[i])
        #print(i)

#print(len(insideArea))

     
outside = []
for i in insideArea:
    for u in totalArea:
        if i == u:
            totalArea.remove(u)

print(len(insideArea))
print(len(totalArea))

random.shuffle(totalArea)
#totalArea = totalArea[:round(len(totalArea)/2)]
print(len(totalArea))
print(insideArea)
random.shuffle(insideArea)
m = []
for i in range(4):
    for i in insideArea:
        n = []
        for j in range(len(i)):
            random_value = random.uniform(-0.1, 0.1)
            n.append(round(i[j]+random_value, 2))
        print(n)
        m.append(n)

insideArea = m + insideArea
        

print(insideArea)

#pd.DataFrame(insideArea).to_excel('aug_5x5_inside.xlsx', index=False)
pd.DataFrame(totalArea).to_excel('aug_5x5_outside.xlsx', index=False) 