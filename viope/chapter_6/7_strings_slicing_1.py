def strings_slicing_1():
    # Input the string from the user
    user_string = input("Enter a string: ")

    # Get the first two characters
    first_two_chars = user_string[:2]

    # Get every other character in the string
    every_other_char = user_string[::2]

    # Print the results
    print(first_two_chars)
    print(every_other_char)


# Main function to run the program
if __name__ == "__main__":
    strings_slicing_1()
