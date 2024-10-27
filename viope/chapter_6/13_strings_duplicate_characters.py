def strings_duplicate_characters():
    # Input a string from the user
    user_string = input("Enter a string: ")

    # Convert the string to a set to remove duplicates
    unique_characters = set(user_string)

    # Check if the length of the unique set is less than the original string
    if len(unique_characters) < len(user_string):
        print("Contains duplicate(s)")
    else:
        print("No duplicates")


# Main function to run the program
if __name__ == "__main__":
    strings_duplicate_characters()
