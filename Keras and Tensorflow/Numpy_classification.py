import numpy as np
import matplotlib.pyplot as plt
from ANN_from_scratch import neural_network

#Data set for training and prediction

data1 = np.random.randn(400,2) + np.array([1.4,2.5]) #offset, add constant values
data2 = np.random.randn(400,2) + np.array([-2.2,1.6])
data = np.vstack((data1, data2))
nrd1,ncd_x = data1.shape
nrd2,ncd_o = data2.shape

label1 = np.zeros((nrd1,1),dtype=np.float32)
label2 = np.ones((nrd2,1),dtype=np.float32)
labels = np.vstack ((label1, label2))

#Selecting 70% randomly 
randomVector = np.random.permutation(nrd1+nrd2)
NmbForTraining = int((nrd1+nrd2)*0.7)
train_x = data[randomVector[:NmbForTraining],:]
test_x = data[randomVector[NmbForTraining:],:]
train_y = labels[randomVector[:NmbForTraining],:]
test_y = labels[randomVector[NmbForTraining:],:]

#----------- Part for neural network ---------------

##data normalization
#x_all = x_all/24 # np.max(x_all)
#y = y/100
##Splitting
#x = np.split(x_all,[3])[0]
#x_test = np.split(x_all,[3])[1]

ann = neural_network(NeuronCount=20)
numOfIterations = 1000
loss = []

for i in range(0,numOfIterations):
    print(f'{i}/{numOfIterations}')
    err = np.mean(np.sqrt(np.power(train_y-ann.forward(train_x),2)))
    loss.append(err)
    print(f'Loss:{err}')
    ann.train(train_x,train_y)

ann.predict(test_x)
minX = np.min(data[:,0])
maxX = np.max(data[:,0])
minY = np.min(data[:,1])
maxY = np.max(data[:,1])

vectorX = np.linspace(minX, maxX,100)
vectorY = np.linspace(minY, maxY,100)
for i in range(0,len(vectorX)):
    for j in range(0,len(vectorY)):
        prediction = ann.predict([[vectorX[i],vectorY[j]]])
        if prediction[0]<= 0.5:
            color = 'yellow'
        else: 
            color = 'brown'
        plt.plot(vectorX[i], vectorY[j],'s',color=color, mfc=color,mec = color, alpha=0.5)



plt.plot(data1[:,0],data1[:,1],"*",color="black")
plt.plot(data2[:,0],data2[:,1],"o",color="black")
plt.grid(True)
plt.show()

