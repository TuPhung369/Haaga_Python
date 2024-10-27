def strings_surnames():
    # Ask the user how many surnames to enter
    count = int(input("How many surnames? "))
    surnames = []

    # Input surnames from the user
    for _ in range(count):
        surname = input("Enter a surname: ")
        surnames.append(surname)

    # Create a set to store distinct surnames, ignoring case
    distinct_surnames = {surname.capitalize() for surname in surnames}

    # Sort the surnames in ascending order
    sorted_surnames = sorted(distinct_surnames)

    # Print the distinct surnames as required
    print(" ".join(sorted_surnames))


# Main function to run the program
if __name__ == "__main__":
    strings_surnames()
