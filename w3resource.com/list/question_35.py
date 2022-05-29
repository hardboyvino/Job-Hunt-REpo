# Problem Statement - Write a Python program to create a list by concatenating a given list which range goes from 1 to n.
sample_list = ["p", "q"]
n = 5


# Create the number list
numbers = [str(i) for i in range(1, n + 1)]

# For each element in sample_list, concat to numbers list
print([i + j for j in numbers for i in sample_list])

# Method 2
# Everything done in 1 line
# Instead of first creating the numbers list to be used once, just put it directly into the new list
print([f"{i}{j}" for j in range(1, n + 1) for i in sample_list])
