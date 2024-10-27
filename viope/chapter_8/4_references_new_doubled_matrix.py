def new_doubled_matrix(matrix):
    # Create a new matrix with each number multiplied by two
    return [[element * 2 for element in row] for row in matrix]


def main():
    m1 = [[1, 2, 3], [4, 5, 6]]
    m2 = new_doubled_matrix(m1)
    print(m1)
    print(m2)


if __name__ == "__main__":
    main()
