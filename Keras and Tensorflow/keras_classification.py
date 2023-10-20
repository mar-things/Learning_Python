import numpy as np
import matplotlib.pyplot as plt
import tensorflow a















TrainFlag = True
if TrainFlag:
    ann = Sequential()
    ann.add(Dense(7,input_dim=2,activation='relu'))#first hidden layer
    ann.add(Dense(1,activation='sigmoid'))
    ann.compile(loss=tf.keras.metrics.binary_crossentropy(), optimizer='adam',
                metrics=['accuracy'])
    #Start  training
    ann.fit(train_x,train_y,epochs=300,verbose=5)
    

