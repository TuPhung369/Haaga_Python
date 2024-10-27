def print_matrix_sum(matrix1, matrix2):
    """Print the sum of two matrices."""
    # Assuming both matrices have the same size
    sum_matrix = []  # Initialize the resulting sum matrix

    for i in range(len(matrix1)):  # Iterate over rows
        sum_row = []  # Initialize the row for the sum matrix
        for j in range(len(matrix1[i])):  # Iterate over columns
            sum_value = (
                matrix1[i][j] + matrix2[i][j]
            )  # Calculate the sum of corresponding elements
            sum_row.append(sum_value)  # Add the sum to the current row
        sum_matrix.append(sum_row)  # Add the row to the sum matrix

    # Print the resulting sum matrix
    for row in sum_matrix:
        print(" ".join(map(str, row)))  # Print each row in the required format


def main():
    m1 = [[1, 2, 0], [2, 3, 4]]
    m2 = [[3, 2, 5], [6, 4, 3]]
    m3 = [[1, 1, 1, 1], [3, 3, 2, 1], [2, 2, 2, 2]]
    m4 = [[2, 2, 2, 3], [2, 3, 1, 0], [1, 2, 3, 4]]

    print_matrix_sum(m1, m2)
    print()  # Print a blank line between outputs
    print_matrix_sum(m3, m4)


# Entry point of the program
if __name__ == "__main__":
    main()
