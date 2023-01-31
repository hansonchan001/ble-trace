import keras
from keras.models import Sequential
from keras.layers import Dense
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

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

inside_data = pd.read_excel('processed_inside/5x5_16.xlsx')
outside_data = pd.read_excel('processed_outside/7x7out.xlsx')

inside = changeToList(inside_data)
outside = changeToList(outside_data)

y_inside = []
y_outside = []
for i in range(len(inside)):
    y_inside.append(1)
for g in range(len(outside)):
    y_outside.append(0)

Y_train = y_inside+ y_outside
X_train = inside + outside

suffled_data = {'input': X_train, 
                'output': Y_train}

df= pd.DataFrame(suffled_data)
df = df.sample(frac = 1)

X = np.array(df['input'].values.tolist())
Y = np.array(df['output'].values.tolist())

classifier = Sequential()
classifier.add(Dense(units = 8, activation = 'relu', input_dim = 4))
classifier.add(Dense(units = 4, activation = 'relu'))
classifier.add(Dense(units = 1, activation = 'sigmoid'))

classifier.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics=['accuracy'])
history = classifier.fit(X, Y, validation_split = 0.2, batch_size = 1, epochs = 500, shuffle= True)

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