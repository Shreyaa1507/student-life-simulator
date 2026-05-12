from activities import Workshop


def attend_workshop(time, collaboration, complete):
    """Calculate workshop attendance and learning."""
    if time < 1 or time > 120:
        return None

    if collaboration not in [True, False] or complete not in [True, False]:
        return None

    learning, social, attendance = Workshop(time, collaboration, complete).gains()
    return [attendance, learning]


def run_workshop_activity(student=None):
    """Ask about workshop attendance and display the results."""
    time_attended = int(input("How long did you attend your workshop? "))

    group_work = input("Did you work with a group? ").lower()
    activities_done = input("Did you complete the workshop activities? ").lower()

    if time_attended < 1 or time_attended > 120:
        print("Please enter a valid time between 1 and 120 minutes inclusive.")
        return

    activity = Workshop(time_attended, group_work == "yes", activities_done == "yes")
    learning, social, attendance = activity.gains()

    print(f"Received attendance: {attendance}")
    print(f"Learning improved: {learning}")

    if student is not None:
        student.attend(activity)
