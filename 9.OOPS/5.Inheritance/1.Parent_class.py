class Person:
    def __init__(self, fname, lname, number):
        self.firstname = fname
        self.lastname = lname
        self.number = number

    def printname(self):
        print(self.firstname, self.lastname, self.number)

    def printnumber(self):
        print(self.number)
        
class Student(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)

class Number(Person):
    def __init__(self, fname, lname, number):
        super().__init__(fname, lname, number)

x = Person("john","wick",34)
x.printname()