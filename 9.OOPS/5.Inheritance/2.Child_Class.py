class Person():
    def __init__(self, fname, lname, address):
        self.firstname = fname
        self.lastname = lname
        self.add= address

    def printname(self):
        print(self.firstname, self.lastname, self.add)

class Yash(Person):
    pass

x = Yash("yash", "dhinoja", "4/5, balmukund krupa")
x.printname()