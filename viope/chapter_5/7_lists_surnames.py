def lists_surnames():
    # Initialize an empty set to store unique surnames
    surnames = set()

    while True:
        surname = input("Enter a surname (ok ends): ")

        # Break the loop if the user enters "ok"
        if surname.lower() == "ok":
            break

        # Add the surname to the set (duplicates will be ignored automatically)
        surnames.add(surname)

    # Convert the set to a sorted list
    surnames.sort()
    print()
    # Print the distinct surnames in alphabetical order
    print(", ".join(surnames))


# Call the function to execute the program
if __name__ == "__main__":
    lists_surnames()


# def lists_surnames():
#     # Initialize an empty list to store surnames
#     surnames = []

#     while True:
#         surname = input("Enter a surname (ok ends): ")

#         # Break the loop if the user enters "ok"
#         if surname.lower() == "ok":
#             break

#         # Append each surname to the list
#         surnames.append(surname)

#     # Remove duplicates by converting the list to a set and back to a sorted list
#     unique_surnames = sorted(set(surnames))

#     # Print the distinct surnames in alphabetical order
#     for surname in unique_surnames:
#         print(surname)  # Each surname will be printed on a new line


# # Call the function to execute the program
# if __name__ == "__main__":
#     lists_surnames()
