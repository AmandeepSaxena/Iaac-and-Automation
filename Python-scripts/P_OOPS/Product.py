#implementing __call__  built in function
#using this instance become functions and can be called like functions
class Product:
    def __init__(self):
        print("Instance Created")

    def __call__(self, a,b):
        print(a*b)


#instance created
p = Product()
#instance called
p(4,5)