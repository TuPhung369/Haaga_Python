def compute_discount(price, discount_percentage):
    """
    Compute the discount amount based on the price and discount percentage.

    :param price: The original price in euros.
    :param discount_percentage: The discount percentage.
    :return: The discount amount in euros.
    """
    return price * (discount_percentage / 100)


def main():
    # Input the price and discount percentage from the user
    try:
        price = float(input("Enter price: "))
        discount_percentage = float(input("Enter discount percentage: "))

        # Compute the discount
        discount = compute_discount(price, discount_percentage)

        # Print the discount amount
        print(f"The discount is {discount:.2f} euros")

    except ValueError:
        print("Please enter valid numbers for price and discount percentage.")


# Call the main function to execute the program
if __name__ == "__main__":
    main()
