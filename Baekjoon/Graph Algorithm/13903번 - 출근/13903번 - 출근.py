# bfs
import sys
from collections import deque

R, C = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for i in range(R)]
N = int(sys.stdin.readline())
dx, dy = [], []
for i in range(N):
    r, c = map(int, sys.stdin.readline().split())
    dx.append(r)
    dy.append(c)

def bfs():
    q = deque()
    visited = [[0] * C for i in range(R)]
    for i in range(C):
        if board[0][i] == 1:
            q.append((0, i))
            visited[0][i] = 1

    while q:
        x, y = q.popleft()
        for i in range(N):
            nx, ny = x + dx[i], y + dy[i]
            if 0<=nx<R and 0<=ny<C and not visited[nx][ny] and board[nx][ny] == 1:
                if nx == R - 1 and board[nx][ny] == 1:
                    return visited[x][y]
                else:
                    q.append((nx, ny))
                    visited[nx][ny] = visited[x][y] + 1

    return -1
if R == 1:
    print(0)
else:
    print(bfs())