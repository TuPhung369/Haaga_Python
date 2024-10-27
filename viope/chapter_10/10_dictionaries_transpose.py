def main():
    vocabulary = {"cat": "kissa", "dog": "koira", "bird": "lintu"}
    print(vocabulary)
    transposed = transpose_dictionary(
        vocabulary
    )  # Call the function and store the result
    print(transposed)


def transpose_dictionary(original_dict):
    transposed_dict = {
        value: key for key, value in original_dict.items()
    }  # Create a new dict with swapped keys and values
    return transposed_dict  # Return the new transposed dictionary


if __name__ == "__main__":
    main()
