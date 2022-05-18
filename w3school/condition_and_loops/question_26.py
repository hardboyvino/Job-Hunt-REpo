# Problem Statement - Write a Python program to print alphabet pattern 'S'.

symbol = "S"

for row in range(7):
    for col in range(5):
        if (
            (row in {0, 3, 6} and col in {1, 2, 3})
            or (row in {1, 2, 6} and col == 0)
            or (row in {0, 4, 5} and col == 4)
        ):
            print(symbol, end="")

        else:
            print(end=" ")

    # Print a new line at the end of the row after getting all the columns
    print()

print()

# Pattern 2
for row in range(15):
    for col in range(18):
        if (
            (row in {0, 1, 2, 6, 7, 8, 12, 13, 14})
            or (0 <= col <= 3 and row in {3, 4, 5})
            or (15 <= col <= 17 and row in {9, 10, 11})
        ):
            print(symbol, end="")

        else:
            print(end=" ")
    print()
