# Problem Statement - Write a Python program that accepts a word from the user and reverse it.

word = input("What is the word? ").strip()

for char in reversed(word): print(char, end="")
