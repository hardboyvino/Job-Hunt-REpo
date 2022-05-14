#!/bin/python3
# Problem statement - Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero. Print the decimal value of each fraction on a new line with  places after the decimal.

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#


def plusMinus(arr):
    countNeg = 0
    countPos = 0
    countZero = 0

    for number in arr:
        if number > 0:
            countPos += 1
        elif number < 0:
            countNeg += 1
        else:
            countZero += 1

    print(f"{countPos/len(arr):.6f}")
    print(f"{countNeg/len(arr):.6f}")
    print(f"{countZero/len(arr):.6f}")


if __name__ == "__main__":
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
