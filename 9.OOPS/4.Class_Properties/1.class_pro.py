class Utuir:
    def __init__(self,name):
        self.name = name

class Properties:
    def __init__(self,name,age):
        self.name = name
        self.age = age

p1 = Properties("Yash", 23)
p2 = Utuir("Dhinoja")

print(p1.name)
print(p1.age)

print(p2.name)