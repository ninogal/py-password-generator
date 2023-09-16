#!/usr/bin/env python3

import random
import string

RED = "\033[91m"
GREEN = "\033[92m"
RESET = "\033[0m"


def generate_password(length):

    # Saves one character of each type to ensure its presence in the final string
    letters = random.choice(string.ascii_letters)
    digits = random.choice(string.digits)
    punctuation = random.choice(string.punctuation)

    # Generate remaining characters
    remaining_length = length - 3
    all_chars = string.ascii_letters + string.digits + string.punctuation
    initial_password = ''.join(random.choice(all_chars) for _ in range(remaining_length))

    # Concatenate everything and mix
    initial_password = letters + digits + punctuation + ''.join(random.sample(initial_password, len(initial_password)))
    password_list = list(initial_password)
    random.shuffle(password_list)
    shuffled_password = ''.join(password_list)

    return shuffled_password


def set_password_length():
    while True:
        try:
            password_length = int(input("\nEnter the password length (recommended min. length 12, max length 200): "))
            if 12 <= password_length <= 200:
                break
            else:
                if 7 < password_length < 12:
                    answer = input("\nThe minimum recommended length for a password is 12 characters. "
                                   "Continue anyway? (y/n): ").strip().lower()
                    if answer == 'y':
                        break
                    elif answer == 'n':
                        print("\n✖️ Password generation aborted.")
                        exit()
                    else:
                        print("\nInvalid response. Please enter 'y' for yes or 'n' for no.")
                else:
                    print("\n", RED, "✖️ Password length should be min 8 max 200 characters.", RESET)
        except ValueError:
            print("\n", RED, "✖️ Please enter a numeric value.", RESET)
    return password_length


if __name__ == "__main__":
    password_length = set_password_length()

    while True:
        generated_password = generate_password(password_length)
        print("\n✔️ Here is your generated password:", GREEN, generated_password, RESET)
        regenerate = input("\nDo you want to generate another password with the same length? (y/n): ").strip().lower()
        if regenerate != 'y':
            break
