import keras
from keras.models import Sequential
from keras.layers import Dense
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#prepare input data
#prepare input data
inside_data = pd.read_excel('processed_inside/114833.xlsx')
outside_data = pd.read_excel('processed_outside/141235.xlsx')

def changeToList(file):
    n = []
    for i in range(len(file)):
        c = []
        for j in range(len(file.iloc[0])):
            c.append(file[j][i])
            #print(x[i][j])
        b = np.array(c)
        n.append(b)

inside =  changeToList(inside_data)
outside = changeToList(outside_data)

y_inside = []
y_outside = []
for i in range(len(inside)):
    y_inside.append(1)
for g in range(len(outside)):
    y_outside.append(0)

Y_train = y_inside[:1500] + y_outside[:-100]
Y_test = y_inside[1500:] + y_outside[-100:]
X_train = inside[:1500] + outside[:-100]
X_test = inside[1500:] + outside[-100:]

X_train = np.array(X_train)
X_test = np.array(X_test)
Y_train = np.array(Y_train)
Y_test = np.array(Y_test)

# configure NN
classifier = Sequential()
classifier.add(Dense(units = 12, activation = 'relu', input_dim = 4))
#classifier.add(Dense(units = 8, activation = 'relu'))
classifier.add(Dense(units = 4, activation = 'relu'))
#classifier.add(Dense(units = 2, activation = 'relu'))
classifier.add(Dense(units = 1, activation = 'sigmoid'))

classifier.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics=['accuracy'])
history = classifier.fit(X_train, Y_train, batch_size = 1, epochs = 3000, shuffle= True)

loss, accuracy = classifier.evaluate(X_test, Y_test)
Y_pred = classifier.predict(X_test)

print(history.history.keys())
# summarize history for accuracy
plt.plot(history.history['accuracy'])
#plt.plot(history.history['val_accuracy'])
plt.title('model accuracy')
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()
# summarize history for loss
plt.plot(history.history['loss'])
#plt.plot(history.history['val_loss'])
plt.title('model loss')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()