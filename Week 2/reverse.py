grades = {"John": "A", "Sara": "B", "Musa": "A"}

new_dict = {}

for name, grade in grades.items():
    if grade not in new_dict:
        new_dict[grade] = []
    new_dict[grade].append(name)

print(new_dict)
