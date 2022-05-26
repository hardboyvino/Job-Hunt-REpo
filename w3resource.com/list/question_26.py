# Problem Statement - Write a python program to check whether two lists are circularly identical.


list_1 = [9, 8, 0, 7, 6, 5, 4, 3, 2, 1]

list_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 98]

if sorted(list_1) == sorted(list_2):
    print(True)

else:
    print(False)
