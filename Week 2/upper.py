try:
    with open("message.txt", "r") as file:
        for line in file:
            print(line.upper(), end="")
except FileNotFoundError:
    print("File not found!")
