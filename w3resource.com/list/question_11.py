# Problem Statement - Write a Python function that takes two lists and returns True if they have at least one common member.

words = "The quick brown fox jumps over the lazy dog"
sentence = sorted(words.split(" "))

sample_list = ["abc", "xyz", "aba", "1221", "brown"]

# Using an excessive amount of list comprehension
# For every word in sentence compared to every word in sample_list, if common word is found, append to a nameless list
# This nameless list has at least 1 element (i.e. length is greater than 0) then print True
if len([word for word in sentence for sample in sample_list if word == sample]) > 0:
    print(True)
else:
    print(False)
