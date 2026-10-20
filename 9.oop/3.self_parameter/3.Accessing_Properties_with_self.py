class Car:
    def __init__(owner, brand, model, year):
        owner.brand = brand
        owner.model = model
        owner.year = year

    def display_info(owner):
        print(f"{owner.brand} {owner.model} {owner.year}")

c1 = Car("Mustang","GT",2018)
c1.display_info()