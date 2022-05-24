# Problem Statement - Write a Python program to create a list of random integers and randomly select multiple items from the said list.

from random import randint, sample


# Create a list of numbers from 100 to 199
random_number = [num for num in range(100, 200)]

# Generate a randomise sample list of 10 numbers from the list with all the numbers being unique
sampling = sample(random_number, 10)

print(random_number)
print(sampling)