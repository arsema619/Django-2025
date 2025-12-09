student_grades = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78
}

def get_grade(student_grades, student_name):
    try:
        return student_grades[student_name]
    except KeyError:
        return "Student not found in the system"

# Example usage
name = input("Enter student name: ")
print(get_grade(student_grades, name))
