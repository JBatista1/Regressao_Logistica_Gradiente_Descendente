import numpy as np
import random

class LogisticRegression:
    def __init__(self, X_train, Y_train,learning_rate, epoch = 1000):
        self.X = np.array(X_train)
        self.Y = np.array(Y_train)
        self.W = self.__create_weight_array(self.X)
        self.learning_rate = learning_rate
        self.epoch = epoch
        value = self.__scalar_product(, valueW = 0)
        print (value)

    def __create_weight_array(self,X):
        size = len(X[0])
        array = []
        for i in range(0, 5):
            if i == 0:
                array.append(0)
            else:
                array.append(random.uniform(0.0, 1.0))
        array = np.array(array)
        return array

    def __trainData(self):
        gradient = self.__create_weight_array(self.W)
        size = len(self.W)-1
        count = 0
        while count < self.epoch:
            for i in random(size):
                scalar = self.__scalar_product(self.X[:,i],i)
                gradient[i] = self.__computes_gradient(scalar)
            
                self.W[i] += self.W[i]+self.learning_rate*gradient


        print ("RRR")

    def __computes_gradient(self, scalar):
        return 1/(1 + np.exp(-scalar))

    def __scalar_product(self, X, columnW):
        size = len(X)
        scalar = 0.0
        for i in range(size):
            scalar += X[i]*self.W[valueW]
        return scalar

