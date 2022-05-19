# Problem Statement - Write a Python program to check whether an alphabet is a vowel or consonant.

vowels = ["a", "e", "i", "o", "u"]

letter = input("Input a letter of the alphabet: ").strip().lower()

if letter.isalpha():
    if letter not in vowels:
        print(f"{letter} is a consonant")
    else:
        print(f"{letter} is a vowel")

else:
    print(f"Enter an alphabet, which {letter} is not")