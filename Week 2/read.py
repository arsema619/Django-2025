sales = []

with open("sales.txt", "r") as file:
    for line in file:
        line = line.strip()
        try:
            number = int(line)
            sales.append(number)
        except ValueError:
            # skip invalid lines
            print(f"Ignored invalid entry: {line}")

total = sum(sales)
print("Valid sales numbers:", sales)
print("Total sales:", total)
