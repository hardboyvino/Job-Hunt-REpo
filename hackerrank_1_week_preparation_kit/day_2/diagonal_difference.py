#!/bin/python3
# Problem Statement - Given a square matrix, calculate the absolute difference between the sums of its diagonals.

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    primary_diagonal_sum = 0
    secondary_diagonal_sum = 0
    
    for number in range(0, len(arr)):
        primary_diagonal_sum += arr[number][number]
        secondary_diagonal_sum += arr[number][len(arr) - (number + 1)]
        
    return abs(primary_diagonal_sum - secondary_diagonal_sum)
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
