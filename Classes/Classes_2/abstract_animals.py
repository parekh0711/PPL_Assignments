from abc import ABC


class Animals(ABC):
    def basic_features(self):
        self.__eyes=2
        self.__legs=4
        self.__ears=2
        self.__nose=1
    def print_features(self):
        print("It has",self.__eyes,"eyes.")
        print("It has",self.__ears,"ears.")
        print("It has",self.__nose,"nose.")
        print("It has",self.__legs,"legs.")
