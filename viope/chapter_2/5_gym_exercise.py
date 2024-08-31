def gym_exercise():
    days_per_year = int(input("Enter the number of days of gym visits per year: "))
    price_per_day_pass = float(input("Enter price for a day pass: "))
    yearly_membership_fee = float(input("Enter yearly membership fee: "))

    total_day_pass_cost = days_per_year * price_per_day_pass

    if total_day_pass_cost < yearly_membership_fee:
        difference = yearly_membership_fee - total_day_pass_cost
        print(f"\nBuying day passes is {difference:.2f} euros cheaper")
    elif yearly_membership_fee < total_day_pass_cost:
        difference = total_day_pass_cost - yearly_membership_fee
        print(f"\nPaying the yearly membership fee is {difference:.2f} euros cheaper")
    else:
        print("\nThere is no price difference")


gym_exercise()
