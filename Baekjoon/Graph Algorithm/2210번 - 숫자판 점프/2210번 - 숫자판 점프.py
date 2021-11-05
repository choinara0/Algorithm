import sys
numList = [list(map(int, sys.stdin.readline().split())) for i in range(5)]
dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]
result = []
def dfs(x, y, num):
    if len(num) == 6:
        if num not in result:
            result.append(num)
        return

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0<=nx<5 and 0<=ny<5:
            dfs(nx, ny, num + str(numList[nx][ny]))


for i in range(5):
    for j in range(5):
        dfs(i, j, str(numList[i][j]))

print(len(result))
