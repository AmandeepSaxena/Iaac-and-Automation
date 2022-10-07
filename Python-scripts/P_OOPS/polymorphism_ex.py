#!bin/python3
class Tomcat:
    def __init__(self,name,version):
        self.name = name
        self.version = version
        return None
    def display(self):
        print(f'This is from tomcat class')
        print(self.name)
        print(self.version)
        return None    

class Apache:
    def __init__(self,name,version):
        self.name = name
        self.version = version
        return None
    def display(self):
        print("This is from Apache class")
        print(self.name)
        print(self.version)
        return None  

t = Tomcat('/path/conf','4.5')
a = Apache('/path/conf/lol.xml','4.45')
t.display()
a.display()


