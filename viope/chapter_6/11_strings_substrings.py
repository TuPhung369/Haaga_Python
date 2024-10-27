def strings_substrings():
    # Input the string and character from the user
    user_string = input("Enter a string: ")
    target_char = input("Enter a character: ")

    # Check if the target character is in the string
    for i in range(len(user_string) - 3):  # Loop through the string
        if (
            user_string[i] == target_char
        ):  # Check if the substring starts with the target character
            print(user_string[i : i + 4])  # Print the 4-character substring


# Main function to run the program
if __name__ == "__main__":
    strings_substrings()
