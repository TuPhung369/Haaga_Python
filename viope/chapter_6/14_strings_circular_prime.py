def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def is_circular_prime(n):
    """Check if a number is a circular prime."""
    str_n = str(n)
    length = len(str_n)

    # Check all rotations of the number
    for i in range(length):
        rotated_number = int(str_n[i:] + str_n[:i])
        if not is_prime(rotated_number):
            return False
    return True


def main():
    """Main function to interact with the user."""
    number = int(input("Enter a positive integer: "))
    if is_circular_prime(number):
        print(f"{number} is a circular prime")
    else:
        print(f"{number} is not a circular prime")


# Entry point of the program
if __name__ == "__main__":
    main()
