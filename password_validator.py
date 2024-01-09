import string


def validate_password(password: str) -> tuple:
    # Criteria
    min_length = 8
    has_min_length = len(password) >= min_length
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_symbol = any(char in string.punctuation for char in password)

    feedback_messages = {
        'min_length': f"Password is too short. Minimum length is {min_length}",
        'has_upper': "Password must contain at least one uppercase letter",
        'has_lower': "Password must contain at least one lowercase letter",
        'has_digit': "Password must contain at least one digit",
        'has_symbol': "Password must contain at least one symbol"
    }

    feedback = [feedback_messages[criterion] for criterion, meets_criteria in
                {'min_length': has_min_length,
                 'has_upper': has_upper,
                 'has_lower': has_lower,
                 'has_digit': has_digit,
                 'has_symbol': has_symbol}
                .items() if not meets_criteria]

    is_strong = len(feedback) == 0
    return is_strong, feedback


if __name__ == "__main__":
    try:
        password = input("Input password: ")
        is_strong, feedback = validate_password(password)

        if is_strong:
            print("Password is strong!")
        else:
            print("Password is not strong. Feedback:")
            for criterion_feedback in feedback:
                print(criterion_feedback)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
