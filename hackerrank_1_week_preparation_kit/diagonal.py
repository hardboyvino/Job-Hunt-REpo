arr = [[1,2,3],[4,5,6],[9,8,9]]

def diagonal_diff(arr):
    first_diagonal = 0
    second_diagonal = 0

    for i in range(len(arr)):
        for j in range(len(arr)):
            if i == j:
                first_diagonal += arr[i][j]
            
            if (i + j) == (len(arr) - 1):
                second_diagonal += arr[i][j]

    return abs(first_diagonal - second_diagonal)

diagonal_diff(arr)