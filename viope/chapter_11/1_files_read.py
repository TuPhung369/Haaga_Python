from pathlib import Path


def main():
    # Prompt the user for the file name
    file_name = input("Enter file name: ")

    # Create a Path object for the specified file
    file_path = Path(file_name)

    try:
        # Attempt to read the file content
        with file_path.open() as file:  # Open the file
            content = file.read()  # Read the file content
            print(content)  # Print the content as it is
    except FileNotFoundError:  # Handle the case where the file does not exist
        print(f"The file {file_name} is not found")  # File not found message


if __name__ == "__main__":
    main()
