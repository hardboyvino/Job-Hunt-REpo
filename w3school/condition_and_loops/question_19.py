# Problem Statement - Write a Python program to print alphabet pattern 'E'.

symbol = "E"

for row in range(7):
    for col in range(5):
        if (col == 0) or ((1 <= col <= 4) and (row in {0, 3, 6})):
            print(symbol, end="")
        else:
            print(end=" ")

    # Print a new line after printing all the columns for the row
    print()
