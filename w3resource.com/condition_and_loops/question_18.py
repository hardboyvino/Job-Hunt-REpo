# Problem Statement - Write a Python program to print alphabet pattern 'D'.

symbol = "D"

for row in range(7):
    for col in range(5):
        if (
            (col == 0)
            or ((row == 0 or row == 6) and (col in {1, 2, 3}))
            or ((row not in {0, 6}) and (col == 4))
        ):
            print(symbol, end="")
        else:
            print(end=" ")

    # Print a new line after printing all the columns for the row
    print()
