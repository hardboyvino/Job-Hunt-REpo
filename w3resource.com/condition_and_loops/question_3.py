# Problem Statement - Write a Python program to guess a number between 1 to 9.
# User is prompted to enter a guess. If the user guesses wrong then the prompt appears again until the guess is correct, on successful guess, user will get a "Well guessed!" message, and the program will exit.

from random import randint

python_random = randint(1, 9)

while True:
    try:
        user_guess = int(input("Enter Number: ").strip())
        if user_guess == python_random:
            print("Well guessed!")
            break

    except ValueError:
        print("Enter an integar")
