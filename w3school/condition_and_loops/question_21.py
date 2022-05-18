# Problem Statement - Write a Python program to print alphabet pattern 'L'.

symbol = "L"

for row in range(7):
    for col in range(5):
        if col == 0 or row == 6:
            print(symbol, end="")
        else:
            print(end=" ")

    # Print a new line after printing all the columns for the row
    print()
