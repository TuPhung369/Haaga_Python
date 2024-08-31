def print_pyramid(height):
    """
    Print a pyramid with the given height using the '*' character.

    :param height: The height of the pyramid.
    """
    for i in range(height):
        # Calculate the number of spaces and stars for the current row
        spaces = " " * (height - i - 1)
        stars = "*" * (2 * i + 1)
        # Print the current row of the pyramid
        print(spaces + stars)


def main():
    # Input height of the pyramid from the user
    try:
        height = int(input("Enter pyramid height: "))

        if height > 0:
            # Call the print_pyramid function with the valid height
            print_pyramid(height)

    except ValueError:
        # If the input is not a valid integer, print the height prompt again
        print("Enter pyramid height: ", end="")


# Call the main function to execute the program
if __name__ == "__main__":
    main()
