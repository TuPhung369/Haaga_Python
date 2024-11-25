def strings_surnames():
    # Ask the user how many surnames to enter
    count = int(input("How many surnames? "))
    surnames = []

    # Input surnames from the user
    for _ in range(count):
        surname = input("Enter a surname: ").strip()
        surnames.append(surname)

    # Create a dictionary to ensure distinct surnames and preserve original capitalization
    distinct_surnames = {surname.lower(): surname.capitalize() for surname in surnames}

    # Sort the surnames alphabetically based on the lowercase version
    sorted_surnames = sorted(distinct_surnames.values())

    # Print the distinct surnames as required
    print("\n" + " ".join(sorted_surnames))


# Main function to run the program
if __name__ == "__main__":
    strings_surnames()
