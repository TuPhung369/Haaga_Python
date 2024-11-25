def strings_of_pearls():
    pearl_count = 0

    # Get the first string
    first_input = input("Enter first string: ")

    # Check if the first input is "quit"
    if first_input.lower() == "quit":
        print("\nBye!")
        return

    # Count occurrences of "pearl" (case-insensitive)
    if first_input.lower() == "pearl":
        pearl_count += 1

    while True:
        user_input = input("Enter next string: ")

        # Check for quit condition
        if user_input.lower() == "quit":
            break

        # Count occurrences of "pearl" (case-insensitive)
        if user_input.lower() == "pearl":
            pearl_count += 1

    # Print the result
    print()
    if pearl_count > 0:
        print(f"{pearl_count} pearls")
    else:
        print("0 pearls")

    print("Bye!")


# Main function to run the program
if __name__ == "__main__":
    strings_of_pearls()
