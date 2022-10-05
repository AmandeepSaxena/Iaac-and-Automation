from cgi import print_exception
from pyexpat import model
from unicodedata import name


class Car:
    def __init__(self,name,model,price):
        self.name = name
        self.model = model
        self.price = price

    def moving (self):
        print("car "+self.name+" is moving") 

c = Car("chevo","covett",3033)
c.moving()