from copy import deepcopy

weekdays_1 = ["Branch 1", ["Monday", "Wednesday", "Friday"]]
weekdays_2 = deepcopy(
    weekdays_1
)  # Use deepcopy to duplicate the list and its nested list
weekdays_2[0] = "Branch 2"  # Change the branch name in the second list
weekdays_2[1].insert(1, "Tuesday")  # Insert one more weekday name

# Print branch names and their corresponding weekdays
print(weekdays_1[0], weekdays_1[1])  # Print first branch and its weekdays
print(weekdays_2[0], weekdays_2[1])  # Print second branch and its weekdays
