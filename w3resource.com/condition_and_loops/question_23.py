# Problem Statement - Write a Python program to print alphabet pattern 'O'.

symbol = "O"

for row in range(7):
    for col in range(5):
        if (col in {0, 4} and row not in {0, 6}) or (
            row in {0, 6} and col in {1, 2, 3}
        ):
            print(symbol, end="")
        else:
            print(end=" ")

    # Print a new line after printing all the columns for the row
    print()
