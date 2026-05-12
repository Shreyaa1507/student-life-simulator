def result(student_info):
    """Calculate the student's final grade."""
    if student_info.attendance < 10:
        return "AF"

    score = student_info.learning

    if score >= 3000:
        return "HD"
    elif score >= 2500:
        return "D"
    elif score >= 2000:
        return "CR"
    elif score >= 1500:
        return "P"
    else:
        return "F"


def display_result(student_info):
    """Display the student's final grade."""
    grade = result(student_info)
    print(f"Final grade: {grade}")
