class Employee:
    company = "Yash"

    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def get_self(self):
        # ( < ) = less 
        # ( > ) = greater  
        if self.salary >= 50000:
            return f"Competent Man"
        elif self.salary >= 10000:
            return f"Helper Man"
        else:
            return f"New Person" 

    def start(self):
        print(f"{self.name} and Age is {self.age} and these {self.salary}.")

name = input("Enter Name : ")
age = input("Enter Age : ")
salary = int(input("Enter Salary : "))

emp = Employee(name, age, salary)
emp.get_self()
emp.start()