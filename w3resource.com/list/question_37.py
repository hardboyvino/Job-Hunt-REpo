# Problem Statement - Write a Python program to find common items from two lists.

sample_list = [1, 2, 3, 4, 5] * 10

other_list = [3, 5, 6, 7, 8] * 5

print([i for i in set(sample_list) if i in set(other_list)])
