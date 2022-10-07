#!bin/python3
class Tomcat:
    def __init__(self,name,version):
        self.name = name
        self.version = version
        return None
    def display(self):
        print(self.name)
        print(self.version)
        return None    

#Passing class as an object for inheritance
#now Apache class can use display method of class Tomcat
class Apache(Tomcat):
    def __init__(self,name,version):
        self.name = name
        self.version = version
        return None

t = Tomcat('/path/conf','4.5')
a = Apache('/path/conf/lol.xml','4.45')
t.display()
a.display()


