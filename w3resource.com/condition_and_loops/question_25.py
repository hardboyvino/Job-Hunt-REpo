# Problem Statement - Write a Python program to print alphabet pattern 'R'.

symbol = "R"

for row in range(7):
    for col in range(5):
        if (
            col == 0
            or (row in {0, 3} and col in {1, 2, 3})
            or (row in {1, 2, 6} and col == 4)
            or (row == 4 and col == 2)
            or (row == 5 and col == 3)
        ):
            print(symbol, end="")
        else:
            print(end=" ")

    # Print a new line after printing all the columns for the row
    print()
