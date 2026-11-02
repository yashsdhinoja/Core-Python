class Employee: # class Define
    company_name = "TechNova Solutions" # class attribute

    def __init__(self, name, role, salary): # constructor & Instance Attributes
        self.name = name
        self.role = role
        self.salary = salary

    def give_raise(self, bouns_amount):  # Instance Method
        self.salary += bouns_amount 
        print(f"New Salary for {self.name} is {self.salary}")

    @staticmethod  # Static Method
    def work_hours():
        print(" Standard work hours are 9 AM to 6 PM. ")

emp1 = Employee("yash", "Msc.IT.", 23000)  # object creation
emp2 = Employee("Anand", "MBA Markerting", 34000) # object creation
emp3 = Employee("Qwerty","Office", 22000)  # object creation

print()
print("=" * 30)
print()

# exection
print(Employee.company_name)
emp1.give_raise(23000)
emp1.work_hours()
print()
print("=" * 30)
print()

# exection
print(Employee.company_name)
emp2.give_raise(12000)
emp2.work_hours()
print()
print("=" * 30)
print()

# execution
print(Employee.company_name)
emp3.give_raise(13000)
emp3.work_hours()