# Initialize variables
total = 0.0
count = 0

# Get the first value from the user
number = float(input("Enter first number: "))

# Standard while loop pattern
while number != 0:
    total += number
    count += 1
    # Get the next value from the user
    number = float(input("Enter next number: "))

# Check if there were any numbers entered (excluding the zero)
if count == 0:
    print("Nothing to be calculated")
else:
    average = total / count
    # Display the average with two decimals
    print(f"The average is {average:.2f}")
