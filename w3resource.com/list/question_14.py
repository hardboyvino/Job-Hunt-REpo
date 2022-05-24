# Problem Statement - Write a Python program to print the numbers of a specified list after removing even numbers from it.

sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 9] * 10

# Again wiht the list comprehension
# For every number in the list
# If the number is not divisible by 2 then add it to the new_list
print([nums for nums in sample_list if nums % 2 != 0])
