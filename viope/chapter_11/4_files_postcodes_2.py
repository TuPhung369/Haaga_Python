from pathlib import Path


def load_data(file_name):
    """Load post-office data from a CSV file into a dictionary."""
    file_path = Path(file_name)

    try:
        with file_path.open("r", newline="", encoding="utf-8") as csvfile:
            post_offices = {}
            for line in csvfile:
                parts = line.strip().split(";")
                if len(parts) == 3:  # Ensure there are 3 parts
                    postcode = parts[0].strip()
                    finnish_name = parts[1].strip().upper()
                    swedish_name = parts[2].strip().upper()

                    # Add postcodes to the dictionary for both Finnish and Swedish names
                    if finnish_name not in post_offices:
                        post_offices[finnish_name] = []
                    post_offices[finnish_name].append(postcode)

                    if swedish_name not in post_offices:
                        post_offices[swedish_name] = []
                    post_offices[swedish_name].append(postcode)

            return post_offices
    except FileNotFoundError:
        return None  # Return None if the file is not found


def main():
    file_name = "postcodes.csv"
    post_offices = load_data(file_name)

    if post_offices is None:
        print(f"The file {file_name} is not found")
        return

    place_name = input("Enter place name: ").strip().upper()

    # Retrieve post-office information based on place name
    if place_name in post_offices:
        unique_postcodes = set(post_offices[place_name])  # Get unique postcodes

        # Print the postcodes for the place name
        for postcode in sorted(unique_postcodes):  # Sort postcodes for ordered output
            print(f"{postcode} {place_name}")
    else:
        print("No postoffice found")


if __name__ == "__main__":
    main()
