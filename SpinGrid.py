from Spin import Spin

class SpinGrid():

    kb = 1 #Constante de Boltzmann normalisée
    J = 1 #Moment magnétique normalisé en l'absence de champ magnétique extérieur pour tout i,j J = J(ij)

    
    def __init__(self,width,ini_temp):
        self.__width = width
        self.__temperature = ini_temp
        self.__spin_numb = self.__width*self.__width
        self.__grid=[]
        self.spingenerate()

    def get_temperature(self):
        return self.__temperature
    
    def spingenerate(self):
        for i in range(1,self.__width+1):
            line=[]
            for j in range(1,self.__width+1):
                line += [Spin((i,j))]
            self.__grid += [line]
    
    def neightboursum(self,coordinates):
        line,col = coordinates
        sum = self.__grid[(line-1)%self.__width][col].get_value() + self.__grid[(line+1)%self.__width][col].get_value() + self.__grid[line][(col-1)%self.__width].get_value() + self.__grid[line][(col+1)%self.__width].get_value()
        return sum

    def energy(self):
        sum = 0
        for i in range(0,self.__width):
            for j in range(0,self.__width):
                sum += self.__grid[i][j].get_value()*self.neightboursum((i,j))
        sum*=(-1*self.J)/(2*self.__width**2)
        return sum
    
    def magnetization(self):
        sum = 0
        for spinline in self.__grid:
            for spin in spinline:
                sum += spin.get_value()
        return sum

    def up_proportion(self):
        count = 0
        for spinline in self.__grid:
            for spin in spinline:
                if spin.get_value() == 1:
                    count += 1
        return int((count/self.__width**2)*100)
    
    def print(self):
        print("Width = ",self.__width,"\nTemperature = ",self.__temperature)
        for line in self.__grid:
            for col in line:
                col.print()

if __name__ == "__main__":
    A = SpinGrid(10,100)
    print(A.up_proportion())