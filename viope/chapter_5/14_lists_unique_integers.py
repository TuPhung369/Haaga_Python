def lists_unique_integers():
    # Input five integers from the user
    integers = []
    for _ in range(5):
        num = int(input("Enter an integer: "))  # Read integer input
        integers.append(num)  # Add to the list

    # Get distinct integers and sort them
    distinct_integers = sorted(set(integers))
    # Sort all inputted integers
    all_integers_sorted = sorted(integers)

    # Print results
    print("Distinct integers in ascending order:", distinct_integers)
    print("All inputted values in ascending order:", all_integers_sorted)


# Main function to test
def main():
    lists_unique_integers()


# Run the main function
if __name__ == "__main__":
    main()
