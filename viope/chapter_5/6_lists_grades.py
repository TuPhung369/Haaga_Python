def lists_grade():
    # Input the price and discount percentage from the user
    words = ["A", "A", "B", "A", "C", "B", "C", "F", "B", "B", "A", "A", "C", "C", "C"]

    word = input("Enter grade letter: ").upper()

    count = words.count(word)

    total_grades = len(words)
    percentage = count / total_grades * 100

    print(f"{percentage:.1f} %")


# Call the main function to execute the program
if __name__ == "__main__":
    lists_grade()
