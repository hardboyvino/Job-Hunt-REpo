# Problem Statement - Write a Python program to find missing and additional values in two lists.

list_1 = ['a', 'b', 'c', 'd', 'e', 'f']

list_2 = ['d', 'e', 'f', 'g', 'h']

missing_values = [i for i in list_1 if i not in list_2]

additional_values = [i for i in list_2 if i not in list_1]

print(missing_values)
print(additional_values)