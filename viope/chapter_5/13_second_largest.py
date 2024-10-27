def second_largest(lst):
    # Use a set to find distinct values and convert it back to a list
    distinct_values = list(set(lst))

    # Check if there are less than 2 distinct values
    if len(distinct_values) < 2:
        return None

    # Sort the distinct values in descending order
    distinct_values.sort(reverse=True)

    # Return the second largest value
    return distinct_values[1]


# Main function to test
def main():
    # You can add test cases here if you want to check the function
    print(second_largest([]))  # Expecting: None
    print(second_largest([5]))  # Expecting: None
    print(second_largest([3, 1, 2, 1]))  # Expecting: 2
    print(second_largest([0, 0, -4, 0]))  # Expecting: -4
    a = [3, 1, 4, 4]
    print(second_largest(a), a)  # Expecting: 3 [3, 1, 4, 4]


# Run the main function
if __name__ == "__main__":
    main()
