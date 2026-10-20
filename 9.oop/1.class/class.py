# CLASS: A blueprint for creating objects
class Car:
    # CLASS ATTRIBUTES: Variables shared by all objects created from this class
    model = "Mercedes"
    year = "2009"

    # CONSTRUCTOR (__init__): Special method called automatically when creating an object
    # PARAMETERS: 'self' refers to the object instance; 'name' and 'number' are inputs passed during object creation
    def __init__(self, name, number):
        # INSTANCE ATTRIBUTES: Variables unique to each individual object created
        self.name = name
        self.number = number

    # STATIC METHOD: Function grouped inside a class that doesn't use 'self' (instance data)
    @staticmethod
    def acc():
        print("ABC College !!!")

    # INSTANCE METHOD: Regular method that accesses or modifies object data using 'self'
    def hello(self):
        print("hello ", self.name)


# OBJECT (INSTANCE): Creating an actual usable object 'c1' from the 'Car' blueprint
c1 = Car("Mustang", 45)

# ACCESSING AN INSTANCE ATTRIBUTE
print(c1.name)  # Prints: Mustang

# CALLING AN INSTANCE METHOD
c1.hello()  # Prints: hello  Mustang