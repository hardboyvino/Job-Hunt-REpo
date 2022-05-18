"""" Problem Statement - Write a Python program to check the validity of password input by users. Go to the editor
Validation :

At least 1 letter between [a-z] and 1 letter between [A-Z].
At least 1 number between [0-9].
At least 1 character from [$#@].
Minimum length 6 characters.
Maximum length 16 characters. """"

from string import punctuation


def is_valid_password(word):
    letters = digits = symbols = 0

    for char in word:
        if char.isalpha():
            letters += 1
        elif char.isdigit():
            digits += 1
        elif char in punctuation:
            symbols += 1
    if (letters > 0) and (digits > 0) and (symbols > 0) and (6 <= len(word) <= 16):
        return True
    else:
        return False


if __name__ == "__main__":
    password = input("Password: ")
    if is_valid_password(password) == True:
        print("Valid Password")
    else:
        print("Invalid password")
