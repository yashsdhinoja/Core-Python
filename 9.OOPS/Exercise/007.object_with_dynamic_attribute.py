# write a function that takes an object and prints all its instance attribute names and value using __dict__.

class Car:
    def __init__(self, car_name="Mercedes-Benz", car_model="Mayback", car_year=2023):
        self.car_name = car_name
        self.car_modal = car_model
        self.car_year = car_year

    def All_o(obj):
        for car, details in obj.__dict__.items():
            print(f"{car}  =>  {details}")

C = Car()
print(C.All_o())

# output
# car_name  =>  Mercedes-Benz
# car_modal  =>  Mayback
# car_year  =>  2023
# None