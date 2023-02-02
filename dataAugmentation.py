import pandas as pd
import numpy as np
import math

di = 0.18   #initial distance to bridge
columns = 20
rows = 20
w = 1.32
h = 1
dv = h/rows    #vertical interval between augementated points
dh = w/columns     #horizontal interval between augmentated points

inside = []
for i in range(rows):
    for j in range(columns):
        n = []
        d1 = math.sqrt((di+dh*j)**2 + (dv*i)**2)
        d2 = math.sqrt((w-di-dh*j)**2 + (dv*i)**2)
        d3 = math.sqrt((di+dh*j)**2 + (h-dv*i)**2)
        d4 = math.sqrt((w-di-dh*j)**2 + (h-dv*i)**2)
        n.append(round(d1, 2))
        n.append(round(d2, 2))
        n.append(round(d3, 2))
        n.append(round(d4, 2))
        #print(n)
        inside.append(n)

print(inside)
print(len(inside))

di_l = 0.18   #initial distance to bridge
columns_l = 20
rows_l = 20
w_l = 1.32
h_l = 1
dv_l = h_l/rows_l    #vertical interval between augementated points
dh_l = w_l/columns_l     #horizontal interval between augmentated points

outside = []
for i in range(rows_l):
    for j in range(columns_l):
        n = []
        d1 = math.sqrt((di_l+dh_l*j)**2 + (dv_l*i)**2)
        d2 = math.sqrt((w_l+di_l+dh_l*j)**2 + (dv_l*i)**2)
        d3 = math.sqrt((di_l+dh_l*j)**2 + (h-dv_l*i)**2)
        d4 = math.sqrt((w_l+di_l+dh_l*j)**2 + (h-dv_l*i)**2)
        n.append(round(d1, 2))
        n.append(round(d2, 2))
        n.append(round(d3, 2))
        n.append(round(d4, 2))
        #print(n)
        outside.append(n)
print(outside)
print(len(outside))

di_r = 0.18   #initial distance to bridge
columns_r = 20
rows_r = 20
w_r = 1.8
h_r = 2.5
dv_r = h_r/rows_r #vertical interval between augementated points
dh_r = w_r/columns_r     #horizontal interval between augmentated points

outside = []
for i in range(rows_r):
    for j in range(columns_r):
        n = []
        d1 = math.sqrt((w_r+di_r+dh_r*j)**2 + (dv_r*i)**2)
        d2 = math.sqrt((di_r+dh_r*j)**2 + (dv_r*i)**2)
        d3 = math.sqrt((w_r+di_r+dh_r*j)**2 + (h_r-dv_r*i)**2)
        d4 = math.sqrt((di_r+dh_r*j)**2 + (h-dv_r*i)**2)
        n.append(round(d1, 2))
        n.append(round(d2, 2))
        n.append(round(d3, 2))
        n.append(round(d4, 2))
        #print(n)
        outside.append(n)
print(outside)
print(len(outside))

di_u = 0.4  
columns_u = 20
rows_u = 20
w_u = 1.32
h_u = 1
dv_u = h_u/rows_u #vertical interval between augementated points
dh_u = w_u/columns_u     #horizontal interval between augmentated points

outside = []
for i in range(rows_u):
    for j in range(columns_u):
        n = []
        d1 = math.sqrt((di_u+dh_u*j)**2 + (dv_u*i)**2)
        d2 = math.sqrt((w_u-di_u-dh_u*j)**2 + (dv_u*i)**2)
        d3 = math.sqrt((di_u+dh_u*j)**2 + (h_u+dv_u*i)**2)
        d4 = math.sqrt((w_u-di_u-dh_u*j)**2 + (h_u+dv_u*i)**2)
        n.append(round(d1, 2))
        n.append(round(d2, 2))
        n.append(round(d3, 2))
        n.append(round(d4, 2))
        #print(n)
        outside.append(n)
print(outside)
print(len(outside))

di_d = 0.5  
columns_d = 10
rows_d = 10
w_d = 1.32
h_d = 1.1
dv_d = h_d/rows_d #vertical interval between augementated points
dh_d = w_d/columns_d     #horizontal interval between augmentated points

outside = []
for i in range(rows_d):
    for j in range(columns_d):
        n = []
        d1 = math.sqrt((di_d+dh_d*j)**2 + (h_d+dv_d*i)**2)
        d2 = math.sqrt((w_d-di_d+dh_d*j)**2 + (h_d+dv_d*i)**2)
        d3 = math.sqrt((di_d+dh_d*j)**2 + (dv_d*i)**2)
        d4 = math.sqrt((w_d-di_d+dh_d*j)**2 + (dv_d*i)**2)
        n.append(round(d1, 2))
        n.append(round(d2, 2))
        n.append(round(d3, 2))
        n.append(round(d4, 2))
        #print(n)
        outside.append(n)
print(outside)
print(len(outside))
