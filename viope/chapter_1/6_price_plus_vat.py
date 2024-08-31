def price_plus_vat():
    try:
        price = float(input("Enter price: "))
        VAT = 0.24
        price_with_vat = price * (1 + VAT)
        print(f"The price with VAT is {price_with_vat:.2f}")
    except ValueError:
        print("Invalid price")


price_plus_vat()
