# bfs
import sys
from collections import deque

T = int(sys.stdin.readline())
dx, dy = [-1, 0, 0, 1], [0, -1, 1, 0]

def bfs(x, y):
    visited[x][y] = 1
    q = deque()
    q.append((x, y))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx ,ny = x + dx[i], y + dy[i]
            if 0<=nx<H and 0<=ny<W and not visited[nx][ny] and board[nx][ny] == '#':
                q.append((nx, ny))
                visited[nx][ny] = 1

for t in range(T):
    H, W = map(int, sys.stdin.readline().split())
    board = [list(map(str, sys.stdin.readline().strip())) for i in range(H)]
    visited = [[0]*W for i in range(H)]
    cnt = 0

    for i in range(H):
        for j in range(W):
            if board[i][j] == '#' and not visited[i][j]:
                bfs(i, j)
                cnt += 1
    print(cnt)