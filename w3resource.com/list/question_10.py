# Problem Statement - Write a Python program to find the list of words that are longer than n from a given list of words.


def find_words(list, n):
    print([word for word in list if len(word) > n])


# Given a sentence, using split forms a list automatically
words = "The quick brown fox jumps over the lazy dog"
sentence = sorted(words.split(" "))

sample_list = ["abc", "xyz", "aba", "1221"]

# The function can be used to search the list and get every string that meets the function criteria
find_words(sentence, 3)
