def strings_box():
    # Input the string from the user
    user_string = input("Enter a string: ")

    # Calculate the length of the string for box width
    box_width = len(user_string) + 4  # 4 for the spaces and borders

    # Print the box with the string
    print("-" * box_width)
    print(f"| {user_string} |")
    print("-" * box_width)


# Main function to run the program
if __name__ == "__main__":
    strings_box()
