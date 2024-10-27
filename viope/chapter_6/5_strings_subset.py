def strings_subset():
    # Input the first string
    first_string = input("Enter first string: ")

    # Input the second string
    second_string = input("Enter second string: ")

    # Check if the second string is empty
    if second_string == "":
        print("Nothing to be checked")
        return

    # Initialize a boolean variable to True
    is_subset = True

    # Loop through each character in the second string
    for char in second_string:
        if char not in first_string:
            is_subset = False
            break

    # Print the result based on the boolean variable
    if is_subset:
        print("Subset")
    else:
        print("Not subset")


# Main function to run the program
if __name__ == "__main__":
    strings_subset()
