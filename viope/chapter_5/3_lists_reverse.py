def lists_reverse():
    # Input the price and discount percentage from the user
    numbers = []
    limit = int(input("How many integers? "))

    while limit > 0:
        number = input("Enter an integer: ")
        numbers.append(number)
        limit -= 1

    numbers.reverse()
    print()
    for i in range(len(numbers)):
        if i == len(numbers) - 1:
            print(numbers[i])
        else:
            print(numbers[i], end=" ")


# Call the main function to execute the program
if __name__ == "__main__":
    lists_reverse()
