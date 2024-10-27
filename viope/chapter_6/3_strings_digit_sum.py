def strings_digit_sum():
    user_input = input("Enter a string: ")
    digit_sum = 0

    # Iterate over each character in the string
    for char in user_input:
        # Check if the character is a digit
        if char.isdigit():
            digit_sum += int(char)

    print(f"The sum of digits is {digit_sum}")


# Main function to run the program
if __name__ == "__main__":
    strings_digit_sum()
