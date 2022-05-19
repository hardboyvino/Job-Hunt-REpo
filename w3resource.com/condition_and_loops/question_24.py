# Problem Statement - Write a Python program to print alphabet pattern 'P'.

symbol = "P"

for row in range(7):
    for col in range(5):
        if (
            col == 0
            or (row in {0, 3} and col in {1, 2, 3})
            or (row in {1, 2} and col == 4)
        ):
            print(symbol, end="")
        else:
            print(end=" ")

    # Print a new line after printing all the columns for the row
    print()
