#1
def create_special_matrix(n):
    if n % 2 != 0:
        raise ValueError("n должно быть четным")
    matrix = []
    for i in range(1, n+1):
        row = [i] * (n - i + 1) + [0] * (i - 1)
        matrix.append(row)
    return matrix


n = 4
matrix = create_special_matrix(n)
for row in matrix:
    print(row)

#2

import numpy as np

def move_max_to_corner(matrix):
    matrix = np.array(matrix)
    max_val = np.max(matrix)
    rows, cols = np.where(matrix == max_val)
    i, j = rows[0], cols[0]  
    matrix[[0, i]] = matrix[[i, 0]]
    matrix[:, [0, j]] = matrix[:, [j, 0]]
    return matrix.tolist()


matrix = [
    [5, 2, 3],
    [4, 9, 6],
    [7, 8, 1]
]
result = move_max_to_corner(matrix)
for row in result:
    print(row)

#3 

import numpy as np

def divide_by_determinant(matrix):
    matrix = np.array(matrix, dtype=float)
    det = np.linalg.det(matrix)
    if det == 0:
        raise ValueError("Определитель равен нулю, деление невозможно")
    return (matrix / det).tolist()
A = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
try:
    result = divide_by_determinant(A)
    for row in result:
        print([f"{x:.2f}" for x in row])
except ValueError as e:
    print(e)
B = [
    [2, 0, 1],
    [0, 1, 2],
    [3, 1, 1]
]
result = divide_by_determinant(B)
for row in result:
    print([f"{x:.2f}" for x in row])