def row_ok(sudoku, row_index):
    """Check if the specified row in the Sudoku grid is valid.

    Args:
        sudoku (list of list of int): The Sudoku grid.
        row_index (int): The index of the row to check.

    Returns:
        bool: True if the row is valid, False otherwise.
    """
    seen = set()  # A set to keep track of numbers we've seen
    for number in sudoku[row_index]:
        if number != 0:  # Ignore zeros (empty squares)
            if number in seen:
                return False  # If the number is already seen, it's invalid
            seen.add(number)  # Add the number to the set
    return True  # The row is valid if no duplicates were found
