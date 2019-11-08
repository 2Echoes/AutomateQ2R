import numpy as np

class Spin():

    def __init__(self,coord):
        self.__value = np.random.choice([-1,1])
        self.__coordinates = coord


