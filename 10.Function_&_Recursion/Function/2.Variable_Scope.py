# Variable Scope 
# Variable can be local (inside a function) or global (outside all function).


# Local Scope:
# Variables declared inside a function are local to that function.
def my_function():
    x = 25 # local variable
    print("Decalred inside function : local variable")
    print(x)
my_function() # output 25

# Global Scope:
# Variable declared outside all function are global and can be accessed anywhere in the program.
pi = 3.1415 # Global Variable
def area(r):
    print("Decalred outside function : Global variable")
    return pi * r * r # Accessing global variable
print(area(5)) # output : 78.53750000000001

