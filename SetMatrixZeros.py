# Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

def set_matrix_zeros(mat):
    rows = len(mat)
    cols = len(mat[0])
    res = []
    for i in range(rows):
        for j in range(cols):
            if mat[i][j] == 0:
                res.append((i, j))
    for r, c in res:
        for i in range(rows):
            mat[i][c] = 0
        for j in range(cols):
            mat[r][j] = 0
    return mat


m, n = map(int, input().split())
mat = [[int(input()) for i in range(n)] for j in range(m)]
print(set_matrix_zeros(mat))
