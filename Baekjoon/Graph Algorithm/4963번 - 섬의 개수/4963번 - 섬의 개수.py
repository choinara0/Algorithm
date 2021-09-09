import sys

sys.setrecursionlimit(10 ** 6)
move = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, 1), (1, -1)]


def dfs(x, y):
    matrix[x][y] = 2
    for i in move:
        new_x, new_y = x + i[0], y + i[1]
        #print(new_x, new_y)
        #print(matrix)
        if new_x < 0 or new_y < 0 or new_x >= h or new_y >= w:
            continue
        elif matrix[new_x][new_y] == 1:
            dfs(new_x, new_y)

    return


while (1):
    w, h = map(int, sys.stdin.readline().split())
    if w == 0 and h == 0:
        break
    matrix = [[j for j in map(int, sys.stdin.readline().split())] for i in range(h)]

    cnt = 0
    for i in range(h):
        for j in range(w):
            if matrix[i][j] == 1:
                dfs(i, j)
                cnt += 1
    print(cnt)
