import pandas as pd
import numpy as np
from keras.models import Sequential
from keras.layers import Dense


b = []
for i in range(4):
    b.append(list(np.array(pd.read_json(str(i+1)))))

aug_out = []
for i in b:
    for e in i:
        aug_out.append(e)

aug_in = list(np.array(pd.read_json('5')))

y_inside = []
y_outside = []
for i in range(len(aug_in)):
    y_inside.append(1)
for g in range(len(aug_out)):
    y_outside.append(0)

Y_train = y_inside+ y_outside
X_train = aug_in + aug_out


suffled_data = {'input': X_train, 
                'output': Y_train}

df= pd.DataFrame(suffled_data)
df = df.sample(frac = 1)

X_test = df['input'].values.tolist()
Y_test = df['output'].values.tolist()

X = np.array(X_test[:-100])
Y = np.array(Y_test[:-100])

classifier = Sequential()
classifier.add(Dense(units = 8, activation = 'relu', input_dim = 4))
classifier.add(Dense(units = 4, activation = 'relu'))
classifier.add(Dense(units = 2, activation = 'relu'))
classifier.add(Dense(units = 1, activation = 'sigmoid'))
classifier.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics=['accuracy'])

history = classifier.fit(X,
                        Y, 
                        validation_split = 0.2,
                        batch_size = 1, 
                        epochs = 500, 
                        shuffle= True)

#evaluate the model
X_Eva_in = np.array(pd.read_excel('data_19jan/5x5_16/1545.xlsx'))
Y_Eva_in = np.array([1 for i in range(len(X_Eva_in))])
loss, accuracy = classifier.evaluate(X_Eva_in, Y_Eva_in)

result = classifier.predict(X_Eva_in)
print(len([e for e in result if e > 0.5])/len(result))

X_Eva_out = np.array(pd.read_excel('data_19jan/15547x7_out.xlsx'))
Y_Eva_out = np.array([0 for i in range(len(X_Eva_out))])
loss, accuracy = classifier.evaluate(X_Eva_out, Y_Eva_out)

result = classifier.predict(X_Eva_out)
print(len([e for e in result if e > 0.5])/len(result))
