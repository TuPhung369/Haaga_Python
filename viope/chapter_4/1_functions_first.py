def print_powers():
    # Initialize the starting power of two
    power = 1

    # Print the first 20 powers of two on a single line
    for _ in range(20):
        print(power, end=" ")
        power *= 2


def main():
    print_powers()


# Call the main function to execute the program
if __name__ == "__main__":
    main()
