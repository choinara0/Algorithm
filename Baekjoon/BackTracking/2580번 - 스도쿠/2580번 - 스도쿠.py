import sys
matrix = []
for i in range(9):
    matrix.append(list(map(int, sys.stdin.readline().split())))
zeros = []
for i in range(9):
    for j in range(9):
        if matrix[i][j] == 0:
            zeros.append((i, j))

def dfs(idx):
    if idx == len(zeros):
        for i in matrix:
            print(*i)
        sys.exit()
    x = zeros[idx][0]
    y = zeros[idx][1]
    dx = (x // 3) * 3
    dy = (y // 3) * 3
    num = [0] + [1 for i in range(9)]
    for i in range(9):
        if (matrix[x][i]):
            num[matrix[x][i]] = 0
    for i in range(9):
        if (matrix[i][y]):
            num[matrix[i][y]] = 0

    for i in range(dx, dx+3):
        for j in range(dy, dy+3):
            temp = matrix[i][j]
            if temp:
                num[temp] = 0
    tempList = []
    for i in range(len(num)):
        if num[i] == 1:
            tempList.append(i)

    for i in tempList:
        matrix[x][y] = i
        dfs(idx+1)
        matrix[x][y] = 0



dfs(0)