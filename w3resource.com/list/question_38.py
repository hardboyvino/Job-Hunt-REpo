# Problem Statement - Write a Python program to change the position of every n-th value with the (n+1)th in a list.
# Sample list: [0, 1, 2, 3, 4, 5]
# Expected Output: [1, 0, 3, 2, 5, 4]

from itertools import chain,  zip_longest


sample_list = [0, 1, 2, 3, 4, 5, 6]

# Take the indexes you want in the order you want them in the new tuple (in this case every 2nd and 1st numbers) because zip_longest creates a list of tuples
# Add a fillvalue (default value) incase the number of items cannot create a full zip_longest
bear = zip_longest(sample_list[1::2], sample_list[::2], fillvalue=0)

# Example of a 3 number swap
# bear = zip_longest(sample_list[2::3], sample_list[1::3], sample_list[::3], fillvalue=0)

# Chain the tuples together into a list. Remember to add asterisks so it unpacks the tuples before adding its individual items into a list
bear = chain(*bear)

print(list(bear))