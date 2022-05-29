# Problem Statement - Write a Python program to count the number of elements in a list within a specified range.

list = [1, 2, 3, 4, 5 , 6] * 5

# Initialise counter to zero
counter = 0

# For every element in the list
for i in list:

    # If the element is between the specified range
    if 3 < i < 7:

        # Add to the counter
        counter += 1

# On the side, created a new list with all the numbers that will be in the counter
range_number = sorted([num for num in list if 3 < num < 7])

# Print both things out
print(range_number)
print(len(range_number))
print(counter)
