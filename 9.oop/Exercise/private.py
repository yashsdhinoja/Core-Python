class Person:
    __name = "Yash"
    #     print(p1.__name)
    #           ^^^^^^^^^
    # AttributeError: 'Person' object has no attribute '__name'

    def __hello():
        print("Hello World !")

p1 = Person()
# print(p1.__name)
print(p1.__hello())