import random
from string import ascii_letters, hexdigits


# # Get a random color hex
# Method 1
print("#{:06x}".format(random.randint(0, 0xFFFFFF)))

# Method 2
print(f"#{random.randint(0, 0xFFFFFF):06x}")

# Method 3
print("#", end="")
for _ in range(6):
    print(random.choice(hexdigits), end="")
print()

# # Get random alphabetical string of length 5
for i in range(5):
    print(random.choice(ascii_letters), end="")
print()

# # Get random value between
print(random.randint(1, 8))

# # Get random multiples of 7 between 0 and 70
# Method 1
while True:
    num = random.randint(0, 70)
    if num % 7 == 0:
        print(num)
        break

# Method 2
print(random.randint(0, 10) * 7)

# Method 3
print(random.randrange(0, 70, 7))
