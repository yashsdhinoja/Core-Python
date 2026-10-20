class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def greef(self):
        print("Hello " + self.name + " Your Age is " + str(self.age))

P1 = Person("Yash", 20)
P1.greef()