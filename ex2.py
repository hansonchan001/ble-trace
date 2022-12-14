from tensorflow import keras
import pandas as pd
import numpy as np

model = keras.models.load_model('models/model_6')

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

    return n


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
Y_train = np.array(Y_train)
Y_test = np.array(Y_test)

X_train = inside[:1500] + outside[:-100]
X_test = inside[1500:] + outside[-100:]
X_train = np.array(X_train)
X_test = np.array(X_test)


model = keras.models.load_models('models/model_5')
loss, accuracy = model.evaluate()