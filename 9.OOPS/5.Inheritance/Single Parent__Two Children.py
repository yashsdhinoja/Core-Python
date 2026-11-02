# ==========================================
# 1. THE PARENT CLASS
# ==========================================
class Car:
    Model="Mercedes" # Class property shared by all animals [cite: 14, 15]

    def __init__(self, name):
        self.name = name  # Instance property unique to the object [cite: 16]

    def Owner(self):
        print(f"{self.name} is the Owner of Car ") 

# ==========================================
# 2. THE CHILD CLASSES (Hierarchical Inheritance)
# ==========================================
# Child 1
class Mercedes(Car):
    def __init__(self, name, year):
        # super() asks the Animal parent to set up the name [cite: 10, 11]
        super().__init__(name)
        self.year = year

    def karl_Benz(self):
        print(f"{self.name} is a Karl Benz")

# Child 2
class Mustarg(Car):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color

    def orange(self):
        print(f"{self.name} ")

# ==========================================
# 3. TESTING IT OUT
# ==========================================

MM = Mercedes(name="Mercedes-Maybach", year="1908")
Ford = Mustarg(name="Ford Mustarg", color="Yellow")

MM.Owner()
MM.karl_Benz()

Ford.Owner()
Ford.orange()   