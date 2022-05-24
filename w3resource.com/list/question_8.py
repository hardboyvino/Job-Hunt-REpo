# Problem Statement - Write a Python program to check a list is empty or not.

dubset = [1] * 20

empty = []


def check_empty(list):
    if len(list) == 0:
        print(True)
    else:
        print(False)


check_empty(dubset)
check_empty(empty)
