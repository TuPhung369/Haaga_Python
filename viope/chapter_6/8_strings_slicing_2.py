def strings_slicing_2():
    # Input the string from the user
    user_string = input("Enter a string: ")

    # Check if the string has less than two characters
    if len(user_string) < 2:
        print("Too short string")
    else:
        # Get the next-to-last character using slicing
        next_to_last_char = user_string[-2]
        print(next_to_last_char)


# Main function to run the program
if __name__ == "__main__":
    strings_slicing_2()
