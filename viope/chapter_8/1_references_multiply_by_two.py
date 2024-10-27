def multiply_by_two(numbers):
    """Multiply each number in the list by two.

    Args:
        numbers (list of int): The list of numbers to be modified.
    """
    for i in range(len(numbers)):
        numbers[i] *= 2  # Multiply each element by 2


def main():
    numbers = [1, 2, 3, 4, 5, 6]
    more_numbers = [10, 20, 30]
    print(numbers)
    multiply_by_two(numbers)
    print(numbers)

    print( more_numbers)
    multiply_by_two(more_numbers)
    print(more_numbers)


if __name__ == "__main__":
    main()
