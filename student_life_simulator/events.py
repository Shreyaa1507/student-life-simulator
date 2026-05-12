from activities import Event


def run_event_activity(student=None):
    """Ask about event attendance and display social and learning results."""
    event = input("Would you like to attend an event? ")
    event_lower = event.lower()

    social = 0
    learning = 0
    event_activity = None

    if event_lower == "yes":
        event_type = input("What event would you like to attend? ")

        if event_type == "First Year CS Festival":
            event_activity = Event(event_type, 100, 0)
        elif event_type == "Study group":
            event_activity = Event(event_type, 50, 50)
        elif event_type == "Movie night":
            event_activity = Event(event_type, 200, -50)
        else:
            event_activity = Event(event_type, 0, 0)

        learning, social, attendance = event_activity.gains()

        print(f"Social improved: {social}")

        if learning < 0:
            print(f"Learning decreased: {abs(learning)}")
        else:
            print(f"Learning improved: {learning}")

    if student is not None and event_activity is not None:
        student.attend(event_activity)
