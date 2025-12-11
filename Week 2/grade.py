Alice# Dictionary of student grades
student_grades = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78
}

# Function to get a grade
def get_grade(student_grades, student_name):
    try:
        return student_grades[student_name]
    except KeyError:
        return "Student not found in the system"

# Ask user to enter student name
name = input("Enter the student name: ")

# Get and print the grade
print("Result:", get_grade(student_grades, name))
