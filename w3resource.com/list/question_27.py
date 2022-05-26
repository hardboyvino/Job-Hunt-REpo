# Problem Statement - Write a Python program to find the second smallest number in a list.

list_1 = [1, 4, 5, 3, 2, 6] * 5

# Turn the whole list to a set
# Then turn it back to a list of only unique items
# Sort the list because sets do not guarantee returning ordered set
# Pick the 2nd item (index = 1) as the second smallest item
second_smallest = sorted(list(set(list_1)))[1]

print(second_smallest)