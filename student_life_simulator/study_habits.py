from activities import Lecture, Workshop
from lecture import attend_lecture
from workshop import attend_workshop


def read_workshops(filename, student):
    """Read workshop records from a file and update student data."""
    with open(filename, "r") as file:
        lines = file.readlines()

    if not lines or lines[0].strip() != "Workshops":
        return student

    for line in lines[1:]:
        if not line.strip():
            continue

        parts = [part.strip() for part in line.split(",")]

        if len(parts) != 3:
            continue

        try:
            time = int(parts[0])
            collaboration = parts[1] == "True"
            complete = parts[2] == "True"
        except ValueError:
            continue

        if attend_workshop(time, collaboration, complete) is None:
            continue

        student.attend(Workshop(time, collaboration, complete))

    return student


def read_lectures(filename, student):
    """Read lecture records from a file and update student data."""
    with open(filename, "r") as file:
        lines = file.readlines()

    if not lines or lines[0].strip() != "Lectures":
        return student

    for line in lines[1:]:
        if not line.strip():
            continue

        parts = [part.strip() for part in line.split(",")]

        try:
            time_focused = int(parts[0])
            distractions = parts[1:]
        except (IndexError, ValueError):
            continue

        if attend_lecture(time_focused, distractions) is None:
            continue

        student.attend(Lecture(time_focused, distractions))

    return student
