# Problem Statement - Write a Python program to generate and print a list of first and last 5 elements where the values are square of numbers between 1 and 30 (both included).

# Again loving list comprehension
# For each number in the range of 1 to 31 (since range does not include the last number), square the number
nums_list = [(nums * nums) for nums in range(1,31)]

# Concate and print the first 5 elements to last 5 elements
print(nums_list[:5] + nums_list[-5:])
