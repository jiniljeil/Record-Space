from keras.models import Sequential
from keras.layers import Dense, Activation 
from tensorflow.keras.optimizers import SGD
import numpy as np 

np.random.seed(777) 

"""
    Non-normalized inputs
"""
 
xy = np.array([[828.659973, 833.450012, 908100, 828.349976, 831.659973],
               [823.02002, 828.070007, 1828100, 821.655029, 828.070007],
               [819.929993, 824.400024, 1438100, 818.97998, 824.159973],
               [816, 820.958984, 1008100, 815.48999, 819.23999],
               [819.359985, 823, 1188100, 818.469971, 818.97998],
               [819, 823, 1198100, 816, 820.450012],
               [811.700012, 815.25, 1098100, 809.780029, 813.669983],
               [809.51001, 816.659973, 1398100, 804.539978, 809.559998]])

x_data = xy[:, 0:-1] 
y_data = xy[:, [-1]] 

# placeholders for a tensor that will be always fed. 
model = Sequential() 
model.add(Dense(1, input_dim=4)) 
model.add(Activation('linear')) 

model.summary() 

model.compile(loss='mse', 
              optimizer=SGD(lr=1e-5),
              metrics=['accuracy'])  


history = model.fit(x_data, y_data, epochs=100) 

predictions = model.predict(x_data) 
score = model.evaluate(x_data, y_data) 

print('Prediction: ', predictions)
print('Accuracy: ', score[1])  
