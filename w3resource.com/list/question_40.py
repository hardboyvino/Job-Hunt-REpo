# Problem Statement - Write a Python program to split a list based on first character of word.

from itertools import groupby


sentence = "Write a Python program to split a list based on first character of word."
sample_list = "the quick brown fox jumps over the lazy dog"

sentence = sorted(sentence.split(" "))
sample_list = sorted(sample_list.split(" "))

def letter_in_words(words):
    # For they key and the iterable
    # Use groupby to group all elements of the iterable that match the key as an object
    for letters, words in groupby(words, key=lambda sample_list : sample_list[0]):
        print(letters)
        for word in words:
            print(word)

letter_in_words(sentence)
letter_in_words(sample_list)
