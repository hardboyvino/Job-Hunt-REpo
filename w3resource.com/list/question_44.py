# Problem Statement - Write a Python program to generate groups of five consecutive numbers in a list. 

n = 5

# For each column append (5 times row_number) plus column_number
# Do this for i number of rows
print([[5*i + j for j in range(1,6)] for i in range(5)])
