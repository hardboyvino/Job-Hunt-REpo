# Problem Statement - Write a Python program to generate a float between 100 and 200, inclusive and generate a random float within a specific range. Float is to 6 decimal places

from random import uniform

print(f"{uniform(100, 200):.6f}")