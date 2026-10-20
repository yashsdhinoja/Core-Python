# ==========================================
# 1. THE PARENT CLASSES
# ==========================================
# Parent 1

class Animale:
    kingdom = "Animalia"
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name}is eating food.")

# Parent 2
class RolePlaying:
    def fun_and_food(self):
        print(f"{self.name} is playing nicely with their human!")

# ==========================================
# 2. THE CHILD CLASSES (Multiple Inheritance)
# ==========================================
# Child 1: Inherits from BOTH Animal and PetRole using a comma

class Dog(Animale, RolePlaying):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def Spas(self):
        print(f"{self.name} Says Woof !!!")

# Child 2: Also inherits from BOTH Animal and PetRole

class Cat(Animale, RolePlaying):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color

    def Meom(self):
        print(f"{self.name} Says Meon !!!")

# ==========================================
# 3. TESTING IT OUT
# ==========================================

my_dog = Dog(name="Saviti", breed="Golden Retivement")
my_cat = Cat(name="Oliver", color="Orange")

my_dog.eat()
my_dog.fun_and_food()
my_dog.Spas()

my_cat.eat()
my_cat.fun_and_food()
my_cat.Meom()