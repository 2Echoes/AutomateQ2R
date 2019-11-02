import numpy as np

class SpinGrid():

    J = 1 # Normalisée en l'absence de champ magnétique extérieur pour tout i,j J = J(ij)
    kb = 1 #Constante de Boltzmann normalisée

    def __init__(self,height,width,ini_temp):
        self.__height = height
        self.__width = width
        self.__temperature = ini_temp
        self.__spinNumber = height*width
        self.__spingen = self.spin_generator()


    @property
    def height(self):
        return self.__height
    @height.setter
    def height(self,hgt):
        self.__height = hgt

    @property
    def width(self):
        return self.__width
    @width.setter
    def width(self,wdth):
        self.__width = wdth

    @property
    def temperature(self):
        return self.__temperature
    @temperature.setter
    def temperature(self,temp):
        self.__temperature = temp

    @property
    def spinNumber(self):
        return self.__spinNumber
    @spinNumber.setter
    def spinNumber(self,number):
        if number == self.height * self.width:
            self.__spinNumber = number

    def print(self):
        print("height = ",self.height," width = ",self.width,"\nSpin number = ",self.spinNumber,"\ntemperature = ",self.temperature)

    def spin_generator(self):
        Spingrid = np.zeros(self.height,self.width)
        for line in range(1,self.height+1):
            for col in range(1,self.width+1):
                Spingrid[line,col] = Spin(line,col,grid=self)
    
    
class Spin():
    
    def __init__(self,coord,grid):
        self.__value = np.random.choice([-1,1])
        self.__coordinates = coord
        self.__grid = grid

    @property
    def value(self):
        return self.__value
    @value.setter
    def value(self,SpinV):
        self.__value = SpinV
    
    @property
    def coordinates(self):
        return self.__coordinates
    @coordinates.setter
    def coordinates(self,coord):
        if (type(coord) == tuple or type(coord) == list or type(coord) == np.ndarray) and len(coord) == 2:
            self.__coordinates = coord

    def print(self):
        print('coordinates = ',self.coordinates,'   Spin = ',self.__value)
    
    def neighboorsum(self):
        sum = 


if __name__ == '__main__':    