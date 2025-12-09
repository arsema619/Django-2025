def my_sqrt(x):
    i = 0
    while (i * i) <= x:
        i += 1
    return i - 1

# Examples
print(my_sqrt(4))  # 2
print(my_sqrt(8))  # 2
