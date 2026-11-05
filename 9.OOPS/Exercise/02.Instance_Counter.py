# Create a class 'Employee' that keeps track of 
# how many Employees objects have been creadted using a class attribute.

class Employee: # class 
    count = 0 # counter to count user.

    def __init__(self, name): #contrutions
        self.name = name 
        Employee.count += 1 # employees count

e1 = Employee("Yash")
e2 = Employee("jiyaa")
e3 = Employee("hrash")

print(f"Total Employees are : {Employee.count}")