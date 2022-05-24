# Problem Statement - Write a Python program to remove duplicates from a list.


duplicates = [1] * 20

dubset = ["abba"] * 10

# Turn the list to a set to remain only unique elements, then turn the set back to a list
# Works for both ints, floats and strings
duplicates = list(set(duplicates))
dubset = list(set(dubset))

print(duplicates)
print(dubset)
