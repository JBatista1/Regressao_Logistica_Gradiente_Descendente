class Prediction:
    def __init__(self, X_train, Y_train,learning_rate, epoch = 1000):
        self.X = np.array(X_train)
        self.Y = np.array(Y_train)
        self.W = self.__create_weight_array()
        self.learning_rate = learning_rate
        self.epoch = epoch
        self.__train()
        print(self.W)