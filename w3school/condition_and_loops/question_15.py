
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
