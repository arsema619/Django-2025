def is_palindrome(x):
    # Negative numbers cannot be palindrome
    if x < 0:
        return False

    # Convert number to string and compare with its reverse
    return str(x) == str(x)[::-1]

# Examples
print(is_palindrome(121))   # True
print(is_palindrome(-121))  # False
