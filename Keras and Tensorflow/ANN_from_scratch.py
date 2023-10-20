import numpy as np
import matplotlib.pyplot as plt
class neural_network(object):
    def __init__(self,NeuronCount):
        #Hyperparameters for ANN strucure
        self.inputSize = 2
        self.outputSize = 1
        self.hiddenSize = NeuronCount #Number of neurons in the hidden layer
        # random weights at the biginning 
            #Input -Hidden layer weights
        self.W1 = np.random.randn(self.inputSize, self.hiddenSize) #(2x3)matrix
            #Hidden layer - output weights
        self.W2 = np.random.randn(self.hiddenSize, self.outputSize) #(3x1)matrix

    def sigmoid(self,s):
        return 1/(1+np.exp(-s)) #sigmoidal function
    
    def forward(self,x):
        self.z = np.dot(x,self.W1)
        self.z2 = self.sigmoid(self.z)
        self.z3 = np.dot(self.z2,self.W2)
        o = self.sigmoid(self.z3)
        return o
    def sigmoidPrime(slef,s):
        return s*(1-s)
    # x - inputs
    # y - Labels or target vector (output)
    # o - output or prediction 
    def backward(self,x,y,o): # Backwards propagation
        self.o_error = y - o 
        self.o_delta = self.o_error*self.sigmoidPrime(o)
        #How much impact to final error has w2
        self.z2_error = self.o_delta.dot(self.W2.T) 
        self.z2_delta = self.z2_error*self.sigmoidPrime(self.z2)


        # ---------- UPDATING THE WEIGHTS ----------
        self.W1 +=x.T.dot(self.z2_delta)# inputs -> hidden
        self.W2 +=self.z2.T.dot(self.o_delta) #hidden -> output
    
    def train(self,x,y):
        o = self.forward(x)
        self.backward(x,y,o)
    def saveWeights(self):
        np.savetxt('w1.txt',self.W1,fmt='%s')
        np.savetxt('w2.txt',self.W2,fmt='%s')
    def predict(self,x_test,printResult=False):
        predict = self.forward(x_test)
        if printResult:
            print("Predicted value: ")
            print('Output value:', f'{self.forward(x_test)}')
        return predict

#Data set for training and prediction
#
#x_all = np.array([[2,9],
#                 [1,5],
#                 [3,6],
#                 [5,10]],dtype=np.float32)
##target vector or labels
#y = np.array([[92],[55],[88]],dtype=np.float32)
#
##data normalization
#x_all = x_all/24 # np.max(x_all)
#y = y/100
##Splitting
#x = np.split(x_all,[3])[0]
#x_test = np.split(x_all,[3])[1]
#
#ann = neural_network(NeuronCount=3)
#numOfIterations = 1000
#loss = []
#for i in range(0,numOfIterations):
#    print(f'{i}/{numOfIterations}')
#    err = np.mean(np.sqrt(np.power(y-ann.forward(x),2)))
#    loss.append(err)
#    print(f'Loss:{err}')
#    ann.train(x,y)
#
#ann.saveWeights()
#ann.predict(x_test)
#
#plt.plot(loss,'-r'),plt.xlabel('Iterations'),plt.ylabel('Loss')
#plt.show()
#