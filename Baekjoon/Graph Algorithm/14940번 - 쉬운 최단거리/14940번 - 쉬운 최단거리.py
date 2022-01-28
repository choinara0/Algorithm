import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for i in range(n)]
visited= [[-1]*m for i in range(n)]
dx, dy = [-1, 0, 0, 1], [0, -1, 1, 0]
target_x, target_y = 0, 0

for i in range(n):
    for j in range(m):
        if board[i][j] == 2:
            target_x = i
            target_y = j
            break
visited[target_x][target_y] = 0

def bfs(x, y):
    q = deque()
    q.append((x, y))

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0<=nx<n and 0<=ny<m and board[nx][ny] == 1 and visited[nx][ny] == -1:
                q.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1

    return

bfs(target_x, target_y)
for i in range(n):
    for j in range(m):
        if board[i][j] == 0:
            visited[i][j] = 0

for i in range(n):
    print(' '.join(map(str, visited[i])))
