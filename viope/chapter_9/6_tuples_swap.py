def tuples_swap():
    # Input seven integers from the user
    numbers = []
    for _ in range(7):
        number = int(input("Enter an integer: "))
        numbers.append(number)

    # Swap each successive pair of elements using slicing
    for i in range(0, len(numbers) - 1, 2):
        # Swap numbers[i] and numbers[i + 1]
        numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]

    # Print the final list
    print(numbers)


if __name__ == "__main__":
    tuples_swap()
