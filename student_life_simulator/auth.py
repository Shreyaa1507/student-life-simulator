def okta(func):
    """Simulate 2-factor verification before a student attends an activity."""
    login_success_count = {}

    def wrapper(self, *args, **kwargs):
        first_char = self.name[0].lower()
        alphabet = "abcdefghijklmnopqrstuvwxyz"

        if first_char.isalpha():
            letter_number = alphabet.index(first_char)
        else:
            letter_number = 0

        if letter_number < 10:
            position_string = "0" + str(letter_number)
        else:
            position_string = str(letter_number)

        learning_value = int(self.learning)
        learning_string = str(learning_value)

        while len(learning_string) < 4:
            learning_string = "0" + learning_string

        verification_code = position_string + learning_string

        print(verification_code)
        print("Input your verification code:", end=" ")

        if self.name not in login_success_count:
            login_success_count[self.name] = 0

        user_input = input()

        if user_input == verification_code:
            login_success_count[self.name] += 1

            if login_success_count[self.name] % 3 == 0:
                print(verification_code)
                print("Input your verification code:", end=" ")
                user_input_again = input()

                if user_input_again != verification_code:
                    return

            return func(self, *args, **kwargs)

        return

    return wrapper
