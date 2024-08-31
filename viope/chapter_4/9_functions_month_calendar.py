import calendar


def print_month_calendar(year, month):
    # Create a TextCalendar instance with Monday as the first day of the week
    cal = calendar.Calendar(firstweekday=0)  # Monday as the first day of the week

    # Get the month calendar as a matrix (list of weeks)
    month_days = cal.monthdayscalendar(year, month)

    # Get the month name for header
    month_name = calendar.month_name[month]

    # Print the month and year header
    print(f" > {month_name} {year} <")

    # Print the days of the week header
    print(" Mon Tue Wed Thu Fri Sat Sun")

    # Print the days of the month
    for week_index, week in enumerate(month_days):
        # Prepare formatted days for the current week
        formatted_days = []

        for day in week:
            if day != 0:
                formatted_days.append(f"{day:4}")  # Format days with 2 spaces
            else:
                formatted_days.append(
                    "    "
                )  # Empty space for days outside the current month

        # Join the formatted days into a string
        week_string = "".join(formatted_days).rstrip()

        # Print the week, only strip trailing spaces if it's the last week with days
        if week_index == len(month_days) - 1:
            # Print without extra spaces at the end
            print(week_string.rstrip())
        else:
            print(week_string)


def main():
    # Get the year and month from the user
    try:
        year = int(input("Enter year: "))
        month = int(input("Enter month: "))
        print()
        # Validate the month
        if 1 <= month <= 12:
            print_month_calendar(year, month)
        else:
            print("Invalid month. Please enter a month between 1 and 12.")

    except ValueError:
        print("Invalid input. Please enter valid integers for year and month.")


# Ensure the main function runs when the script is executed
if __name__ == "__main__":
    main()
