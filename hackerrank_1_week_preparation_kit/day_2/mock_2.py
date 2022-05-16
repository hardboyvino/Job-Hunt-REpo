import numpy as np

arr = [112, 42, 83, 119], [56, 125, 56, 49], [15, 78, 101, 43], [62, 98, 114, 108]
\\
matrix = np.array(
    [[112, 42, 83, 119], [56, 125, 56, 49], [15, 78, 101, 43], [62, 98, 114, 108]]
)

for column in range(0, (len(matrix))):
    if (
        (matrix[len(matrix) - 1][column]) > (matrix[0][column])
        and (matrix[len(matrix) - 1][column]) > (matrix[1][column])
    ) or (
        (matrix[len(matrix) - 2][column]) > (matrix[0][column])
        and (matrix[len(matrix) - 2][column]) > (matrix[1][column])
    ):
        matrix[:, column] = np.flip(matrix[:, column])

matrix = matrix.tolist()

for row in matrix:
    if (max(row) != row[0]) and (max(row) != row[1]):
        row.reverse()
print(matrix[0][0] + matrix[0][1] + matrix[1][0] + matrix[1][1])
print(matrix)
