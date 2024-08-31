def gender_distribution():
    female = int(input("Enter the number of female students: "))
    male = int(input("Enter the number of male students: "))
    total = female + male
    if total > 0:
        female_percentage = (female / total) * 100
        male_percentage = (male / total) * 100
    else:
        female_percentage = 0.0
        male_percentage = 0.0
    print()
    print(f"Female: {female_percentage:.1f} %")
    print(f"Male: {male_percentage:.1f} %")


gender_distribution()
