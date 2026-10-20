# ==========================================
# 1. THE EXPANDED PARENT CLASSES
# ==========================================
# Parent 1
class Animal:
    kingdom = "Animalia"

    def __init__(self, name, age):
        self.name = name
        self.age = age
    def eat(self):
        print(f"{self.name} is eating food. ")

# Parent 2
class PetRole:
    def play_with_human(self):
        print(f"{self.name} is playing nicely with thier human! " )

# ==========================================
# 2. THE CHILD CLASSES 
# ==========================================
class Dog(Animal, PetRole):
    def __init__(self, name, age, breed):
        super().__init__(name,age)
        self.breed = breed

    def bark(self):
        print(f"{self.name} the {self.breed} cat says Meow !")

class Cat(Animal, PetRole):
    def __init__(self, name, age, color):
        super().__init__(name, age) 
        self.color = color
        
    def meow(self):
        print(f"{self.name} the {self.color} cat says Meow!")

# ==========================================
# 3. ADDING MULTIPLE OBJECTS!
# ==========================================
# By putting our objects in a list, we can create as many as we want

my_pets = [
    Dog(name="Buddy", age=3, breed="Golden Retriever"),
    Dog(name="Pip", age=1, breed="Border Collie"),
    Cat(name="Oliver", age=4, color="Orange"),
    Cat(name="Luna", age=2, color="Black")
]

print("--- Interacting with ALL our Pet Objects ---")

for pet in my_pets:
    print(f"\n Meet {pet.name} (Age: {pet.age})")
    pet.eat()
    pet.play_with_human()

    if isinstance(pet, Dog):
        pet.bark()
    elif isinstance(pet, Cat):
        pet.meow()