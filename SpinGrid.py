from Spin import Spin

class SpinGrid():
    
    def __init__(self,height,width,ini_temp):
        self.__height = height
        self.__width = width
        self.__temperature = ini_temp
        self.__spin_numb = self.__height*self.__width
        self.__grid=[]
        self.spingenerate()

    def get_temperature(self):
        return self.__temperature
    
    def spingenerate(self):
        for i in range(1,self.__height+1):
            for j in range(1,self.__width+1):
                self.__grid += [Spin((i,j))]
