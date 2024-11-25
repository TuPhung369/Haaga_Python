def strings_same_characters():
    # Input two strings from the user
    first_string = input("Enter first string: ")
    second_string = input("Enter second string: ")

    # Remove blanks and sort the characters of the strings
    first_sorted = sorted(first_string.replace(" ", ""))
    second_sorted = sorted(second_string.replace(" ", ""))

    # Check if the sorted characters are the same
    if first_sorted == second_sorted:
        print("Same characters")
    else:
        print("Different characters")


# Main function to run the program
if __name__ == "__main__":
    strings_same_characters()
