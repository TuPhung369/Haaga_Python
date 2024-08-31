# Input an integer from the user
n = int(input("Enter an integer: "))

# Check if there are integers to print
if n < 1:
    print("Nothing to be printed")
else:
    total_sum = 0
    # Print integers in descending order
    for i in range(n, 0, -1):
        print(i, end=" ")
        total_sum += i

    # Print the sum of the integers
    print(f"\nThe sum is {total_sum}")
