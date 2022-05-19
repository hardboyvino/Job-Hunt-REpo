""" Problem Statement - Write a Python program to construct the following pattern, using a nested for loop.

* 
* * 
* * * 
* * * * 
* * * * * 
* * * * 
* * * 
* * 
* """

while True:
    try:
        pattern_size = int(input("Size: ").strip())
        break
    except ValueError:
        pass

for i in range(1, pattern_size):
    print("* " * i)

for j in range(pattern_size, 0, -1):
    print("* " * j)
