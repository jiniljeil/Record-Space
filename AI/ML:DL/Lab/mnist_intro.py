from keras.models import Sequential
from keras.layers import Dense, Activation
from keras.utils import np_utils 
import numpy as np 

np.random.seed(777) 

from keras.datasets import mnist 

nb_classes = 10 # 0 ~ 9 

(x_train, y_train), (x_test, y_test) = mnist.load_data() 

# for using TensorFlow backend. 
x_train = x_train.reshape(x_train.shape[0], x_train.shape[1] * x_train.shape[2]) 
x_train = x_train.astype('float') / 255 

# one_hot 
y_train = np_utils.to_categorical(y_train, nb_classes) 

x_test = x_test.reshape(x_test.shape[0], x_test.shape[1] * x_train.shape[2]) 
x_test = x_test.astype('float') / 255

# one_hot 
y_test = np_utils.to_categorical(y_test, nb_classes) 

model = Sequential() 
model.add(Dense(nb_classes, input_dim=784))
model.add(Activation('softmax')) 

model.summary() 

model.compile(loss='categorical_crossentropy',
              optimzer='sgd',
              metrics=['accuracy']) 

history = model.fit(x_train, y_train, epochs=15) 
score = model.evaluate(x_test, y_test) 

print('\nAccuracy:', score[1])

