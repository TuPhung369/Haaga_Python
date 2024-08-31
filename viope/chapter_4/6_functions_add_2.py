def add(float1, float2):
    """
    Compute the sum of two floats and return the result as an integer.
    Uses rounding to ensure that half values are rounded up.

    :param float1: The first float number.
    :param float2: The second float number.
    :return: The sum of the two floats rounded to the nearest integer.
    """
    # Compute the sum of the floats
    result = float1 + float2
    # Round the result to the nearest integer
    return int(result + 0.5)


def main():
    # Input two floats from the user
    try:
        float1 = float(input("Enter a float: "))
        float2 = float(input("Enter a float: "))

        # Call the add function
        result = add(float1, float2)

        # Print the result
        print(result)

    except ValueError:
        print("Please enter valid floating-point numbers.")


# Ensure main is only executed when running the script directly
if __name__ == "__main__":
    main()
