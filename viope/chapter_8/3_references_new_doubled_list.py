def new_doubled_list(numbers):
    # Create a new list with each number multiplied by two
    return [number * 2 for number in numbers]


def main():
    first_list = [1, 2, 3, 4, 5, 6]
    second_list = new_doubled_list(first_list)
    print(first_list)
    print(second_list)


if __name__ == "__main__":
    main()
