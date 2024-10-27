def count_distinct(lst):
    # Convert the list to a set to remove duplicates, then return its length
    return len(set(lst))


# Main function to test
def main():
    # Example tests
    print(count_distinct([]))  # Expecting: 0
    print(count_distinct([6]))  # Expecting: 1
    print(count_distinct([5, 6, 5, 6, 7, 8]))  # Expecting: 4
    a = [1, 2, 2]
    print(count_distinct(a), a)  # Expecting: 2 [1, 2, 2]


# Run the main function
if __name__ == "__main__":
    main()
