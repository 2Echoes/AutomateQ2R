import numpy as np

class Spin():

    def __init__(self,coord):
        self.__value = np.random.choice([-1,1])
        self.__coordinates = coord
    
    def get_coordinates(self):
        return self.__coordinates
    
    def get_value(self):
        return self.__value
    
    def print(self):
        print("coordinates ",self.__coordinates," value = ",self.__value)
