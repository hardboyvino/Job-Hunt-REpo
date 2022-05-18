# Problem Statement - Write a Python program to check a triangle is equilateral, isosceles or scalene.

while True:
    try:
        x = float(input("X: ").strip())
        y = float(input("Y: ").strip())
        z = float(input("Z: ").strip())
        break
    except ValueError:
        pass

if (x > 0 and y > 0 and z > 0):
    if x == y == z:
        print("Equilateral triangle")

    elif (x == y) or (x == z) or (y == z):
        print("Isosceles triangle")

    else:
        print("Scalene triangle")
else:
    raise ValueError

