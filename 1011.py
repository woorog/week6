def flip(matrix):
    return matrix[::-1]

def flip2(matrix):
    return [row[::-1] for row in matrix]

def rotate_90_clock(matrix):
    return [list(row) for row in zip(*matrix[::-1])]

def rotate_90_lclock(matrix):
    return [list(row) for row in zip(*matrix)][::-1]

def operation_5(matrix, y, x):
    half_y, half_x = y // 2, x // 2
    new_matrix = [[0] * x for _ in range(y)]
    for i in range(y):
        for j in range(x):
            if i < half_y and j < half_x: # 1 -> 2
                new_matrix[i][j + half_x] = matrix[i][j]
            elif i < half_y and j >= half_x: # 2 -> 3
                new_matrix[i + half_y][j] = matrix[i][j]
            elif i >= half_y and j >= half_x: # 3 -> 4
                new_matrix[i][j - half_x] = matrix[i][j]
            else: # 4 -> 1
                new_matrix[i - half_y][j] = matrix[i][j]
    return new_matrix

def operation_6(matrix, y, x):
    half_y, half_x = y // 2, x // 2
    new_matrix = [[0] * x for _ in range(y)]
    for i in range(y):
        for j in range(x):
            if i < half_y and j < half_x: # 1 -> 4
                new_matrix[i + half_y][j] = matrix[i][j]
            elif i < half_y and j >= half_x: # 2 -> 1
                new_matrix[i][j - half_x] = matrix[i][j]
            elif i >= half_y and j >= half_x: # 3 -> 2
                new_matrix[i - half_y][j] = matrix[i][j]
            else: # 4 -> 3
                new_matrix[i][j + half_x] = matrix[i][j]
    return new_matrix


y, x, tc = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(y)]
case = list(map(int, input().split()))

for ncase in case:
    if ncase == 1:
        board = flip(board)
    elif ncase == 2:
        board = flip2(board)
    elif ncase == 3:
        board = rotate_90_clock(board)
        y, x = x, y
    elif ncase == 4:
        board = rotate_90_lclock(board)
        y, x = x, y
    elif ncase == 5:
        board = operation_5(board, y, x)
    elif ncase == 6:
        board = operation_6(board, y, x)


for row in board:
    print(' '.join(map(str, row)))