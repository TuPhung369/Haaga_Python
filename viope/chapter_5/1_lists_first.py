def lists_first():
    # Initialize the list
    lists = [1, 5, 4, 6, 2, 7]

    # Loop through the list and print each element with a space
    for i in range(len(lists)):
        if i == len(lists) - 1:  # For the last element, avoid adding extra space
            print(lists[i])
        else:
            print(lists[i], end=" ")


def main():
    lists_first()


# Call the main function to execute the program
if __name__ == "__main__":
    main()


# def lists_first():
#     # Initialize the list
#     lists = [1, 5, 4, 6, 2, 7]

#     # Print the elements of the list on a single line with spaces, without a trailing space
#     print(" ".join(map(str, lists)))


# def main():
#     lists_first()


# # Call the main function to execute the program
# if __name__ == "__main__":
#     main()
