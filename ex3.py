import  keras
import pandas as pd
import numpy as np

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

inside_data = pd.read_excel('processed_inside/114833.xlsx')
outside_data = pd.read_excel('processed_outside/141235.xlsx')

inside = changeToList(inside_data)
outside = changeToList(outside_data)

y_inside = []
y_outside = []
for i in range(len(inside)):
    y_inside.append(1)
for g in range(len(outside)):
    y_outside.append(0)

Y_test = y_inside[1500:] + y_outside[-100:]
Y_test = np.array(Y_test)

X_test = inside[1500:] + outside[-100:]
X_test = np.array(X_test)

model = keras.models.load_model('models/model_5')
loss, accuracy = model.evaluate(X_test, Y_test)
#print(model)
