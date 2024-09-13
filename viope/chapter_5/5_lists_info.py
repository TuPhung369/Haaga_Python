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

    print("count: ", len(numbers))
    print("min: ", min(numbers))
    print("max: ", max(numbers))
    print("sum: ", sum(numbers))


# Call the function to execute the program
if __name__ == "__main__":
    lists_integers()
