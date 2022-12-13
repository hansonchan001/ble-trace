import keras
from keras.models import Sequential
from keras.layers import Dense
import keras.optimizers as opt
import pandas as pd
import numpy as np
import handle_inside_data
import matplotlib.pyplot as plt

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

Y_train = y_inside[:100] + y_outside[:-100]
Y_test = y_inside[100:] + y_outside[-100:]
Y_train = np.array(Y_train)
Y_test = np.array(Y_test)

X_train = inside[:100] + outside[:-100]
X_test = inside[100:] + outside[-100:]
X_train = np.array(X_train)
X_test = np.array(X_test)

# configure NN
classifier = Sequential()
classifier.add(Dense(units = 16, activation = 'relu', input_dim = 4))
classifier.add(Dense(units = 8, activation = 'relu'))
classifier.add(Dense(units = 4, activation = 'relu'))
classifier.add(Dense(units = 1, activation = 'sigmoid'))

classifier.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics=['accuracy'])
history = classifier.fit(X_train, Y_train, validation_split=0.33, epochs=150, batch_size=1, verbose=0, shuffle= True)

loss, accuracy = classifier.evaluate(X_test)
#Y_pred = classifier.predict(X_test)

print(history.history.keys())
# summarize history for accuracy
plt.plot(history.history['accuracy'])
plt.plot(history.history['val_accuracy'])
plt.title('model accuracy')
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()
# summarize history for loss
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('model loss')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()
