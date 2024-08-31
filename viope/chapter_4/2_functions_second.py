def print_rectangle(height, width):
    # Print the rectangle using '*' characters
    for _ in range(height):
        print("*" * width)


def main():
    # Input the height and width from the user
    try:
        height = int(input("Enter height: "))
        width = int(input("Enter width: "))

        # Check if height and width are positive integers
        if height <= 0 or width <= 0:
            print("Height and width must be positive integers.")
        else:
            # Call the function to print the rectangle
            print_rectangle(height, width)

    except ValueError:
        print("Please enter valid integers for height and width.")


# Call the main function to execute the program
if __name__ == "__main__":
    main()
