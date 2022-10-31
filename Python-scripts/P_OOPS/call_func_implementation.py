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



'''
another example
class Product(object):
    def __init__(self):
        print("Instance created")
    def __call__(self, *args):
        num = 0
        for i in args:
            num += i
        print(num)

p = Product()
#instance called 

p(4,5)
'''