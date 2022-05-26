# Problem Statement - Write a Python program to find the index of an item in a specified list.

# Get the list
word_list = "The quick brown fox jumps over the lazy dog".split(" ")

# If item in list, print index
word = "brown"

# Long method
# for index, words in enumerate(word_list):
#     if words == word:
#         print(index)

# Pythonic method
print(word_list.index(word))
        