# Problem Statement - Write a Python program to generate a 3*4*6 3D array whose each element is *.

# Print 3 columns of char
# All colummns are in 4 rows
# The 3 by 4 in present in the z-axis 6 times
# Kind of confusing and trippy
new_list = [[["#" for _ in range(3)] for _ in range(4)] for _ in range(6)]

print(new_list)
