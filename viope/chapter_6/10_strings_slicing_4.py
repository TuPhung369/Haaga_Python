def strings_slicing_4():
    # Input the string from the user
    user_string = input("Enter a string: ")

    # Check if the string is the same when reversed using slicing
    if user_string == user_string[::-1]:
        print("Yes")
    else:
        print("No")


# Main function to run the program
if __name__ == "__main__":
    strings_slicing_4()
