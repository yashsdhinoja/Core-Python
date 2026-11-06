# create a 'Point' class with x and y attributes, and implement equality comparsion 
# so two points with the same cooridution are considered equal.

# class 
class compare_two_points:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # methods
    def __eq__(self, other): 
        if not isinstance(other, compare_two_points):
            return NotImplemented
        return self.x == other.x and self.y == other.y


p1 = compare_two_points(1,2)
p2 = compare_two_points(1,2)
p3 = compare_two_points(3,4)

print(p1 == p2)
print(p1 == p3)