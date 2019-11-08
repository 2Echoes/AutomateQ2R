import numpy as np


class SpinGrid():

    # Normalisé en l'absence de champ magnétique extérieur pour tout i,j J = J(ij)
    J = 1
    kb = 1  # Constante de Boltzmann normalisée

    def __init__(self, height, width, ini_temp):
        self.__height = height
        self.__width = width
        self.__temperature = ini_temp
        self.__spinNumber = self.height*self.width
        self.__grid = []
        self.spin_generator()

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, hgt):
        self.__height = hgt

    @property
    def width(self):
        return self.__width
    
    def findSpin(self, x, y):
        return self.__grid[x][y]

    @width.setter
    def width(self, wdth):
        self.__width = wdth

    @property
    def temperature(self):
        return self.__temperature

    @temperature.setter
    def temperature(self, temp):
        self.__temperature = temp

    @property
    def spinNumber(self):
        return self.__spinNumber

    @spinNumber.setter
    def spinNumber(self, number):
        self.__spinNumber = number

    def print(self):
        print("height = ", self.height, " width = ", self.width,
              "\nSpin number = ", self.spinNumber, "\ntemperature = ", self.temperature)

    def spin_generator(self):
        for i in range(1, self.width+1):
            for j in range(1, self.height+1):
                yield Spin((j, i), self)

    def spin_generator(self):
        for i in range(1, self.width+1):
            for j in range(1, self.height+1):
                self.__grid[i][j] = Spin()


class Spin():

    def __init__(self, coord, grid):
        self.__value = np.random.choice([-1, 1])
        self.__coordinates = coord
        self.__Sgrid = grid

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, SpinV):
        self.__value = SpinV

    @property
    def coordinates(self):
        return self.__coordinates

    @coordinates.setter
    def coordinates(self, coord):
        if (type(coord) == tuple or type(coord) == list or type(coord) == np.ndarray) and len(coord) == 2:
            self.__coordinates = coord

    @property
    def Sgrid(self):
        return self.__grid

    @Sgrid.setter
    def grid(self, grid):
        self.__grid = grid

    def print(self):
        print('coordinates = ', self.coordinates, '   Spin = ', self.__value)

    def neighboorsum(self):
        line = self.coordinates[0]
        col = self.coordinates[1]


if __name__ == '__main__':
    grille = SpinGrid(2, 2, 100)
    grille.print()
