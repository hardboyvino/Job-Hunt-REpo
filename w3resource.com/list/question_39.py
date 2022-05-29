# Problem Statement - Write a Python program to convert a list of multiple integers into a single integer.
# Sample list: [11, 33, 50]
# Expected Output: 113350

sample_list = [11, 33, 50]

# Method 1
# Use list comp to turn each item in the list into a str from an int as join only works on str
print("".join([str(i) for i in sample_list]))

# Method 2
# Same as method 1 but using map
print("".join(list(map(str, sample_list))))