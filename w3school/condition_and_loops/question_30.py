# Problem Statement - Write a Python program to print alphabet pattern 'Z'.

symbol = "Z"

for row in range(7):
    for col in range(7):
        if (row in {0, 6}) or (col + row == 6):
            print(symbol, end="")

        else:
            print(end=" ")

    # Print a new line after printing all the columns for the row
    print()
