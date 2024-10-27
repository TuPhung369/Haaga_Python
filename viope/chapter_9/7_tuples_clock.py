def roll_forward(current_time, add_hours, add_minutes):
    # Unpack the current time tuple
    hours, minutes = current_time

    # Add the minutes and calculate overflow for hours
    minutes += add_minutes
    hours += add_hours + minutes // 60  # Add overflow from minutes
    minutes = minutes % 60  # Keep minutes between 0 and 59

    # Keep hours between 0 and 23
    hours = hours % 24

    return (hours, minutes)


def main():
    # Initialize the current time
    current_time = (0, 0)
    print(f"The current time is {current_time[0]:02}:{current_time[1]:02}")

    while True:
        # Input hours and minutes to add
        add_hours = int(input("Enter hours to add: "))
        if add_hours < 0:
            break  # Terminate the program on negative hours
        add_minutes = int(input("Enter minutes to add: "))

        # Roll the clock forward
        current_time = roll_forward(current_time, add_hours, add_minutes)

        # Print the new clock time
        print(f"{current_time[0]:02}:{current_time[1]:02}")


if __name__ == "__main__":
    main()
