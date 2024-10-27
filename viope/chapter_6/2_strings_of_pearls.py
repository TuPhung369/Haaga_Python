def strings_of_pearls():
    pearl_count = 0

    while True:
        user_input = input("Enter next string: ")

        # Check for quit condition
        if user_input.lower() == "quit":
            break

        # Count occurrences of "pearl" (case-insensitive)
        if user_input.lower() == "pearl":
            pearl_count += 1

    # Check if pearl_count is greater than 0 and print the result
    if pearl_count > 0:
        print(f"{pearl_count} pearls")

    print("Bye!")


# Main function to run the program
if __name__ == "__main__":
    strings_of_pearls()
