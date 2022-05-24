# Problem Statement - Write a Python program to shuffle and print a specified list.

from sklearn.utils import shuffle


sample_list = ["Red", "Green", "White", "Black", "Pink", "Yellow"]

# Shuffle the list using shuffle from the random module
sample_list = shuffle(sample_list)

print(sample_list)
