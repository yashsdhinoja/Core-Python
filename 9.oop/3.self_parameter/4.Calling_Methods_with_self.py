class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return "Hello, " + self.name

    def qwerty(self):
        return "Hello, " + str(self.age)

    def welcome(self):
        age = self.qwerty()
        message = self.greet()
        print(message + " ! Welcome to SWEC \n")
        print("Your Age is " + age)

p1 = Person("yash", 23)
p1.welcome()