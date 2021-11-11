import sys
from collections import deque

dx = [-2, -2, 0, 0, 2, 2]
dy = [-1, 1, -2, 2, -1, 1]
N = int(sys.stdin.readline())
board = [[-1]*N for i in range(N)]
visited = [[0]*N for i in range(N)]
r1, c1, r2, c2 = map(int, sys.stdin.readline().split())

def bfs(x, y, x2, y2):
    q = deque()
    q.append((x, y))
    visited[x][y] = 1
    board[x][y] = 0

    while q:
        qx, qy = q.popleft()
        for i in range(6):
            nx, ny = qx+dx[i], qy+dy[i]
            if 0<=nx<N and 0<=ny<N and not visited[nx][ny]:
                q.append((nx, ny))
                visited[nx][ny] = 1
                board[nx][ny] = board[qx][qy] + 1

    return board[x2][y2]

print(bfs(r1, c1, r2, c2))
