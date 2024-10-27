from urllib.request import urlopen


def lists_words_from_url():
    # Fetch the word list from the URL and decode it
    url = "https://www.mit.edu/~ecprice/wordlist.10000"
    word_list = [word.decode("utf-8") for word in urlopen(url).read().splitlines()]

    # Display the total word count
    word_count = len(word_list)
    print(f"{word_count} words")

    # Calculate and display the average word length
    total_length = sum(len(word) for word in word_list)
    average_length = total_length / word_count
    print(f"The average word length is {average_length}")

    # Initialize a list of counters for each word length from 1 to 22
    counters = [0] * 23

    # Count the number of words of each length
    for word in word_list:
        length = len(word)
        if 1 <= length <= 22:
            counters[length] += 1

    # Display the counts of each word length
    print("Length Count")
    for length, count in enumerate(
        counters[1:], start=1
    ):  # Start from 1 to skip the 0th element
        print(f"{length:>6} {count:5}")


# Run the function
lists_words_from_url()
