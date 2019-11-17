from dataSetManager import DataSetManager
class Main:
    def __init__(self):
        data = DataSetManager()
        self.X_train, self.X_test, self.Y_train, self.Y_test = data.get_data_X_Y_for_train_and_test()

    def train(self):
        print (self.X_train)
        print (self.Y_train)



main = Main()
main.train()