from pathlib import Path
import csv


def load_file(file_name):
    """Load bike ride data from a CSV file."""
    file_path = Path(file_name)
    rides = []

    try:
        with file_path.open("r", newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                rides.append(row)
        return rides
    except FileNotFoundError:
        return None  # Return None if the file is not found


def show_statistics(rides):
    """Calculate and display total kilometers, average distance, and average duration."""
    total_distance = 0
    total_duration = 0
    num_rides = len(rides)

    for ride in rides:
        distance = (
            int(ride["Covered distance (m)"]) / 1000
        )  # Convert meters to kilometers
        duration = int(ride["Duration (sec.)"])  # Duration in seconds
        total_distance += distance
        total_duration += duration

    average_distance = total_distance / num_rides if num_rides > 0 else 0
    average_duration = (
        total_duration / num_rides * (1 / 60) if num_rides > 0 else 0
    )  # Convert to minutes

    # Print statistics without decimal for total distance and rounded average values
    print(f"{int(total_distance)} kilometers on {num_rides} bike rides")
    print(f"Average distance: {average_distance:.1f} kilometers")
    print(
        f"Average duration: {round(average_duration)} minutes\n"
    )  # Round to the nearest minute


def show_max_departures(rides):
    """Show the bike stations with the maximum number of departures."""
    departure_counts = {}

    for ride in rides:
        departure_station = ride["Departure station name"]
        departure_counts[departure_station] = (
            departure_counts.get(departure_station, 0) + 1
        )

    # Find the maximum number of departures
    max_departures = max(departure_counts.values(), default=0)

    # Get all stations with the maximum number of departures
    max_departure_stations = [
        station
        for station, count in departure_counts.items()
        if count == max_departures
    ]

    # Sort the station names in ascending order
    max_departure_stations.sort()

    # Print the results
    print("Maximum number of departures from a bike station:")
    for station in max_departure_stations:
        print(f"{station} ({max_departures} departures)")


def main():
    file_name = input("Enter file name: ").strip()
    rides = load_file(file_name)

    if rides is None:
        print(f"The file {file_name} is not found")
        return

    show_statistics(rides)  # Call the statistics function
    show_max_departures(rides)  # Show max departures


if __name__ == "__main__":
    main()
