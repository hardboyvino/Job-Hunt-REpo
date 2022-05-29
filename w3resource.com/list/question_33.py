# Problem Statement - Write a Python program to generate all sublists of a list.

from itertools import combinations


sample_list = [10, 20, 30, 40]

n = 2

all_possible_sublist = [
    sample_list[i : i + n]
    for i in range(len(sample_list))
    if len(sample_list[i : i + n]) == n
]

all_combinations_at_n = [list(sub) for sub in combinations(sample_list, n)]

all_combinations = [
    list(sub)
    for i in range(len(sample_list))
    for sub in combinations(sample_list, i)
    if len(sub) != 0
]

print(all_possible_sublist)
print(all_combinations_at_n)
print(all_combinations)
