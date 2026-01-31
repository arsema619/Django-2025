from abc import ABC, abstractmethod

class Employee(ABC):
    @abstractmethod
    def calculate_salary(self):
        pass

# ❌ This will cause an error if uncommented
# emp = Employee()

class PartTimeEmployee(Employee):
    def calculate_salary(self):
        return 2000   # part-time salary

# test
pt = PartTimeEmployee()
print(pt.calculate_salary())
