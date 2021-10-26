import sys
from collections import deque

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

N, M = map(int, sys.stdin.readline().split())
matrix = [list(sys.stdin.readline().rstrip()) for i in range(N)]

def bfs(x, y):
    q.append((x, y, 0))
    visited[x][y] = 1
    distance = 0

    while q:
        qx, qy, qd = q.popleft()
        for i in range(4):
            nx, ny = qx + dx[i], qy + dy[i]
            if 0<=nx<N and 0<=ny<M and matrix[nx][ny] == 'L' and visited[nx][ny] == 0:
                visited[nx][ny] = visited[qx][qy] + 1
                q.append((nx, ny, qd+1))
                distance = qd + 1

    return distance

cnt = 0
q = deque()

for i in range(N):
    for j in range(M):
        if matrix[i][j] == 'L':
            visited = [[0] * M for i in range(N)]
            cnt = max(cnt, bfs(i, j))

print(cnt)