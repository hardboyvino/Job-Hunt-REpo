# Problem Statement - Write a Python program to flatten a shallow list.

# If list contains sublist
from itertools import chain


lst = [[10, 20, 30, 40], [50, 60, 70, 80], [90, 100, 110, 120]]

# # Make it one flat list i.e. [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]
# # Just take each individual sublist from the overall list,
# # and then take every item in each sublist and append to the flat list
# flatlist = [item for sublist in lst for item in sublist]


# Method 2 is to use chain from itertools but need to add asterisks on the iterable (the list) 
# to ensure the list unpacked before iteration
# Else it will become a list within a list
flatlist = list(chain(*lst))

print(flatlist)