# create a student class that stores a list of grades and has a method to compute the average grade.

# class
class Average_Grade:
    def __init__(self, name): # parameter
        self.name = name
        self.grades = [45,98,90]

    # methods
    def add_grade(self, grade):
        self.grades.append(grade)

    def Avg_mesuured(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)

AG = Average_Grade("Yash")
print(AG.name, "\t")
print(AG.Avg_mesuured())

