import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
board = [list(map(str, sys.stdin.readline().strip())) for i in range(M)]
dx, dy = [-1, 0, 0, 1], [0, -1, 1, 0]
visited = [[0]*N for i in range(M)]
w_power, b_power = 0, 0

def bfs(x, y):
    q = deque()
    q.append((x, y))
    cnt = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0<=nx<M and 0<=ny<N and not visited[nx][ny] and board[x][y] == board[nx][ny]:
                q.append((nx, ny))
                visited[nx][ny] = 1
                cnt += 1
    return cnt + 1

for i in range(M):
    for j in range(N):
        if not visited[i][j] and board[i][j] == 'W':
            visited[i][j] = 1
            w_power += (bfs(i, j) ** 2)
        elif not visited[i][j] and board[i][j] == 'B':
            visited[i][j] = 1
            b_power += (bfs(i, j) ** 2)

print(w_power, b_power)