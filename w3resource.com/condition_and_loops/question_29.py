# Problem Statement - Write a Python program to print alphabet pattern 'X'.

symbol = "*"

for row in range(7):
    for col in range(5):
        if (
            (row in {0, 1, 5, 6} and col in {0, 4})
            or (row in {2, 4} and col in {1, 3})
            or (row == 3 and col == 2)
        ):
            print(symbol, end="")

        else:
            print(end=" ")

    # Print a new line after printing all the columns for the row
    print()
