import random
import string


def generate_password(length: int) -> str:
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password


if __name__ == "__main__":
    try:
        length = int(input("Input the length for the password: "))
        if length <= 0:
            print("Input positive length.")
        else:
            password = generate_password(length)
            print("Generated Password: ", password)
    except ValueError:
        print("Please enter a valid integer for the password length.")
