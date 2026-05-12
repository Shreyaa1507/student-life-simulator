from activities import Lecture


def attend_lecture(time_focused, distractions):
    """Calculate lecture learning based on focus time and distractions."""
    if time_focused < 1 or time_focused > 100:
        return None

    learning, social, attendance = Lecture(time_focused, distractions).gains()
    return learning


def run_lecture_activity(student=None):
    """Ask about lecture focus and display the learning result."""
    time_focused = int(input("How long did you focus on your lecture? "))
    distractions = input("What distractions do you have? ").split(",")

    if time_focused < 1 or time_focused > 100:
        print("Please enter a valid time between 1 and 100 minutes inclusive.")
        return

    activity = Lecture(time_focused, distractions)
    learning, social, attendance = activity.gains()

    print(f"Learning improved: {learning:.2f}")

    if student is not None:
        student.attend(activity)
