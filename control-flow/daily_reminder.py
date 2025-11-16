# Prompt user for task, priority, and time-bound status
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

# Use match case to handle priority
match priority:
    case "high":
        # Modify based on time-bound
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
        else:
            print(f"Reminder: '{task}' is a high priority task.")
    case "medium":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a medium priority task that requires immediate attention today!")
        else:
            print(f"Reminder: '{task}' is a medium priority task.")
    case "low":
        if time_bound == "yes":
            print(f"Note: '{task}' is a low priority task that requires immediate attention today!")
        else:
            print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")
    case _:
        print(f"'{task}' has an unknown priority level")

