# Problem Statement - Write a Python program to print alphabet pattern 'T'.

symbol = "T"


for row in range(7):
    for col in range(5):
        if (row == 0) or (col == 2):
            print(symbol, end="")

        else:
            print(end=" ")

    print()
