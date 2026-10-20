class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def printname(self):
        print(self.name)

    def printage(self):
        print(self.age)

p1 = Person("Yash", 23)

p1.printname()
p1.printage()