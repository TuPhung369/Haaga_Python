def common_members(list1, list2):
    # Loop through each item in list1
    for item in list1:
        # Check if this item is in list2
        if item in list2:
            return True  # Common element found
    return False  # No common element found


# def common_members(list1, list2):
#     # Convert lists to sets and check if there's any intersection
#     return bool(set(list1) & set(list2))


# Main function
def main():
    # Test the function with example lists
    print(common_members([1, 2, 5], [4, 5]))  # Expecting: True
    print(common_members([1, 2, 3], [4, 5]))  # Expecting: False


# Run the main function
if __name__ == "__main__":
    main()
