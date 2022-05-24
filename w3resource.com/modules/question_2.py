from csv import DictReader
from random import choice, randint
import os

number_list = [1, 2, 3, 4, 5]
number_set = {1, 2, 3, 4, 5}
number_dict = {"First": 1, "Second": 2, "Third": 3, "Fourth": 4, "Fifth": 5}

# Get a random element from a list
print(choice(number_list))

# Get a random element from a set
print(choice(list(number_set)))

# Get a random elements value from a dictionary
selection = list(number_dict)
print(number_dict[choice(selection)])

# # Get a random element from the current directory
print(choice(os.listdir()))
