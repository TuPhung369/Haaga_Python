def main():
    team = {
        "John": "software developer",
        "Ann": "project manager",
        "Susan": "software developer",
        "Jill": "lead developer",
    }

    # Using a set to store unique roles
    unique_roles = set(team.values())

    # Printing each unique role
    for role in sorted(unique_roles):
        print(role)


if __name__ == "__main__":
    main()
