lines = []

# While the whole code is true
while True:
    # Try to get input of different lines and append the uppercase version of that line to lines list
    try:
        l = input("Lines: ")
        lines.append(l.upper())

    # Use an except of either Ctrl-D or Ctrl-C to error to exit the program and stop asking for new lines
    except (KeyboardInterrupt, EOFError):
        print()
        break

# For each line in the lines list, print the line
for l in lines:
    print(l)
