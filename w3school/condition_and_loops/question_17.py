# Problem Statement - Write a Python program to print alphabet pattern 'A'

symbol = "A"

# Method 1
# def print_symbol_space_symbol(symbol, repeation):
#     for _ in range(repeation):
#         print(symbol, end=" ")
#         print(end=" ")
#         print(end=" ")
#         print(symbol)
# # Design each line one at a time

# # Line 1
# print(end=" ")
# print(symbol * 3)

# # Line 2 and 3
# print_symbol_space_symbol(symbol, 2)

# # Line 4
# print(symbol * 5)

# # Line 5 to 7
# print_symbol_space_symbol(symbol, 3)


# Method 2
for row in range(7):
    for col in range(5):
        if ((row == 0 or row == 3) and (col == 1 or col == 2 or col == 3)) or (
            row != 0 and (col == 0 or col == 4)
        ):
            print(symbol, end="")
        else:
            print(end=" ")

    # Print a new line after printing all the columns for the row
    print()
