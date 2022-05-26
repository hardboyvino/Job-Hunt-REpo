# Problem Statement - Write a Python program to get the frequency of the elements in a list.

from collections import Counter


list_1 = [1, 4, 5, 3, 2, 6] * 5

uniques = list(set(list_1))

# for uniques in range(len(list_1)):
#     if uniques in list_1:
#         print(list_1.count(uniques))


# Use the Counter class from collections module to automatically count all the occurences of an item in a list
# Turn it into a dict to keep the data structure cleaner
final = dict(Counter(sorted(list_1),))
print(final)
