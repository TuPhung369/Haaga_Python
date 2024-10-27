def remove_min_max(lst):
    # Check if the list is empty or has only one element
    if len(lst) <= 1:
        lst.clear()  # Clear the list if it's empty or has one element
    else:
        # Remove the smallest and largest values
        min_value = min(lst)
        max_value = max(lst)
        lst.remove(min_value)  # Remove the first occurrence of the minimum value
        lst.remove(max_value)  # Remove the first occurrence of the maximum value


def main():
    a = [3, 1, 4, 1, 5]
    remove_min_max(a)
    print(a)


if __name__ == "__main__":
    main()
