# Problem Statement - Write a Python program to sum of two given integers. However, if the sum is between 15 to 20 it will return 20.

while True:
    try:
        int_1 = int(input("Number 1: ").strip())
        int_2 = int(input("Number 2: ").strip())
        break
    except ValueError:
        pass

if 15 < int_1 + int_2 < 20:
    print("20")

else:
    print(int_1 + int_2)