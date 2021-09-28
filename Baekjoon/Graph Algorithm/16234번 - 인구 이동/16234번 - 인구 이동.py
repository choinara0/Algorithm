import sys
from collections import deque

N, L, R = map(int, sys.stdin.readline().split())
matrix = []
for i in range(N):
    matrix.append(list(map(int, sys.stdin.readline().split())))
dxs = [-1, 0, 0, 1]
dys = [0, -1, 1, 0]
time = 0
def bfs(a, b):
    q = deque()
    q.append([a, b])
    temp = []
    temp.append([a, b])
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dxs[i], y + dys[i]
            if (0<=nx<N and 0<=ny<N) and visited[nx][ny] == 0 and (L <= abs(matrix[nx][ny] - matrix[x][y]) <= R) :
                visited[nx][ny] = 1
                q.append([nx, ny])
                temp.append([nx, ny])

    return temp

while True:
    visited = [[0] * N for i in range(N)]
    flag = False
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:
                visited[i][j] = 1
                t = bfs(i, j)
                if len(t) > 1:
                    flag = True
                    n = sum(matrix[x][y] for x, y in t) // len(t)
                    for x, y in t:
                        matrix[x][y] = n

    if not flag:
        break
    time += 1

print(time)