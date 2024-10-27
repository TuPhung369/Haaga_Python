from pathlib import Path


def load_data(file_name):
    """Load post-office data from a CSV file into a dictionary."""
    file_path = Path(file_name)

    try:
        with file_path.open("r", newline="", encoding="utf-8") as csvfile:
            # Create a dictionary to store post-office data
            post_offices = {}
            for line in csvfile:
                # Split each line into parts based on semicolon
                parts = line.strip().split(";")
                if (
                    len(parts) == 3
                ):  # Ensure there are 3 parts (postcode, Finnish name, Swedish name)
                    postcode = parts[0]
                    finnish_name = parts[1]
                    swedish_name = parts[2]
                    # Store in dictionary with postcode as key
                    post_offices[postcode] = (finnish_name, swedish_name)
            return post_offices
    except FileNotFoundError:
        return None  # Return None if the file is not found


def main():
    # Input the name of the CSV file
    file_name = input("Enter postcode file name: ")

    # Load the post-office data
    post_offices = load_data(file_name)

    # Check if the file was found
    if post_offices is None:
        print(f"The file {file_name} is not found")
        return  # Exit the program if the file is not found

    # Print the number of rows (post-offices)
    print(f"{len(post_offices)} rows\n")

    # Input a postcode from the user
    postcode = input("Enter postcode: ")

    # Retrieve post-office information based on postcode
    if postcode in post_offices:
        finnish_name, swedish_name = post_offices[postcode]
        print(f"{postcode} {finnish_name}")
        print(f"{postcode} {swedish_name}")
    else:
        print("Unknown postcode")


if __name__ == "__main__":
    main()
