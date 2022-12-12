import keras
from keras.models import Sequential
from keras.layers import Dense
import pandas as pd
import numpy as np

#prepare input data
y = pd.read_excel('processedData/processed_out_1100.xlsx')
a = pd.read_excel('processedData/processed_in_110223.xlsx')
b = pd.read_excel('processedData/processed_in_110226.xlsx')
c = pd.read_excel('processedData/processed_in_110232.xlsx')

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

# 439 data for inside, 241 data for outside
x_out = changeToList(y)
x_in = changeToList(a)+changeToList(b)+changeToList(c)

X_train = x_in[:420] + x_out[:-20]
X_test = x_in[420:] + x_out[-20:]
X_train = np.array(X_train)
X_test = np.array(X_test)

y_in = []
y_out = []
for i in range(len(x_in)):
    y_in.append([1,0])
for g in range(len(x_out)):
    y_out.append([0,1])

Y_train = y_in[:420] + y_out[:-20]
Y_train = np.array(Y_train)
Y_test = y_in[420:] + y_out[-20:]
Y_test = np.array(Y_test)

# configure NN
classifier = Sequential()
classifier.add(Dense(units = 16, activation = 'relu', input_dim = 4))
classifier.add(Dense(units = 8, activation = 'relu'))
classifier.add(Dense(units = 6, activation = 'relu'))
classifier.add(Dense(units = 2, activation = 'sigmoid'))

classifier.compile(optimizer = 'adam', loss = 'binary_crossentropy')
classifier.fit(X_train, Y_train, batch_size = 1, epochs = 2800, shuffle= True)

Y_pred = classifier.predict(X_test)
#Y_pred = [ 1 if y>=0.5 else 0 for y in Y_pred ]
print(Y_pred)
#print(len(Y_pred))
for y in Y_pred:
    if y[0] > 0.5:
        y[0] = 1
        y[1] = 0
    else:
        y[1] = 1
        y[0] = 0
#print(Y_pred) 

Y_pred = (np.rint(Y_pred)).astype(int)
d = 0
for p in range(len(Y_pred)):
    if Y_pred[p][0] == Y_test[p][0]:
        d += 1
print(d/len(Y_pred)*100)