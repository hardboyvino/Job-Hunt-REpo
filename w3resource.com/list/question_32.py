# Problem Statement - Write a Python program to check whether a list contains a sublist.
from itertools import combinations
list_1 = [2,4,3,5,7]

sublist = [3,7]

# For each i in the range of length of original list
# Take a slice of sublist length but ensure sublist created are exactly the same length of sublist
# This is because if sublist is length 3, program will still take sublist of 2 as valid but we do not want that
combination_list = [list_1[i:i+len(sublist)] for i in range(0, len(list_1)) if len(list_1[i:i+len(sublist)]) == len(sublist)]
print(combination_list)

# Does the sublist exist in the combination list
if sublist in combination_list:
    print(True)

else:
    print(False)