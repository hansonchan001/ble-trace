from keras.models import Sequential
from keras.layers import Dense, Dropout
from sklearn import model_selection
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import datetime
import random
import dataHandler

# load input data to list
#inside = pd.DataFrame(pd.read_excel('processed_inside/02241630.xlsx')).values.tolist()
#outside = pd.DataFrame(pd.read_excel('processed_outside/02241456_out.xlsx')).values.tolist()
inside = dataHandler.handle_data('HSK1A_in')
outside = dataHandler.handle_data('HSK1A_out')

#create labels according to the amonut of features
y_inside = [1 for i in range(len(inside))]
y_outside = [0 for i in range(len(outside))]

#combine the 2 input list into 1 input list
Y = y_inside+ y_outside
X = inside + outside

#split up the data set as training and testing data sets
X_train, X_test, Y_train, Y_test = model_selection.train_test_split(X, Y, test_size=0.2, random_state=0)

#turn list into numpy array
X_train = np.array(X_train)
X_test = np.array(X_test)
Y_train = np.array(Y_train)
Y_test = np.array(Y_test)

#initiate deep learning netowrk
classifier = Sequential()
#classifier.add(Dropout(.1, input_shape=(4,)))
classifier.add(Dense(units = 12, activation = 'relu', input_dim = 4))
classifier.add(Dense(units = 8, activation = 'relu'))
classifier.add(Dense(units = 4, activation = 'relu'))
classifier.add(Dense(units = 2, activation = 'relu'))
classifier.add(Dense(units = 1, activation = 'sigmoid'))
classifier.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics=['accuracy'])

#start traing the model and evaluate with testing data set
history = classifier.fit(X_train, Y_train, validation_split = 0.2, batch_size = 1, epochs = 50, shuffle= True)
loss, accuracy = classifier.evaluate(X_test, Y_test)

#save the model to models folder
model_name = str(datetime.datetime.now().strftime('%m%d%H%M'))
classifier.save('models/model_' + model_name)

print(history.history.keys())

#plot the training performance
fig, (ax1, ax2) = plt.subplots(1,2)
ax1.plot(history.history['accuracy'])
ax1.plot(history.history['val_accuracy'])
ax1.set_title('model accuracy')
ax1.set(xlabel='epoch', ylabel='accuracy')
ax1.legend(['train', 'test'], loc='upper left')
ax2.plot(history.history['loss'])
ax2.plot(history.history['val_loss'])
ax2.set_title('model loss')
ax2.set(xlabel='epoch')
ax2.legend(['train', 'test'], loc='upper left')

ax2.label_outer()