def sharing_apples():
    apples = int(input("How many apples? "))
    children = int(input("How many children? "))

    apples_per_child = apples // children
    leftover_apples = apples % children

    print(f"\nEach child will get {apples_per_child} apples.")
    print(f"There will be {leftover_apples} leftover apples.")


sharing_apples()
