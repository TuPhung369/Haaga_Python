def remove_successive_duplicates(lst):
    # Check if the list is empty
    if not lst:
        return

    # Initialize a new list to store the result
    result = [lst[0]]  # Start with the first element

    # Iterate through the list starting from the second element
    for i in range(1, len(lst)):
        if lst[i] != lst[i - 1]:  # Check for successive duplicates
            result.append(lst[i])  # Add to the result if not a duplicate

    # Modify the original list to reflect the result
    lst[:] = result  # Update the original list in-place


# Main function to test
def main():
    a = [3, 1, 1, 2, 1, 2, 2, 2, 3]
    remove_successive_duplicates(a)
    print(a)  # Expecting: [3, 1, 2, 1, 2, 3]

    a = [1]
    remove_successive_duplicates(a)
    print(a)  # Expecting: [1]

    a = []
    remove_successive_duplicates(a)
    print(a)  # Expecting: []


# Run the main function
if __name__ == "__main__":
    main()
