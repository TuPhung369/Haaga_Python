def row_ok(sudoku, row_index):
    """Check if the specified row in the Sudoku grid is valid.

    Args:
        sudoku (list of list of int): The Sudoku grid.
        row_index (int): The index of the row to check.

    Returns:
        bool: True if the row is valid, False otherwise.
    """
    seen = set()
    for number in sudoku[row_index]:
        if number != 0:  # Ignore zeros (empty squares)
            if number in seen:
                return False  # If the number is already seen, it's invalid
            seen.add(number)
    return True


def column_ok(sudoku, column_index):
    """Check if the specified column in the Sudoku grid is valid.

    Args:
        sudoku (list of list of int): The Sudoku grid.
        column_index (int): The index of the column to check.

    Returns:
        bool: True if the column is valid, False otherwise.
    """
    seen = set()
    for row in sudoku:
        number = row[column_index]
        if number != 0:  # Ignore zeros (empty squares)
            if number in seen:
                return False  # If the number is already seen, it's invalid
            seen.add(number)
    return True


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

    seen = set()
    for r in range(3):  # Loop through 3 rows
        for c in range(3):  # Loop through 3 columns
            number = sudoku[row_index + r][column_index + c]
            if number != 0:  # Ignore zeros (empty squares)
                if number in seen:
                    return False  # If the number is already seen, it's invalid
                seen.add(number)
    return True  # The block is valid if no duplicates were found


def grid_ok(sudoku):
    """Check if the entire Sudoku grid is valid.

    Args:
        sudoku (list of list of int): The Sudoku grid.

    Returns:
        bool: True if the grid is valid, False otherwise.
    """
    for i in range(9):
        if not row_ok(sudoku, i):
            return False  # Check each row
        if not column_ok(sudoku, i):
            return False  # Check each column

    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            if not block_ok(sudoku, i, j):
                return False  # Check each 3x3 block

    return True  # If all checks passed, the grid is valid


def main():
    sudoku_1 = [
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

    sudoku_2 = [
        [2, 6, 7, 8, 3, 9, 5, 0, 4],
        [9, 0, 3, 5, 1, 0, 6, 0, 0],
        [0, 5, 1, 6, 0, 0, 8, 3, 9],
        [5, 1, 9, 0, 4, 6, 3, 2, 8],
        [8, 0, 2, 1, 0, 5, 7, 0, 6],
        [6, 7, 4, 3, 2, 0, 0, 0, 5],
        [0, 0, 0, 4, 5, 7, 2, 6, 3],
        [3, 2, 0, 0, 8, 0, 0, 5, 7],
        [7, 4, 5, 0, 0, 3, 9, 0, 1],
    ]

    print(grid_ok(sudoku_1))  # False
    print(grid_ok(sudoku_2))  # True


if __name__ == "__main__":
    main()
