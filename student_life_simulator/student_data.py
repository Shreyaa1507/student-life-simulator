from auth import okta


class Student:
    def __init__(self, name: str, degree: str, year: int, unit: str):
        """Initialise a student with their details and progress values."""
        self.name = name
        self.degree = degree
        self.year = year
        self.unit = unit
        self.social = 0.0
        self.learning = 0.0
        self.attendance = 0

    @okta
    def attend(self, activity):
        """Apply an activity's gains to the student."""
        gains = activity.gains()

        self.learning += gains[0]
        self.social += gains[1]
        self.attendance += gains[2]

    def __str__(self):
        return (
            f"Name:       {self.name}\n"
            f"Degree:     {self.degree}\n"
            f"Year:       {self.year}\n"
            f"Unit:       {self.unit}\n"
            f"Social:     {self.social:.2f}\n"
            f"Learning:   {self.learning:.2f}\n"
            f"Attendance: {int(self.attendance)}"
        )


def create_student(name, degree, year_of_study, unit_code):
    """Store the student's details and starting scores."""
    return Student(name, degree, year_of_study, unit_code)
