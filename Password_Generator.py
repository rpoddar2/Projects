"""A small piece of code for generating a strong password automatically"""

import pyperclip
import random
import string


def password_generator():
    digit = string.digits
    upper = string.ascii_uppercase
    lower = string.ascii_lowercase
    special = string.punctuation
    password = digit + upper + lower + special

    while True:
        try:
            # Taking the user desired length for the password
            print("Password length should be between 8 and 32 chars")
            pass_len = int(input("Enter the length of the password you want - "))
        except ValueError:
            print("Not a number. Please select a number")
            continue

        if pass_len < 8:
            print("Length does not match the criteria. Try again.")
            continue
        else:
            break

    # Logic for generating the password
    again = 'y'
    while pass_len > 7 and again == 'y':
        final = ''.join(random.sample(password, pass_len))

        # Returning the password and copying to the clipboard
        print(f"Your password is - {final}", "It is copied to the clipboard", sep='\n')
        pyperclip.copy(final)
        pyperclip.paste()
        again = input("Press y to generate again, else, n ")


password_generator()
