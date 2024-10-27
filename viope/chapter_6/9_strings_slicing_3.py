def strings_slicing_3():
    # Input the string from the user
    user_string = input("Enter a string: ")

    # Loop through the length of the string to create substrings
    for i in range(1, len(user_string) + 1):
        # Print the substring from the start to the current index
        print(user_string[:i])


# Main function to run the program
if __name__ == "__main__":
    strings_slicing_3()
