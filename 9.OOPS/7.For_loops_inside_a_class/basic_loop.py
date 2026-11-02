class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def show_marks(self):
        # the loop is inside a method (show methods).
        for m in self.marks: 
            # we loop over {self.marks}, the data that belongs to this object. 
            print(m) # m is a normal temporary variable and does not need self.

s1 = Student("Yash",[45, 55, 78])
s1.show_marks()