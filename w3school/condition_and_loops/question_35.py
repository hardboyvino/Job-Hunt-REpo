# Problem Statement - Write a Python program to check a string represent an integer or not.
string = input("Input a string: ").strip()

while True:
    try:
        if int(string):
            print("The string is an integer.")
            break
    except ValueError:
        print("The string is not an integer. ")
        break
