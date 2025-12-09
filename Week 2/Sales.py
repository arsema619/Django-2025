# Open sales.txt and read numbers
sales = []

with open("sales.txt", "r") as file:
    for line in file:
        line = line.strip()
        try:
            number = int(line)
            sales.append(number)
        except ValueError:
            print(f"Ignored invalid entry: {line}")

print("Valid sales numbers:", sales)
