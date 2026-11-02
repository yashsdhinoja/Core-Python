class Car:
    def __init__(self,name,well):
        self.name = name
        self.well = well

    def move(self):
        print("! Drive")

class Boart:
    def __init__(self, name, model):
        self.name = name
        self.model = model

    def move(self):
        print("! Move Fast")

car1 = Car("Yash","Hash")
boat1 = Boart("Yash","GSL")

for x in (car1, boat1):
    x.move()

for y in (car1.name, boat1.name):
    print(y)

for f in (car1.well, boat1.model):
    print(f)