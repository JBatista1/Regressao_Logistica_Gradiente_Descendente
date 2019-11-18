from dataSetManager import DataSetManager
from logisticRegression import LogisticRegression
from prediction import Prediction
class Main:
    def __init__(self, classClassify):
        print("Init Class")
        self.classClassfy = classClassify

    def logisticAcurracy(self):
        acurracy = self.__logisictRegression()
        print("Acurracy is", acurracy)
    def __logisictRegression(self):

        data = DataSetManager(self.classClassfy)
        X_train, X_test, Y_train, Y_test = data.get_data_X_Y_for_train_and_test()

        log = LogisticRegression(X_train=X_train, Y_train=Y_train, learning_rate=0.01)
        W = log.get_value_W()
        acurracy = log.prediction(X_test, W, Y_test)
        return acurracy

    def mediaAcurracy(self,numberIteration):
        acurracy = 0
        for i in range(numberIteration):
           acurracy += self.__logisictRegression()
        media = acurracy/numberIteration
        print("Acurracy is", media)

# pass as a parameter the type of flower you want to compare with the others
# 1 = Setosa
# 2 = Versiculor
# 3 = Virginica

main = Main(0)
# main.logisticAcurracy()
main.mediaAcurracy(10)
