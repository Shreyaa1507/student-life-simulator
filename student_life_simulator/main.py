from events import run_event_activity
from login import run_login_screen
from lecture import run_lecture_activity
from results import display_result
from student_data import create_student
from units import run_unit_enrollment
from workshop import run_workshop_activity


def main():
    student_details = run_login_screen()

    if student_details:
        name, degree, year_of_study = student_details
        unit_code = run_unit_enrollment()
        student = create_student(name, degree, year_of_study, unit_code)

        run_workshop_activity(student)
        run_lecture_activity(student)
        run_event_activity(student)
        display_result(student)


if __name__ == "__main__":
    main()
