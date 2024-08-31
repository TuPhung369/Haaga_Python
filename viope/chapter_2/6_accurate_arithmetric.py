from decimal import Decimal, getcontext


def accurate_arithmetic():
    getcontext().prec = 30
    first_number = Decimal(input("Enter first number: "))
    second_number = Decimal(input("Enter second number: "))

    result = first_number + second_number

    print(f"\n{first_number} + {second_number} = {result}")


accurate_arithmetic()
