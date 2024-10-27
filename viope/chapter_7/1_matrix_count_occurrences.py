def count_occurrences(matrix, target):
    """Count occurrences of the target integer in the matrix."""
    count = 0
    for row in matrix:
        count += row.count(target)  # Count occurrences in the current row
    return count


def main():
    m = [[1, 2, 3], [1, 2, 2], [1, 1, 1], [1, 2, 1]]
    print(count_occurrences(m, 1))  # Should print the count of 1s
    print(count_occurrences(m, 2))  # Should print the count of 2s
    print(count_occurrences(m, 5))  # Should print 0, as there are no 5s


# Entry point of the program
if __name__ == "__main__":
    main()
