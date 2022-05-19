# Problem Statement - Write a Python program to count the number of even and odd numbers from a series of numbers.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

count_odd = 0
count_even = 0

for number in numbers:
    if number % 2 == 0:
        count_even += 1
    else:
        count_odd += 1

print(f"Number of even numbers: {count_even}")
print(f"Number of odd numbers: {count_odd}")
