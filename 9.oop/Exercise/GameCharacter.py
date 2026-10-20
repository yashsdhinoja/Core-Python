class GameCharacter: # class define
    server_region = "North America" # class Attribute

    def __init__(self, name, role, level): # Constructor & Instance Attributes
        self.name = name
        self.role = role
        self.level = level

    def level_up(self, levels_gained): # Instance Method
        self.level += levels_gained
        print(f"{self.name} leveled up ! New level is {self.level}.")

    @staticmethod # static method
    def server_status():
        print("Server is currently Online and stable.")

GC1 = GameCharacter("Yash", "Chess", 5) # Object Creation
GC2 = GameCharacter("Harsh", "BGMI", 4) # Object Creation

print("="*40)
print(GameCharacter.server_region) # Execution
GC1.level_up(1) # Execution
GC1.server_status() # Execution
print("="*40)
print(GameCharacter.server_region) # Execution
GC2.level_up(3) # Execution 
GC2.server_status() # Execution
print("="*40)