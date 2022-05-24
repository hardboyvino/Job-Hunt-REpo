# Problem Statement - Write a Python program to generate all permutations of a list in Python.

from itertools import permutations

sample_list = sample_list = ["Red", "Green", "White", "Black", "Pink", "Yellow"]

# Create a list of perm from all possible permutation of the sample_list
permutation = [perm for perm in permutations(sample_list)]

print(len(permutation))
