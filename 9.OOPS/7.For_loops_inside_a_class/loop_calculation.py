class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def total(self):
        result = 0
        for m in self.marks:
            result = result + m
        return result

    def average(self):
        return self.total() / len(self.marks)

S1 = Student("Ravi", [44, 78, 62])
print(S1.total())
print(S1.average())