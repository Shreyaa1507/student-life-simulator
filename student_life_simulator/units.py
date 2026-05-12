def is_valid_unit(unit_code: str):
    """Check whether a unit code follows the required format."""
    if len(unit_code) != 8:
        print("Please enter a unit with 8 characters.")
        return False

    if not unit_code[:4].isalpha() or not unit_code[:4].isupper():
        print("Please enter a valid 4 letter code.")
        return False

    if unit_code[4] not in "1234":
        print("Please enter a valid 4 number code.")
        return False

    if not unit_code[5:].isdigit():
        print("Please enter a valid 4 number code.")
        return False

    return True


def run_unit_enrollment():
    """Ask the user to enter a unit code."""
    unit_code = input("What unit would you like to enroll in? ")

    while not is_valid_unit(unit_code):
        unit_code = input("What unit would you like to enroll in? ")

    print(f"You have enrolled in {unit_code}.")
    return unit_code
