# Problem Statement - Write a Python program to get unique values from a list.


list_1 = [1, 4, 5, 3, 2, 6] * 5

# Turn the whole list to a set
# Then turn it back to a list of only unique items
# Turn the set back into a list
uniques = list(set(list_1))

print(uniques)