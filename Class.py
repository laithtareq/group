class Computer:
    RAM = 20
    def brand():
        return "HP"

class Calculation:
    def __init__(self,**kwargs): # kwargs = {"x":1,"y":5}
        self.x = kwargs['x']
        self.y = kwargs['y']
    def Sum(self):
        return self.x+self.y
    def Sub(self):
        return self.x-self.y
    def Mul(self,w):
        return self.x*self.y*w
    def Squar(self,z):
        return z**2

