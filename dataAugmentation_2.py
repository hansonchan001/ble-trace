import pandas as pd
import numpy as np
import math
import json

#           (0.12, 1.5, 0.6, 1.8)   *   *   #   #   (1.5, 0.18, 1.6, 0.7)
#           *   *   *   #   #   #   #   #   &   &   &
#           *   *   *   ()   -   -   -   -   &   &   &
#           *   *   *   -   -   -   -   -   &   &   &
#           *   *   *   -   -   -   -   -   &   &   &
#           *   *   *   -   -   -   -   -   &   &   &
#           *   *   *   @   @   @   @   @   &   &   &
#           (0.8, 1.7, 0.18, 1.6) *   *   @   @   @ (1.7, 0.9, 1.5, 0.2 )

di = 0.18  #initial distance to bridge
columns = 40
rows = 40
w = 1.5
h = 0.6
dv = h/rows    #vertical interval between augementated points
dh = w/columns     #horizontal interval between augmentated points

totalArea = []
for i in range(rows):
    for j in range(columns):
        n = []
        d1 = math.sqrt((dh*j)**2 + (dv*i)**2)+di
        d2 = math.sqrt((w-dh*j)**2 + (dv*i)**2)+di
        d3 = math.sqrt((dh*j)**2 + (h-dv*i)**2)+di
        d4 = math.sqrt((w-dh*j)**2 + (h-dv*i)**2)+di
        n.append(round(d1, 2))
        n.append(round(d2, 2))
        n.append(round(d3, 2))
        n.append(round(d4, 2))
        #print(n)
        totalArea.append(n)

#print(inside)
#print(len(inside))

di_l = 0.6   #initial distance to bridge
columns_l = 20
rows_l = 20
w_l = 1
h_l = 2
dv_l = h_l/rows_l    #vertical interval between augementated points
dh_l = w_l/columns_l     #horizontal interval between augmentated points

outside_l = []
for i in range(rows_l):
    for j in range(columns_l):
        n = []
        d1 = math.sqrt((dh_l*j)**2 + (dv_l*i)**2)+di_l
        d2 = math.sqrt((w+dh_l*j)**2 + (dv_l*i)**2)+di_l
        d3 = math.sqrt((dh_l*j)**2 + (h-dv_l*i)**2)+di_l
        d4 = math.sqrt((w+dh_l*j)**2 + (h-dv_l*i)**2)+di_l
        n.append(round(d1, 2))
        n.append(round(d2, 2))
        n.append(round(d3, 2))
        n.append(round(d4, 2))
        #print(n)
        outside_l.append(n)


di_r = 0.6  #initial distance to bridge
columns_r = 20
rows_r = 20
w_r = 1
h_r = 2
dv_r = h_r/rows_r #vertical interval between augementated points
dh_r = w_r/columns_r     #horizontal interval between augmentated points

outside_r = []
for i in range(rows_r):
    for j in range(columns_r):
        n = []
        d1 = math.sqrt((w+dh_r*j)**2 + (dv_r*i)**2)+di_r
        d2 = math.sqrt((dh_r*j)**2 + (dv_r*i)**2)+di_r
        d3 = math.sqrt((w+dh_r*j)**2 + (h-dv_r*i)**2)+di_r
        d4 = math.sqrt((dh_r*j)**2 + (h-dv_r*i)**2)+di_r
        n.append(round(d1, 2))
        n.append(round(d2, 2))
        n.append(round(d3, 2))
        n.append(round(d4, 2))
        #print(n)
        outside_r.append(n)


di_u = 0.6 
columns_u = 15
rows_u = 15
w_u = 1.5
h_u = 1
dv_u = h_u/rows_u #vertical interval between augementated points
dh_u = w_u/columns_u     #horizontal interval between augmentated points

outside_u = []
for i in range(rows_u):
    for j in range(columns_u):
        n = []
        d1 = math.sqrt((dh_u*j)**2 + (dv_u*i)**2)
        d2 = math.sqrt((w-dh_u*j)**2 + (dv_u*i)**2)+di_u
        d3 = math.sqrt((dh_u*j)**2 + (h+dv_u*i)**2)+di_u
        d4 = math.sqrt((w-dh_u*j)**2 + (h+dv_u*i)**2)+di_u
        n.append(round(d1, 2))
        n.append(round(d2, 2))
        n.append(round(d3, 2))
        n.append(round(d4, 2))
        #print(n)
        outside_u.append(n)


di_d = 0.6
columns_d = 15
rows_d = 15
w_d = 1.5
h_d = 1
dv_d = h_d/rows_d #vertical interval between augementated points
dh_d = w_d/columns_d     #horizontal interval between augmentated points

outside_d = []
for i in range(rows_d):
    for j in range(columns_d):
        n = []
        d1 = math.sqrt((di_d+dh_d*j)**2 + (h+dv_d*i)**2)
        d2 = math.sqrt((w-di_d+dh_d*j)**2 + (h+dv_d*i)**2)
        d3 = math.sqrt((di_d+dh_d*j)**2 + (dv_d*i)**2)
        d4 = math.sqrt((w-di_d+dh_d*j)**2 + (dv_d*i)**2)
        n.append(round(d1, 2))
        n.append(round(d2, 2))
        n.append(round(d3, 2))
        n.append(round(d4, 2))
        #print(n)
        outside_d.append(n)


r = json.dumps(outside_r, indent=4)
l = json.dumps(outside_l, indent=4)
u = json.dumps(outside_u, indent=4)
d = json.dumps(outside_d, indent=4)
inside = json.dumps(inside, indent=4)

v = [r, l, u, d, inside]
count = 0
for q in v:
    count += 1
    with open(str(count), "w") as outfile:
        outfile.write(q)