import keras
from keras.models import Sequential
from keras.layers import Dense
import keras.optimizers as opt
import pandas as pd
import numpy as np
import handle_inside_data

#prepare input data
inside_data = pd.read_excel('processed_inside/114833.xlsx')
outside_data = pd.read_excel('processed_outside/141235.xlsx')

inside = handle_inside_data.changeToList(inside_data)
outside = handle_inside_data.changeToList(outside_data)

y_inside = []
y_outside = []
for i in range(len(inside)):
    y_inside.append(1)
for g in range(len(outside)):
    y_outside.append(0)

Y_train = y_inside[:1200] + y_outside[:-1000]
Y_test = y_inside[1200:] + y_outside[-1000:]
Y_train = np.array(Y_train)
Y_test = np.array(Y_test)

X_train = inside[:1200] + outside[:-1000]
X_test = inside[1200:] + outside[-1000:]
X_train = np.array(X_train)
X_test = np.array(X_test)

# configure NN
classifier = Sequential()
classifier.add(Dense(units = 16, activation = 'relu', input_dim = 4))
classifier.add(Dense(units = 8, activation = 'relu'))
classifier.add(Dense(units = 4, activation = 'relu'))
classifier.add(Dense(units = 1, activation = 'sigmoid'))

classifier.compile(optimizer = 'adam', loss = 'binary_crossentropy')
classifier.fit(X_train, Y_train, batch_size = 1, epochs = 1500, shuffle= True)
opt = opt.Adam(learning_rate=0.001)

Y_pred = classifier.predict(X_test)
Y_pred_mirror = Y_pred

for y in Y_pred_mirror:
    if y > 0.5:
        y = 1
    else:
        y = 0

Y_pred= (np.rint(Y_pred)).astype(int)
d = 0
for p in range(len(Y_pred)):
    if Y_pred[p] == Y_test[p]:
        d += 1
print(d/len(Y_pred)*100)