def guitar_strings():

    num_gigs = int(input("Number of gigs: "))
    gigs_per_set = int(input("Gigs to be played with the same set of strings: "))
    price_per_set = float(input("Price of a set of guitar strings: "))

    if gigs_per_set > 0:
        sets_needed = (num_gigs + gigs_per_set - 1) // gigs_per_set
    else:
        sets_needed = 0

    total_cost = sets_needed * price_per_set

    print(f"\nThe guitarist needs {sets_needed} new sets of guitar strings")
    print(f"The total cost is {total_cost:.2f} euros")


guitar_strings()
