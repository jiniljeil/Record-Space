from keras.models import Sequential
from keras.layers import Dense
from tensorflow.keras.optimizers import SGD
import numpy as np 

x_data = np.array([[0., 0.],
          [0., 1.],
          [1., 0.],
          [1., 1.]])
y_data = np.array([[0.],
          [1.],
          [1.],
          [0.]])

model = Sequential()
model.add(Dense(1, input_dim=2, activation='sigmoid'))
sgd = SGD(lr=0.1)
model.compile(loss='binary_crossentropy', optimizer=sgd,
              metrics=['accuracy'])
model.summary()
model.fit(x_data, y_data, epochs=50000)

score = model.evaluate(x_data, y_data, verbose=0)
print('Test score:', score[0])
print('Test accuracy:', score[1])