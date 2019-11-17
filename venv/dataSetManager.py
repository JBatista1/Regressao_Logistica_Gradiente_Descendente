import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split


class DataSetManager:

    def __init__(self):
        self.iris = self.__load_dataset()
        self.X, self.Y = self.__splitDataset()

    def get_data_X_Y_for_train_and_test(self):
        X_train, X_test, Y_train, Y_test = train_test_split(self.X, self.Y, test_size=0.33, random_state=42)
        return X_train,X_test,Y_train,Y_test

    def __load_dataset(self):
        dataset = datasets.load_iris()
        return dataset

    def __convert_to_binary_rating(self, y):
        binaryArray = np.where(y == 0, 0, 1)
        return binaryArray

    def __splitDataset(self):
        X = self.iris.data
        Y = self.iris.target
        Y  = self.__convert_to_binary_rating(Y)
        return X, Y






