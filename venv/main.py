from dataSetManager import DataSetManager
from logisticRegression import LogisticRegression
class Main:
    def __init__(self):
        data = DataSetManager()

        self.X_train, self.X_test, self.Y_train, self.Y_test = data.get_data_X_Y_for_train_and_test()

        logisticRegression = LogisticRegression(X_train=self.X_train, Y_train = self.Y_train, learning_rate = 0.00001)

    def train(self):
        print ("Nada")



main = Main()
main.train()