def lists_second():
    # Input the price and discount percentage from the user
    words = []
    while True:
        word = input("Enter a word (quit ends): ")
        if word.low() == "quit":
            break
        words.append(word)
    words.sort()
    for word in words:
        print(word)


# Call the main function to execute the program
if __name__ == "__main__":
    lists_second()
