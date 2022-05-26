# Problem Statement - Write a Python program to find the second largest number in a list.

list_1 = [1, 4, 5, 3, 2, 6] * 5

# Turn the whole list to a set
# Then turn it back to a list of only unique items
# Sort the list because sets do not guarantee returning ordered set
# Pick the 2nd to last item (index = -2) as the second largest item
second_largest = sorted(list(set(list_1)))[-2]

print(second_largest)