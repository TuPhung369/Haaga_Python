# Ask the user to enter an integer
user_input = input("Enter an integer: ")

try:
    # Attempt to convert the input to an integer
    number = int(user_input)
    # If successful, print "OK"
    print("OK")
except ValueError:
    # If a ValueError occurs, the input is not an integer
    # Print the input enclosed in single quotes with the appropriate message
    print(f"'{user_input}' is not an integer")
