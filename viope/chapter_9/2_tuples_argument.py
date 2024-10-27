def tuples_argument(player_info):
    # Unpack the tuple into variables
    team_name, player_name, goals = player_info
    # Print the player's information in the required format
    print(f"{player_name} ({team_name}), {goals} goals")


def main():
    p = ("Hawks", "Jennifer", 10)
    tuples_argument(p)


if __name__ == "__main__":
    main()
