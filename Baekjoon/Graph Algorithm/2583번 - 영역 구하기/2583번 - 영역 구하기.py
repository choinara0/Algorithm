import sys
from collections import deque

M, N, K = map(int, sys.stdin.readline().split())
matrix = [[0] * N for i in range(M)]

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]
result = []
for i in range(K):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    for j in range(x1, x2):
        for k in range(y1, y2):
            matrix[k][j] = 1

def bfs(x, y):
    q = deque()
    q.append((x, y))
    matrix[x][y] = 1
    area = 1
    while q:
        qx, qy = q.popleft()
        for i in range(4):
            nx, ny = qx + dx[i], qy + dy[i]
            if 0<=nx<M and 0<=ny<N and matrix[nx][ny] == 0:
                matrix[nx][ny] = 1
                q.append((nx,ny))
                area += 1
    result.append(area)
    return

for i in range(M):
    for j in range(N):
        if matrix[i][j] == 0:
            bfs(i, j)

result.sort()
print(len(result))
print(*result)