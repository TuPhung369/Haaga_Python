def main():
    # Team dictionary from dictionaries_team_1
    team = {
        "John": "software developer",
        "Ann": "project manager",
        "Susan": "software developer",
        "Jill": "lead developer",
    }

    # Print names in the default order
    print(" ".join(team.keys()))

    # Print names in sorted order
    print(" ".join(sorted(team.keys())))


if __name__ == "__main__":
    main()
