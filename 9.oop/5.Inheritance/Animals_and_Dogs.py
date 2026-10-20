# --- THE PARENT CLASS ---
class Animal:
    # 1. CLASS PROPERTY
    # Every single animal we create will share this trait.
    kingdom = "Animalia" 

    def __init__(self, name):
        # 2. INSTANCE PROPERTY
        # Every animal has a name, but it is unique to them ('self').
        self.name = name

    def eat(self):
        print(f"{self.name} is eating food.")


# --- THE CHILD CLASS (INHERITANCE) ---
# We put (Animal) in parentheses to tell Python: "Dog inherits from Animal"
class Dog(Animal):
    
    def __init__(self, name, breed):
        # 3. THE super() FUNCTION
        # Instead of writing 'self.name = name' again, we let the Animal 
        # parent class handle it using super().
        super().__init__(name) 
        
        # Now we add the property that is specific ONLY to Dogs.
        self.breed = breed

    # We can also create methods unique to the Dog class
    def bark(self):
        print(f"{self.name} says Woof!")

# ==========================================
# Let's test it out!
# ==========================================

# Create a Dog instance
my_dog = Dog(name="Buddy", breed="Golden Retriever")

# Accessing the Class Property (inherited from Animal)
print(f"Kingdom: {my_dog.kingdom}")  # Output: Kingdom: Animalia

# Accessing Instance Properties
print(f"Name: {my_dog.name}")        # Output: Name: Buddy
print(f"Breed: {my_dog.breed}")      # Output: Breed: Golden Retriever

# Using methods
my_dog.eat()                         # Output: Buddy is eating food. (Inherited from Animal)
my_dog.bark()                        # Output: Buddy says Woof! (Specific to Dog)

# # --- THE PARENT CLASS ---
# class Animal:
#     kingdom = "Animalia" 

#     def __init__(self, name):
#         self.name = name

#     def eat(self):
#         print(f"{self.name} is eating food.")

# # --- THE CHILD CLASS (INHERITANCE) ---
# class Dog(Animal):
#     def __init__(self, name, breed):
#         super().__init__(name) 
#         self.breed = breed

#     def bark(self):
#         print(f"{self.name} says Woof!")

# # ==========================================
# # Let's add User Input!
# # ==========================================

# print("Welcome to the Dog Creator!")

# # 1. Ask the user for the dog's name and breed using input()
# user_name = input("Please enter your dog's name: ")
# user_breed = input("Please enter your dog's breed: ")

# # 2. Pass those new variables into our Dog class
# my_dog = Dog(name=user_name, breed=user_breed)

# # 3. Watch it work!
# print("\n--- Dog Created Successfully! ---")
# print(f"Kingdom: {my_dog.kingdom}")  
# print(f"Name: {my_dog.name}")        
# print(f"Breed: {my_dog.breed}")      

# # Using inherited and specific methods
# my_dog.eat()                         
# my_dog.bark()