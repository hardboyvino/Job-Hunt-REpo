#!/bin/python3
# Problem Set - Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers. Then print the respective minimum and maximum values as a single line of two space-separated long integers.

import math
import os
import random
import re
import sys
from itertools import combinations

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#


def miniMaxSum(arr):
    # Get an empty list for all the sums
    sums = []

    # Iterate over the array and get a combo of 4 numbers and sum them up then append to the sum to the sums array
    # This required importing combinations from the itertools module
    for number in combinations(arr, 4):
        sums.append(sum(number))

    # Sort the sums array in ascending order
    sums = sorted(sums)

    # Print the first sum and last sum separated by a space, not a new line
    print(sums[0], end=" ")
    print(sums[-1])


if __name__ == "__main__":

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
