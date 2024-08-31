def double_factorial(n):
    # Handle the case when n is 0 or 1
    if n == 0:
        return 1
    # Determine parity of n
    is_even = n % 2 == 0
    result = 1

    # Compute the double factorial
    for i in range(n, 0, -2):
        result *= i

    return result


# Input from the user
try:
    number = int(input("Enter a non-negative integer: "))
    if number < 0:
        print("Please enter a non-negative integer")
    else:
        result = double_factorial(number)
        print(f"{number}!! = {result}")
except ValueError:
    print("Please enter a non-negative integer")
