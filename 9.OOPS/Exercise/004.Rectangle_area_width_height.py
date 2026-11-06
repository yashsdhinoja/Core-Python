# Create a Rectangle class with width, height, and methods to compute area and perimeter.

# class
class Rectangle:
    #  parameter pass
    def __init__(self, breath, lenght):
        self.breath = breath
        self.lenght = lenght

    # mehtods
    def area_of_object(self):
        return self.breath * self.lenght # 4 * 5 => 20

    def perimeter(self):
        return 2 * (self.breath * self.lenght) # 2 * (4 * 5) => 40

r = Rectangle(4, 5)
print(r.area_of_object())
print(r.perimeter())