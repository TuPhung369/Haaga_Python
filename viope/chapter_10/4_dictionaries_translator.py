def main():
    translations = {}

    # Creating the dictionary
    print("=== Creating a dictionary ===")
    while True:
        english_word = input("Enter english word (quit ends): ").lower()
        if english_word == "quit":
            break
        finnish_word = input("Enter finnish word: ").lower()
        translations[english_word] = finnish_word

    # Using the dictionary
    print("\n=== Using a dictionary ===")
    while True:
        english_word = input("Enter english word (quit ends): ").lower()
        if english_word == "quit":
            break
        if english_word in translations:
            print(translations[english_word])
        else:
            print("Unknown word")


if __name__ == "__main__":
    main()
