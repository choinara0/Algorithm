import sys
from collections import deque

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]
N, M = map(int, sys.stdin.readline().split())
paper = [list(map(int, sys.stdin.readline().split())) for i in range(N)]
visited = [[0] * M for i in range(N)]

def bfs(x, y):
    q.append((x, y))
    wide = 1

    while q:
        qx, qy = q.popleft()

        for i in range(4):
            nx, ny = qx + dx[i], qy + dy[i]

            if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == 0 and paper[nx][ny] == 1:
                visited[nx][ny] = 1
                q.append((nx, ny))
                wide += 1

    return wide

q = deque()
drawCnt, drawWide = 0, 0

for i in range(N):
    for j in range(M):
        if paper[i][j] == 1 and visited[i][j] == 0:
            drawCnt += 1
            visited[i][j] = 1
            drawWide = max(drawWide, bfs(i, j))

print(drawCnt)
print(drawWide)