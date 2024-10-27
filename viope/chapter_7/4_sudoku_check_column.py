def column_ok(sudoku, column_index):
    """Check if the specified column in the Sudoku grid is valid.

    Args:
        sudoku (list of list of int): The Sudoku grid.
        column_index (int): The index of the column to check.

    Returns:
        bool: True if the column is valid, False otherwise.
    """
    seen = set()  # A set to keep track of numbers we've seen
    for row in sudoku:
        number = row[column_index]
        if number != 0:  # Ignore zeros (empty squares)
            if number in seen:
                return False  # If the number is already seen, it's invalid
            seen.add(number)  # Add the number to the set
    return True  # The column is valid if no duplicates were found


def main():
    sudoku = [
        [9, 0, 0, 0, 8, 0, 3, 0, 0],
        [2, 0, 0, 2, 5, 0, 7, 0, 0],
        [0, 2, 0, 3, 0, 0, 0, 0, 4],
        [2, 9, 4, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 7, 3, 0, 5, 6, 0],
        [7, 0, 5, 0, 6, 0, 4, 0, 0],
        [0, 0, 7, 8, 0, 3, 9, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 3],
        [3, 0, 0, 0, 0, 0, 0, 0, 2],
    ]

    print(column_ok(sudoku, column_index=0))  # False
    print(column_ok(sudoku, column_index=1))  # True
    print(column_ok(sudoku, column_index=8))  # True


if __name__ == "__main__":
    main()
