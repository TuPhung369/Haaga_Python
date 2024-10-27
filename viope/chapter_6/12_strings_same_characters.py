def strings_same_characters():
    # Input two strings from the user
    first_string = input("Enter first string: ")
    second_string = input("Enter second string: ")

    # Remove blanks and convert strings to sets of characters
    first_set = set(first_string.replace(" ", ""))
    second_set = set(second_string.replace(" ", ""))

    # Check if the sets of characters are the same
    if first_set == second_set:
        print("Same characters")
    else:
        print("Different characters")


# Main function to run the program
if __name__ == "__main__":
    strings_same_characters()
