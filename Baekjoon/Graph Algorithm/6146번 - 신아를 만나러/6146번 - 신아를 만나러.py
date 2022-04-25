import sys
from collections import deque

def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited = [[0] * 1001 for _ in range(1001)]
    visited[x][y] = 1

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0<=nx<=1000 and 0<=ny<=1000:
                if not visited[nx][ny] and board[nx][ny] != 1:

                    if nx == X and ny == Y:
                        return visited[x][y]

                    q.append((nx, ny))
                    visited[nx][ny] = visited[x][y] + 1

    return

X, Y, N = map(int, sys.stdin.readline().split())
X, Y = X + 500, Y + 500
dx, dy = [-1, 0, 0, 1], [0, -1, 1, 0]
board = [[0] * 1001 for _ in range(1001)]
for _ in range(N):
    a, b = map(int, sys.stdin.readline().split())
    board[a+500][b+500] = 1

print(bfs(500, 500))