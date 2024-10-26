def positive_sum(numbers):
    # Return the sum of positive numbers in the list
    return sum(num for num in numbers if num > 0)


def main():
    # Initialize an empty list to store user inputs
    numbers = []

    # Input five integers from the user
    for _ in range(5):
        num = int(input("Enter an integer: "))
        numbers.append(num)

    # Call the positive_sum function and get the result
    result = positive_sum(numbers)

    # Print a blank line for separation
    print()

    # Print the result
    print(result)


if __name__ == "__main__":
    main()
