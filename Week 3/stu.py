class Student:
    def __init__(self):
        self.__grade = None   # private attribute

    def set_grade(self, grade):
        self.__grade = grade

    def get_grade(self):
        return self.__grade

# create object
student1 = Student()

# set and get grade
student1.set_grade("A")
print("Grade:", student1.get_grade())
