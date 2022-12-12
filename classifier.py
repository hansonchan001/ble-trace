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

X_train = x_in[:400] + x_out[:-40]
X_test = x_in[400:] + x_out[-40:]
X_train = np.array(X_train)
X_test = np.array(X_test)
""" print(X_train)
print(X_train.shape)
print(X_test)
print(X_test.shape)
x = x_in + x_out
x = np.array(x) """

y_in = []
y_out = []
for i in range(len(x_in)):
    y_in.append([1,0])
for g in range(len(x_out)):
    y_out.append([0,1])

Y_train = y_in[:400] + y_out[:-40]
Y_train = np.array(Y_train)
Y_test = y_in[400:] + y_out[-40:]
Y_test = np.array(Y_test)
""" print(Y_train)
print(Y_train.shape)
print(Y_test)
print(Y_test.shape) """

# configure NN
classifier = Sequential()
classifier.add(Dense(units = 16, activation = 'relu', input_dim = 4))
classifier.add(Dense(units = 8, activation = 'relu'))
classifier.add(Dense(units = 6, activation = 'relu'))
classifier.add(Dense(units = 2, activation = 'sigmoid'))

classifier.compile(optimizer = 'rmsprop', loss = 'binary_crossentropy')
classifier.fit(X_train, Y_train, batch_size = 1, epochs = 5)

Y_pred = classifier.predict(X_test)
Y_pred = [ 1 if y>=0.5 else 0 for y in Y_pred ]