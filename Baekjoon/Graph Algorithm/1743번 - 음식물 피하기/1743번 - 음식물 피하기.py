import sys
from collections import deque

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]
N, M, K = map(int ,sys.stdin.readline().split())
matrix = [[0]*M for i in range(N)]
visited = [[0]*M for i in range(N)]

for i in range(K):
    a, b = map(int, sys.stdin.readline().split())
    matrix[a-1][b-1] = 1

def bfs(x, y):
    visited[x][y] = 1
    cnt = 1
    q = deque()
    q.append((x, y))
    while q:
        qx, qy = q.popleft()
        for i in range(4):
            nx, ny = qx + dx[i], qy + dy[i]
            if 0<=nx<N and 0<=ny<M and not visited[nx][ny] and matrix[nx][ny] == 1:
                visited[nx][ny] = 1
                cnt += 1
                q.append((nx, ny))
    return cnt

answer = 0
for i in range(N):
    for j in range(M):
        if matrix[i][j] == 1 and not visited[i][j]:
            answer = max(answer, bfs(i, j))
print(answer)