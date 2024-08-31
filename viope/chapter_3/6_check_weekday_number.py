# Ask the user to enter a weekday number
user_input = input("Enter a weekday number: ")

try:
    # Attempt to convert the input to an integer
    weekday_number = int(user_input)

    # Check if the number is between 1 and 7
    if 1 <= weekday_number <= 7:
        print("OK")
    else:
        print("Please enter an integer between 1 and 7")
except ValueError:
    # If a ValueError occurs, the input is not an integer
    print("Please enter an integer between 1 and 7")
