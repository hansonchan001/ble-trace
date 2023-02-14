import pandas as pd
import numpy as np
from keras.models import Sequential
from keras.layers import Dense

def changeToList(file):
    n = []
    for i in range(len(file)):
        c = []
        for j in range(len(file.iloc[0])):
            c.append(file[j][i])
        b = np.array(c)
        n.append(b)

    return n

inside = pd.read_excel('aug_5x5_inside.xlsx')
outside = pd.read_excel('aug_5x5_outside.xlsx')

inside = changeToList(inside)
outside = changeToList(outside)

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

X = np.array(X_test)
Y = np.array(Y_test)

classifier = Sequential()
classifier.add(Dense(units = 16, activation = 'relu', input_dim = 4))
classifier.add(Dense(units = 8, activation = 'relu'))
classifier.add(Dense(units = 4, activation = 'relu'))
classifier.add(Dense(units = 2, activation = 'relu'))
classifier.add(Dense(units = 1, activation = 'sigmoid'))
classifier.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics=['accuracy'])

history = classifier.fit(X,
                        Y, 
                        validation_split = 0.2,
                        batch_size = 1, 
                        epochs = 200, 
                        shuffle= True)

#evaluate the model
X_Eva_in = np.array(pd.read_excel('processed_inside/5x5_16.xlsx'))
Y_Eva_in = np.array([1 for i in range(len(X_Eva_in))])
loss, accuracy = classifier.evaluate(X_Eva_in, Y_Eva_in)

result = classifier.predict(X_Eva_in)
print(len([e for e in result if e > 0.5])/len(result))

#X_Eva_out = np.array(pd.read_excel('data_19jan/15547x7_out.xlsx'))
#Y_Eva_out = np.array([0 for i in range(len(X_Eva_out))])
#loss, accuracy = classifier.evaluate(X_Eva_out, Y_Eva_out)
#
#result = classifier.predict(X_Eva_out)
#print(len([e for e in result if e > 0.5])/len(result))
