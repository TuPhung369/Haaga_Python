while True:
    # Input a month number from the user
    user_input = input("Enter a month number: ")

    try:
        # Attempt to convert the input to an integer
        month_number = int(user_input)

        # Check if the number is between 1 and 12
        if 1 <= month_number <= 12:
            print("OK")
            break  # Exit the loop if the input is a valid month number
        else:
            print(f"{month_number} is not a valid month number\n")
    except ValueError:
        # If a ValueError occurs, the input is not a valid integer
        print(f"'{user_input}' is not a valid month number\n")
