# Function to return the sum of every other element in the list
def sum_every_other(lst):
    if not lst:  # Check if the list is empty
        return None
    return sum(lst[::2])  # Sum every other element starting from index 0


# The command sum(lst[::2]) is a combination of Python’s list slicing and the sum() function. Here’s how it works, broken down step by step:

# Explanation of lst[::2]
# lst - This is the list you’re working with. Let’s say lst = [1, 2, 3, 4, 5].

# Slicing with [::2] - The slice notation [::2] means "take every second element in the list, starting from the first one."

# The general format of slicing is [start:stop:step].
# ::2 here omits start and stop, so it considers the whole list but uses a step of 2.
# For lst = [1, 2, 3, 4, 5]:

# lst[::2] selects the elements at index positions 0, 2, and 4.
# This results in the list [1, 3, 5].
# Explanation of sum(lst[::2])
# sum() Function - Now, sum() adds up the elements in the list [1, 3, 5].
# sum([1, 3, 5]) returns 1 + 3 + 5 = 9.
# So, if lst = [1, 2, 3, 4, 5], then sum(lst[::2]) outputs 9.


# Main function to test the sum_every_other function
def main():
    # You can define a list here to test, for example:
    a = [1, 2, 3, 4, 5]
    print(sum_every_other(a))  # Expected output: 9
    print(a)  # Ensure the original list is unchanged


# Run the main function only when this script is executed directly
if __name__ == "__main__":
    main()
