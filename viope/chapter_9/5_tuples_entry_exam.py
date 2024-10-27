def grade_exam(applicants, passing_score):
    # Create a list to hold the tuples of passed applicants
    passed_applicants = []

    # Iterate through the list of applicants
    for applicant in applicants:
        name, score = applicant  # Unpack the tuple
        if (
            score >= passing_score
        ):  # Check if the score meets or exceeds the passing score
            passed_applicants.append(applicant)  # Add the applicant to the passed list

    return passed_applicants  # Return the list of passed applicants


def main():
    applicants = [("Ann", 30), ("Jack", 25), ("Jill", 40)]
    passed_applicants = grade_exam(applicants, 30)
    print("Entry exam passed")
    for name, points in passed_applicants:
        print(f"{name}, {points} points")


if __name__ == "__main__":
    main()
