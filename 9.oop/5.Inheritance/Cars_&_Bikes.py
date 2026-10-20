class Car:
    carname = "Car"
    def __init__(self, name):
        self.name = name

    def vom(self):
        print(f"{self.name} is vom vom in highway.")



class Mercedes(Car):
    def __init__(self, name, year):
        super().__init__(name)
        self.year = year

    def fine(self):
        print(f"{self.name} fina at 235-209 Durham Regional Rd 16, Oshawa, ON L1H 5H8, Canada")



my_car = Mercedes(name="Mercedes-Maybach", year="S 580 4MATIC")

print(f"carname: {my_car.carname} ")
print(f"name: {my_car.name}")
print(f"year: {my_car.year}")

my_car.vom()
my_car.fine()