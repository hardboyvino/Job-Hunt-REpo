# Problem Statement - Write a Python program to print alphabet pattern 'G'.

symbol = "G"

for row in range(7):
    for col in range(5):
        if (
            (row in {0, 6} and col in {1, 2, 3})
            or (col == 0 and row not in {0, 6})
            or (row == 3 and col in {2, 3, 4})
            or (col == 4 and row in {1, 3, 4, 5})
        ):
            print(symbol, end="")
        else:
            print(end=" ")

    # Print a new line after printing all the columns for the row
    print()
