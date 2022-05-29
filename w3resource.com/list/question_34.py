# Problem Statement - Write a Python program using Sieve of Eratosthenes method for computing primes upto a specified number.

# Given the last digit, create a list with list comp (again, loving it!) so all possible numbers are there
n = 100
integers = [i for i in range(2, n+1)]

# # For i in list in range of 2 till len of list
# for i in integers:

# # For index, j element in the list
#     for index, j in enumerate(integers):

# # If j is divisible by i then pop off the list
#         if j % i == 0 and i != j:
#             integers.pop(index)

# When appending or popping with list comp, it mutates the list so be careful when using list comp and it is not to create a brand new list
[integers.pop(index) for i in integers for index, j in enumerate(integers) if j % i == 0 and i != j]

# Count the length of list remaining at the end
print(integers)
print(len(integers))
