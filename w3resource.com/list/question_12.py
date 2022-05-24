# Problem Statement - Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.

sample_list = ["Red", "Green", "White", "Black", "Pink", "Yellow"]

# Loving list comprehension
# For every color in sample list which is also given an index
# If that index is not in a set provided, append it to the new_list
# Else ignore it (Not stated but implied)
new_list = [color for index, color in enumerate(sample_list) if index not in {0, 4, 5}]

print(new_list)
