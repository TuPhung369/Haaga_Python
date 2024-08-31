def compute_earnings(hourly_wage, hours_worked):
    """
    Compute the earnings based on hourly wage and hours worked,
    including overtime pay.

    :param hourly_wage: The hourly wage in euros.
    :param hours_worked: The total number of hours worked.
    :return: The total earnings in euros.
    """
    regular_hours = min(hours_worked, 40)
    overtime_hours = max(0, hours_worked - 40)

    regular_pay = regular_hours * hourly_wage
    overtime_pay = overtime_hours * (hourly_wage * 1.5)

    return regular_pay + overtime_pay


def main():
    # Input hourly wage and hours worked from the user
    try:
        hourly_wage = float(input("Enter wage: "))
        hours_worked = int(input("Enter hours: "))

        if hourly_wage < 0 or hours_worked < 0:
            print("Wage and hours must be non-negative.")
        else:
            # Compute earnings
            earnings = compute_earnings(hourly_wage, hours_worked)

            # Print the earnings with two decimal places
            print(f"The earnings are {earnings:.2f}")

    except ValueError:
        print("Please enter valid numbers for wage and hours.")


# Call the main function to execute the program
if __name__ == "__main__":
    main()
