from keras.models import Sequential
from keras.layers import Dense, Activation
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
model.add(Dense(2, input_dim=2, activation='sigmoid')) 
model.add(Dense())
model.add(Dense(1, activation='sigmoid')) 
sgd = SGD(lr=0.1) 
model.compile(loss='binary_crossentropy', 
              optimizer=sgd, 
              metrics=['accuracy']) 

model.summary() 
model.fit(x_data, y_data, epochs=50000) 

predictions = model.predict(x_data) 
# print('Argmax:', predictions.argmax(axis=-1)) 
print(predictions)

score = model.evaluate(x_data, y_data, verbose=0) 
print('Test score:', score[0]) 
print('Test accuracy:',score[1]) 

