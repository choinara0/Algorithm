import sys
from collections import deque

N = int(sys.stdin.readline())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
visited = [[0 for _ in range(N)] for __ in range(N)]
dx, dy = [1, 0], [0, 1]

def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = 1

    while q:
        x, y = q.popleft()
        for i in range(2):
            nx, ny = x + (dx[i]*board[x][y]), y + (dy[i]*board[x][y])

            if nx == N-1 and ny == N-1:
                return "HaruHaru"

            if 0<=nx<N and 0<=ny<N and not visited[nx][ny]:
                q.append((nx, ny))
                visited[nx][ny] = 1

    return "Hing"

print(bfs(0, 0))