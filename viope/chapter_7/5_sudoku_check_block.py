def block_ok(sudoku, row_index, column_index):
    """Check if the specified 3x3 block in the Sudoku grid is valid.

    Args:
        sudoku (list of list of int): The Sudoku grid.
        row_index (int): The starting row index of the block (should be 0, 3, or 6).
        column_index (int): The starting column index of the block (should be 0, 3, or 6).

    Returns:
        bool: True if the block is valid, False otherwise.
    """
    # Check if the starting indexes are valid for a 3x3 block
    if row_index not in [0, 3, 6] or column_index not in [0, 3, 6]:
        return False

    seen = set()  # A set to keep track of numbers we've seen
    for r in range(3):  # Loop through 3 rows
        for c in range(3):  # Loop through 3 columns
            number = sudoku[row_index + r][column_index + c]
            if number != 0:  # Ignore zeros (empty squares)
                if number in seen:
                    return False  # If the number is already seen, it's invalid
                seen.add(number)  # Add the number to the set
    return True  # The block is valid if no duplicates were found


def main():
    sudoku = [
        [9, 0, 0, 0, 8, 0, 3, 0, 0],
        [2, 0, 0, 2, 5, 0, 7, 0, 0],
        [0, 2, 0, 3, 0, 0, 0, 0, 4],
        [2, 9, 4, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 7, 3, 0, 5, 6, 0],
        [7, 0, 5, 0, 6, 0, 4, 0, 6],
        [0, 0, 7, 8, 0, 3, 9, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 3],
        [3, 0, 0, 0, 0, 0, 0, 0, 2],
    ]

    print(block_ok(sudoku, row_index=0, column_index=0))  # False
    print(block_ok(sudoku, row_index=3, column_index=6))  # False
    print(block_ok(sudoku, row_index=6, column_index=3))  # True


if __name__ == "__main__":
    main()
