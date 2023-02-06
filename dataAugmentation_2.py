import pandas as pd
import numpy as np
import math
import json

#                     (0.12, 1.5, 0.6, 1.8)                       (1.5, 0.18, 1.6, 0.7)
#     *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *
#     *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *
#     *   *   *   *   -   -   -   -   -   -   -   -   -   -   -   -   *   *   *   *
#     *   *   *   *   -   -   -   -   -   -   -   -   -   -   -   -   *   *   *   *
#     *   *   *   *   -   -   -   -   -   -   -   -   -   -   -   -   *   *   *   *
#     *   *   *   *   -   -   -   -   -   -   -   -   -   -   -   -   *   *   *   *
#     *   *   *   *   -   -   -   -   -   -   -   -   -   -   -   -   *   *   *   *
#     *   *   *   *   -   -   -   -   -   -   -   -   -   -   -   -   *   *   *   *
#     *   *   *   *   -   -   -   -   -   -   -   -   -   -   -   -   *   *   *   *
#     *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *
#     *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *
#                     (0.8, 1.7, 0.18, 1.6)                       (1.7, 0.9, 1.5, 0.2 )

di = 0.18  #initial distance to bridge
columns = 20
rows = 10
inside_w = 1.5
inside_h = 0.75
dv = inside_h/rows    #vertical interval between augementated points
dh = inside_w/columns     #horizontal interval between augmentated points

totalArea = []
insideArea = []


for i in range(rows):
    for j in range(columns):
        n = []
        d1 = math.sqrt((dh*j)**2 + (dv*i)**2)+di
        d2 = math.sqrt((inside_w-dh*j)**2 + (dv*i)**2)+di
        d3 = math.sqrt((dh*j)**2 + (inside_h-dv*i)**2)+di
        d4 = math.sqrt((inside_w-dh*j)**2 + (inside_h-dv*i)**2)+di
        n.append(round(d1, 2))
        n.append(round(d2, 2))
        n.append(round(d3, 2))
        n.append(round(d4, 2))
        #print(n)
        insideArea.append(n)


