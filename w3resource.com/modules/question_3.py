from random import choice, randint
from string import ascii_letters

# Get a random alphabetic character
print(choice(ascii_letters))

# Get a random alphabetic string of random length
for _ in range(randint(1, 50)):
    print(choice(ascii_letters), end="")
print()

# Get a random alphabetic string of fixed length
# Method 1
i = 0

while i < 10:
    print(choice(ascii_letters), end="")
    i += 1
print()

# Method 2
for _ in range(10):
    print(choice(ascii_letters), end="")
print()