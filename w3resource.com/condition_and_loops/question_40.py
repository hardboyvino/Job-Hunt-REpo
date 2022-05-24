# Problem Statement - Write a Python program to find the median of three values.

# Create an empty list for all the user input numbers
numbers = []

# Initialise the i to 0
i = 0

while i < 3:
    num = int(input("Enter number: ").strip())
    numbers.append(num)
    i += 1

# Sort the list
numbers = sorted(numbers)

# Take the middle number in the list as the median
print(numbers[len(numbers) // 2])