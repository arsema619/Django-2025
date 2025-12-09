def fizz_buzz(n):
    result = []
    for i in range(1, n+1):
        if i % 3 == 0 and i % 5 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(i))
    return result

# Examples
print(fizz_buzz(3))  # ["1", "2", "Fizz"]
print(fizz_buzz(5))  # ["1", "2", "Fizz", "4", "Buzz"]
