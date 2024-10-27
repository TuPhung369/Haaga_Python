def main():
    team = {
        "John": "software developer",
        "Ann": "project manager",
        "Susan": "software developer",
        "Jill": "lead developer",
    }

    # Updating the dictionary with user input
    while True:
        name = input("Enter name (quit ends): ")
        if name.lower() == "quit":
            break
        role = input("Enter role: ")
        team[name] = role  # Adds or updates the role for the entered name
        print()  # Adds a blank line after each role entry

    # Printing the final dictionary with correct formatting
    print()  # Blank line before printing the team
    for name, role in sorted(team.items()):
        print(f"{name:<7} {role}")


if __name__ == "__main__":
    main()
