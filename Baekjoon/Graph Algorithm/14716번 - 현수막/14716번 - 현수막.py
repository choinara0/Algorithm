import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]
dx = [-1, 0, 1, -1, 1, -1, 0, 1]
dy = [1, 1, 1, 0, 0, -1, -1, -1]
wc = 0

def bfs(x, y):
    q = deque()
    q.append((x, y))

    while q:
        x, y = q.popleft()
        for i in range(8):
            nx, ny = x + dx[i], y + dy[i]
            if 0<=nx<N and 0<=ny<M and not visited[nx][ny]:
                if board[nx][ny] == 1:
                    q.append((nx, ny))
                visited[nx][ny] = 1

for i in range(N):
    for j in range(M):
        if board[i][j] == 1 and not visited[i][j]:
            wc += 1
            visited[i][j] = 1
            bfs(i, j)
print(wc)