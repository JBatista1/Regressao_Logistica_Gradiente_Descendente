import  numpy as np

class Prediction:
    def __init__(self, X_test, Y_test, W, threshold = 5):
        self.X = X_test
        self.Y = Y_test
        self.W = np.array(W)
        self.threshold = threshold
        self.prediction()

    def prediction(self):
        size = len(self.X)
        acurracy = 0

        for i in range(size):
            sumatory = 0
            result = 0
            for j in range(len(self.W[0])):
                sumatory += self.X[i][j]*self.W[0][j]
            print(sumatory)
            if sumatory >= self.threshold:
                result = 1
            if result == self.Y[i]:
                print("a")
                acurracy += 1

        print(acurracy/size)
