# Problem Statement - Write a Python program to construct the following pattern, using a nested loop number.

num = int(input("Number to end at: ").strip())

# for i in range(1, num + 1):
#     for j in range(1, num + 1):

        # If i greater than or equal to j, then print i and change prints auto-newline to nothing
#         if i >= j:
#             print(i, end="")
    # At the end of the row, print a new line
#     print()


# Method 2
for i in range(1, num + 1):
    
    # Print a string version of i, i times
    print(str(i) * i)