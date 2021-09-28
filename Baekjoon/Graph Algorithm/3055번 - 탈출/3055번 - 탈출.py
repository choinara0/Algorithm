import sys
from collections import deque

dxs = [-1, 0, 0, 1]
dys = [0, -1, 1, 0]


R, C = map(int, sys.stdin.readline().split())
visit=[[0]*C for _ in range(R)]
matrix = []
for i in range(R):
    matrix.append(list(sys.stdin.readline().strip()))

q = deque()
flag = False
target_x, target_y = 0, 0
for i in range(R):
    for j in range(C):
        if matrix[i][j] == 'S':
            q.appendleft((i, j))
        elif matrix[i][j] == '*':
            q.append((i, j))
        elif matrix[i][j] == 'D':
            target_x = i
            target_y = j

while q:

    if flag:
        break

    x, y = q.popleft()

    for i in range(4):
        nx, ny = x + dxs[i], y + dys[i]
        if nx<0 or nx>=R or ny<0 or ny>=C:
            continue
        if matrix[x][y] == '*':
            if matrix[nx][ny] == '.' or matrix[nx][ny] == 'S':
                matrix[nx][ny] = '*'
                q.append((nx, ny))
        elif matrix[x][y] == 'S':
            if matrix[nx][ny] == '.':
                matrix[nx][ny] = 'S'
                visit[nx][ny] = visit[x][y] + 1
                q.append((nx, ny))
            elif matrix[nx][ny] == 'D':
                flag = True
                visit[nx][ny] = visit[x][y] + 1
                break

if visit[target_x][target_y] == 0:
    print('KAKTUS')
else:
    print(visit[target_x][target_y])