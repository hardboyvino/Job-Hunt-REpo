# Problem Statement - Write a Python program to create the multiplication table (from 1 to 10) of a number. 

# Get the number we need multilication table for
num = int(input("Number to multiply: ").strip())

# For i between 1 and 10, print the line 6 x 1 = 6 (something like this)
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")
