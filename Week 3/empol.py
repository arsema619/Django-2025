class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary   # monthly salary

    def annual_salary(self):
        return self.salary * 12

# test
emp1 = Employee("John", 3000)
print("Name:", emp1.name)
print("Annual Salary:", emp1.annual_salary())
