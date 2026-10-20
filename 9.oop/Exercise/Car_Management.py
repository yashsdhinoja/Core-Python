class Car:

    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def show_details(self):
        print(f"Brand : {self.brand}")
        print(f"Model : {self.model}")
        print(f"Price : {self.price}")

    def start(self):
        print(f"{self.brand} and {self.model} started.")

brand = input("Enter Brand : ")
model = input("Enter Model : ")
price = int(input("Enter price : "))

car = Car(brand, model, price)
car.show_details()
car.start()