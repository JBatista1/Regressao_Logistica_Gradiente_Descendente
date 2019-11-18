import numpy as np
import random

class LogisticRegression():

    def __init__(self, X_train, Y_train,learning_rate, epoch = 1000):

        self.X = np.array(X_train)
        self.Y = np.array(Y_train)
        self.W = self.__create_weight_array()
        self.learning_rate = learning_rate
        self.epoch = epoch
        self.__train()

    def get_value_W(self):
        return self.W

    def __create_weight_array(self):
        size = len(self.X[0])
        array = np.random.rand(1,size)
        return array
    # Printo graphic
    def __binat_cross_entropy(self, W, X, y):
        size = len(X)
        XtW = self.__scalar_product(X,W)
        equals_one = np.multiply(-y,np.log(self.__sigmoid(XtW)))
        equals_zero = np.multiply((1-y), np.log(self.__sigmoid(XtW)))
        result = np.sum(equals_one-equals_zero)
        result = result/size
        return result

    def __sigmoid(self, scalar):
        return 1/(1 + np.exp(-scalar))

    def __train(self):
        print("Train logistic Regression...")
        for i in range(self.epoch):
            self.W = self.W - (self.learning_rate) * np.sum((self.__sigmoid(self.X@self.W.T) - self.Y)*self.X, axis= 0)

    def __scalar_product(self, X, W):
        size = len(X)
        scalar = 0.0
        for i in range(size):
            scalar += X[i]*self.W[valueW]
        return scalar

    def prediction(self, X, W, Y, threshold = 0.5):
        print("Test and validation...")
        size = len(X)
        acurracy = 0
        for i in range(size):
            classification = 0
            result = self.__sigmoid(X[i]@W.T)
            if result >= threshold:
                classification = 1
            if classification == Y[i]:
                acurracy += 1
        return (acurracy/size)*100


