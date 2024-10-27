from urllib.request import urlopen
from collections import defaultdict


def main():
    # Fetch the content from the URL
    url = "https://www.mit.edu/~ecprice/wordlist.10000"
    content = urlopen(url).read().decode("UTF-8")

    # Initialize a dictionary to count letter occurrences
    letter_counts = defaultdict(int)

    # Count each letter in a case-insensitive manner
    for char in content.lower():
        if char.isalpha():  # Only consider alphabetic characters
            letter_counts[char] += 1

    # Print the count of each letter that appears in the content
    for letter, count in sorted(letter_counts.items()):
        print(f"{letter}: {count}")


if __name__ == "__main__":
    main()
