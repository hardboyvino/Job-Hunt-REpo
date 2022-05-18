# Problem Statement - Write a Python program to print alphabet pattern 'M'.

# Add extra space to make the M look prettier
symbol = "* "

for row in range(7):
    for col in range(5):
        if (col in {0, 4}) or (row == 2 and col in {1, 3}) or (row == 3 and col == 2):
            print(symbol, end="")
        else:
            # Add double space so it matches with the symbol + space above
            print(end="  ")

    # Print a new line after printing all the columns for the row
    print()
