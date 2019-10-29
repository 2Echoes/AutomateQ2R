import numpy as np

class SpinGrid():

    def __init__(self,hauteur,largeur,temp_ini):
        self.__hauteur = hauteur
        self.__largeur = largeur
        self.__temperature = temp_ini
        # self.__energie
        # self.__probabilite = 
        self.__grid = self.__grid = np.random.choice((-1,1),(hauteur,largeur))


    @property
    def hauteur(self):
        return self.__hauteur
    @property
    def largeur(self):
        return self.__largeur
    @property
    def temperature(self):
        return self.__temperature
    @property
    def grid(self):
        return self.__grid

    @grid.setter
    def grid(self,hauteur,largeur):
        self.__grid = np.random.choice((-1,1),(hauteur,largeur))

        

        
"""     @property
    def energie(self):
        return self.__energie
    @property
    def probabilite(self):
        return self.__probabilite """
    




if __name__=='__main__':
    A = SpinGrid(10,10,100)
    print(A.grid)