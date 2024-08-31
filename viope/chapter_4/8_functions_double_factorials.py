def double_factorial(n):
    if n == 0:
        return 1  # 0!! is defined as 1
    elif n == 1:
        return 1  # 1!! is defined as 1
    else:
        result = 1
        # Compute the double factorial by multiplying the appropriate terms
        for i in range(n, 0, -2):
            result *= i
        return result


def main():
    # Iterate over the range from 0 to 9 and compute the double factorial for each number
    for i in range(10):
        result = double_factorial(i)
        # Print the result in the specified format
        print(f"{i}!! = {result}")


# Ensure the main function runs when the script is executed
if __name__ == "__main__":
    main()
