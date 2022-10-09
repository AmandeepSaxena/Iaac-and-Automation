class Person(object):
    def __init__(self,name,age):
        self.__age = age
        self.__name = name
        return None
    def display(self):
        print(f'name is : {self.__name} and age is {self.__age}')
        return None
p = Person('Aman','10')
p.display()
'''
p.__age # this is will not work so remove this
__variable name or __display()- method name - means they are private and can be used inside class only

'''


