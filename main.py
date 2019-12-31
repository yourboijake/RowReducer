import numpy as np

def rowReducer(matrix):
    #determine matrix shape to find max number of pivots
    dim = matrix.shape
    num_rows = dim[0]
    num_cols = dim[1]
    if num_rows < num_cols:
        pivots = num_rows
    else:
        pivots = num_cols

    #identify necessary row reduction values (labeled mult), and multiply other rows accordingly
    for x in range(pivots):
        for y in range(x):
            if matrix[x][x] != 0:
                mult = -1 * matrix[y][x]/matrix[x][x]
            else:
                mult = 0
            if matrix[y][x] != 0:
                for z in range(num_cols):
                        matrix[y][z] = matrix[y][z] + mult * matrix[x][z]
        for y in range(x+1, num_rows):
            if matrix[x][x] != 0:
                mult = -1 * matrix[y][x]/matrix[x][x]
            else:
                mult = 0
            if matrix[y][x] != 0:
                for z in range(num_cols):\
                        matrix[y][z] = matrix[y][z] + mult * matrix[x][z]

    #reduce pivots to 1, change other row values accordingly
    for x in range(num_rows):
        for y in range(num_cols):
            if matrix[x][y] != 0:
                reduce_ratio = 1/matrix[x][y]
                break
        for z in range(num_cols):
            matrix[x][z] = matrix[x][z] * reduce_ratio

    return matrix

#sample cases
m1 = np.array([[1.0, 2.0, 5.0], [4.0, 19.0, 6.0]])
m2 = np.array([[4.0, 0.0], [6.0, 7.0]])
m3 = np.array([[4.1, 6.3, 7.8], [2.9, 6.7, 5.4], [1.8, 67.3, 7.4]])
print(m1)
print(rowReducer(m1))
print(m2)
print(rowReducer(m2))
print(m3)
print(rowReducer(m3))
