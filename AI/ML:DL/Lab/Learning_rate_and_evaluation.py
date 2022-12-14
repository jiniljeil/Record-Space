from keras.models import Sequential 
from keras.layers import Dense, Activation 
from tensorflow.keras.optimizers import SGD
import numpy as np 

np.random.seed(777) # for reproducibility

x_data = np.array([[1, 2, 1], [1, 3, 2], [1, 3, 4], [1, 5, 5],
          [1, 7, 5], [1, 2, 5], [1, 6, 6], [1, 7, 7]])
y_data = np.array([[0, 0, 1], [0, 0, 1], [0, 0, 1], [0, 1, 0],
          [0, 1, 0], [0, 1, 0], [1, 0, 0], [1, 0, 0]])

# Evaluation our model using this test dataset
x_test = np.array([[2, 1, 1], [3, 1, 2], [3, 3, 4]])
y_test = np.array([[0, 0, 1], [0, 0, 1], [0, 0, 1]])

model = Sequential() 
model.add(Dense(3, input_dim=3))
model.add(Activation('softmax')) 

model.summary() 

"""
Learning rate default value: 0.01

if overshooting occurs in the training, 
we should revise the learning rate. 

Diverge -> lower 
Almost no change -> higher 
"""
model.compile(loss='categorical_crossentropy', 
              optimizer=SGD(lr=0.01),
              metrics=['accuracy']) 

history = model.fit(x_data, y_data, epochs=2000) 

predictions = model.predict(x_test) 
score = model.evaluate(x_test, y_test) 

print('Prediction: ', [np.argmax(prediction) for prediction in predictions]) 
print('Accuracy: ', score[1])