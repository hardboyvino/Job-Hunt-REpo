# Problem Statement - Write a Python program that accepts a string and calculate the number of digits and letters

# Initialise all the counters to zero by saying they all equal eachother which equals 0
letters = digits = space = others = 0

sentence = input("Text: ").strip()

for char in sentence:
    if char.isalpha():
        letters += 1

    elif char.isdigit():
        digits += 1

    elif char.isspace():
        space += 1

    else:
        others += 1

print(f"Letters {letters}")
print(f"Digits {digits}")
print(f"Spaces {space}")
print(f"Others {others}")
