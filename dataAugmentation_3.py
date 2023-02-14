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
inside = []
for i in range(500):
    a = round(random.uniform(0.18, 1.28*1.1), 2)
    b = round(random.uniform(0.18, 1.28*1.1), 2)
    c = round(random.uniform(0.18, 1.1*1.1), 2)
    d = round(random.uniform(0.18, 1.1*1.1), 2)
    inside.append([a,b,c,d])

print(inside)

#outside = []
#for i in range(1000):
#    a = round(random.uniform(0.18, 1.28*1.1), 2)
#    b = round(random.uniform(0.18, 1.28*1.1), 2)
#    c = round(random.uniform(0.18, 1.1*1.1), 2)
#    d = round(random.uniform(0.18, 1.1*1.1), 2)
#    outside.append([a,b,c,d])
#
#print(inside)


pd.DataFrame(inside).to_excel('aug_5x5_inside.xlsx', index=False)


