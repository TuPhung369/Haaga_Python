def pow_2_3(n):
    # Calculate the second and third powers of the integer
    p2 = n**2
    p3 = n**3
    # Return the results in a tuple
    return p2, p3


def main():
    x = int(input("Enter an integer: "))
    p2, p3 = pow_2_3(x)
    print(p2)
    print(p3)


if __name__ == "__main__":
    main()
