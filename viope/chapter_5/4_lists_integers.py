def lists_integers():
    # Initialize an empty list to store numbers
    numbers = []
    limit = 5  # Limit of 5 integers

    # Input 5 integers from the user
    while limit > 0:
        number = int(input("Enter an integer: "))  # Convert input to integer
        numbers.append(number)  # Add the integer to the list
        limit -= 1

    # Sort numbers in descending order
    numbers.sort(reverse=True)
    print()
    # Print the numbers with a space after each number (including the last one)
    for num in numbers:
        print(num, end=" ")  # Use end=" " to ensure a trailing space after each number


# Call the function to execute the program
if __name__ == "__main__":
    lists_integers()
