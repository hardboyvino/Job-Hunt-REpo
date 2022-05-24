# Problem Statement - Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples.

sample_list = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

# Sort the list but the key should be the 2nd items in the tuple, not the first which is used by default
# Lambda function is used because its better than creating a new function which would have made the sorted be:
# def last_item(word):
# return word[-1]
# sample_list = sorted(sample_list, key=last_item)
sample_list = sorted(sample_list, key=lambda x: x[1])

print(sample_list)
