class Person:
    def __init__(abcd, zzz, xxx):  # The __init__() method is called automatically every time the class is being used to create a new object.
        abcd.zzz = zzz
        abcd.xxx = xxx

p1 = Person("yash",23)
print(p1.zzz)
print(p1.xxx)
print(p1)