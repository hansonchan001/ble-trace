from keras.models import Sequential
from keras.layers import Dense
import pandas as pd
import numpy as np
import datetime
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

X_test = df['input'].values.tolist()
Y_test = df['output'].values.tolist()

X = np.array(X_test[:-500])
Y = np.array(Y_test[:-500])

classifier = Sequential()
classifier.add(Dense(units = 8, activation = 'relu', input_dim = 4))
classifier.add(Dense(units = 4, activation = 'relu'))
classifier.add(Dense(units = 2, activation = 'relu'))
classifier.add(Dense(units = 1, activation = 'sigmoid'))

classifier.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics=['accuracy'])
history = classifier.fit(X, Y, validation_split = 0.2, batch_size = 1, epochs = 1000, shuffle= True)

#evaluate the model
X_Eva = np.array(X_test[500:])
Y_Eva = np.array(Y_test[500:])
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




# summarize history for accuracy
""" plt.plot(history.history['accuracy'])
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
plt.show() """