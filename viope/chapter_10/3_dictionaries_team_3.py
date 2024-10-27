def main():
    # Team dictionary from dictionaries_team_1
    team = {
        "John": "software developer",
        "Ann": "project manager",
        "Susan": "software developer",
        "Jill": "lead developer",
    }

    while True:
        name = input("Enter name (quit ends): ")
        if name.lower() == "quit":
            break
        elif name in team:
            print(f"{name} is a {team[name]}")
        else:
            print(f"{name} is not in the team")


if __name__ == "__main__":
    main()
