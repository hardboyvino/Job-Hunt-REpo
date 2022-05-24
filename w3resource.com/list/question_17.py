# Problem Statement - Write a Python program to generate and print a list except for the first 5 elements, where the values are square of numbers between 1 and 30 (both included).

# See question 16 for explanation
nums_list = [(nums * nums) for nums in range(1, 31)]

print(nums_list[5:])