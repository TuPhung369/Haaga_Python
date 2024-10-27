from pathlib import Path
import csv


def load_file(file_name):
    """Load bike ride data from a CSV file."""
    file_path = Path(file_name)

    try:
        with file_path.open("r", newline="", encoding="utf-8") as csvfile:
            reader = csv.reader(csvfile)
            data = list(reader)
            # Exclude the first line (headers)
            return data[1:]  # Return all rows except the first one
    except FileNotFoundError:
        return None  # Return None if the file is not found


def show_statistics(data):
    """Show statistics from the bike ride data."""
    total_distance = 0.0  # Initialize total_distance as a float
    total_duration = 0  # Initialize total_duration as an integer
    ride_count = len(data)

    for row in data:
        try:
            # Assuming the covered distance is in the seventh column and duration in the eighth column
            distance = (
                float(row[6]) / 1000
            )  # Convert distance from meters to kilometers
            duration = int(row[7]) / 60  # Convert duration from seconds to minutes

            total_distance += distance
            total_duration += duration
        except (ValueError, IndexError):
            continue  # Skip rows with invalid data or if the row has less than required columns

    # Check for zero rides to avoid division by zero
    if ride_count > 0:
        average_distance = total_distance / ride_count
        average_duration = total_duration / ride_count
    else:
        average_distance = 0
        average_duration = 0

    # Display statistics rounded to the nearest integer where appropriate
    print(f"{total_distance:.0f} kilometers on {ride_count} bike rides")
    print(f"Average distance: {average_distance:.1f} kilometers")
    print(f"Average duration: {average_duration:.0f} minutes")


def main():
    # Input the name of the CSV file from the user
    file_name = input("Enter file name: ")
    print()  # Adding an extra newline for better output formatting

    # Load the file and get data
    data = load_file(file_name)

    # Check if data was loaded successfully
    if data is None:
        print(f"The file {file_name} is not found")
    else:
        show_statistics(data)


if __name__ == "__main__":
    main()
