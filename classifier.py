from keras.models import Sequential
from keras.layers import Dense, Dropout
import pandas as pd
import numpy as np
import datetime
import matplotlib.pyplot as plt
import random

inside = pd.DataFrame(pd.read_excel('processed_inside/10x5.xlsx')).values.tolist()
outside = pd.DataFrame(pd.read_excel('processed_outside/7x12out.xlsx')).values.tolist()

random.shuffle(inside)
inside = inside[:1500]

random.shuffle(outside)
outside = outside[:800]

y_inside = [1 for i in range(len(inside))]
y_outside = [0 for i in range(len(outside))]

#y_inside = []
#y_outside = []
#for i in range(len(inside)):
#    y_inside.append(1)
#for g in range(len(outside)):
#    y_outside.append(0)

Y_train = y_inside+ y_outside
X_train = inside + outside

suffled_data = {'input': X_train, 
                'output': Y_train}

df= pd.DataFrame(suffled_data)
df = df.sample(frac = 1)

X_test = df['input'].values.tolist()
Y_test = df['output'].values.tolist()

evaluateSamplesNumber = 200

X = np.array(X_test[:-evaluateSamplesNumber])
Y = np.array(Y_test[:-evaluateSamplesNumber])

classifier = Sequential()
#classifier.add(Dropout(.1, input_shape=(4,)))
classifier.add(Dense(units = 12, activation = 'relu', input_dim = 4))
classifier.add(Dense(units = 8, activation = 'relu'))
classifier.add(Dense(units = 4, activation = 'relu'))
classifier.add(Dense(units = 2, activation = 'relu'))
classifier.add(Dense(units = 1, activation = 'sigmoid'))
classifier.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics=['accuracy'])

history = classifier.fit(X, Y, validation_split = 0.2, batch_size = 1, epochs = 1000, shuffle= True)

#evaluate the model
X_Eva = np.array(X_test[-evaluateSamplesNumber:])
Y_Eva = np.array(Y_test[-evaluateSamplesNumber:])
loss, accuracy = classifier.evaluate(X_Eva, Y_Eva)

model_name = str(datetime.datetime.now().strftime('%m%d%H%M'))
classifier.save('models/model_' + model_name)

print(history.history.keys())

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

