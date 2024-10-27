def strings_start():
    # Input a string from the user
    user_input = input("Enter a string: ")

    # Convert the string to lowercase
    lowercase_string = user_input.lower()

    # Convert the string to uppercase
    uppercase_string = user_input.upper()

    # Calculate the length of the string
    string_length = len(user_input)

    # Print the results
    print(lowercase_string)
    print(uppercase_string)
    print(f"{string_length} characters")


# Main function to run the program
if __name__ == "__main__":
    strings_start()
