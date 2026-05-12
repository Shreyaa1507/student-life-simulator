from welcome import BORDER, display_welcome_screen


def get_student_details():
    """Ask the user for their student details."""
    name = input("Enter your full name:         ")
    degree = input("Enter your degree program:    ")
    year_of_study = int(input("Enter your year of study:     "))

    return name, degree, year_of_study


def validate_student_details(name, degree, year_of_study):
    """Check that the student details match the project rules."""
    if len(name) > 25:
        print("Your name is incorrect.")
        return False

    if len(degree) > 25:
        print("Your degree is incorrect.")
        return False

    if year_of_study > 10:
        print("Your year is incorrect.")
        return False

    return True


def display_signup_summary(name, degree, year_of_study):
    """Display the student's sign-up details."""
    print(BORDER)
    print("|           Thank you for signing up!            |")
    print(BORDER)
    print("| Field              | Your Details              |")
    print(BORDER)
    print(f"| Name               | {name:<25} |")
    print(f"| Degree             | {degree:<25} |")
    print(f"| Year of Study      | {year_of_study:<25} |")
    print(BORDER)


def run_login_screen():
    """Run the sign-up/login screen."""
    display_welcome_screen()
    name, degree, year_of_study = get_student_details()

    if validate_student_details(name, degree, year_of_study):
        display_signup_summary(name, degree, year_of_study)
        return name, degree, year_of_study

    return None
