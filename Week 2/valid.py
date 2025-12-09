total = 0

with open("numbers.txt", "r") as file:
    for line in file:
        line = line.strip()
        try:
            total += int(line)
        except ValueError:
            print(f"Ignored invalid line: {line}")

print("Sum =", total)
