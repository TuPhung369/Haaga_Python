# Input the interest rate, capital income tax rate, initial deposit, and number of years
interest_rate = float(input("Enter interest rate: "))
tax_rate = float(input("Enter capital income tax rate: "))
initial_deposit = float(input("Enter initial deposit: "))
number_of_years = int(input("Enter number of years: "))
print("")
# Set the initial balance to the initial deposit
balance = initial_deposit

# Loop through each year
for year in range(1, number_of_years + 1):
    # Calculate the interest before tax
    interest = balance * (interest_rate / 100)

    # Subtract the capital income tax from the interest
    interest_after_tax = interest * (1 - tax_rate / 100)

    # Add the interest after tax to the balance
    balance += interest_after_tax

    # Print the balance at the end of the year
    print(f"Year {year}: {balance:.2f}")
