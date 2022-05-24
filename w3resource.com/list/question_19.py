# Problem Statement - Write a Python program to get the difference between the two lists.

list_1 = [1, 2, 3, 4, 5] * 5

list_2 = [3, 4, 5, 6, 7] * 5

# For every element in list_1 if it is not in list_2, add to the difference list
difference = [x for x in list_1 if x not in list_2]

# Print all the duplicates
print(difference)

# Print only unique items from the differences
print(list(set(difference)))