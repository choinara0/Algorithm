import sys
from collections import deque

n = int(sys.stdin.readline())
board = [list(map(int, sys.stdin.readline().strip())) for i in range(n)]
dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]
visited = [[-1]*n for i in range(n)]

def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = 0
    while q:
        x, y = q.popleft()
        if x == n-1 and y == n-1:
            print(visited[x][y])
            return
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0<=nx<n and 0<=ny<n and visited[nx][ny] == -1:
                if board[nx][ny] == 1:
                    visited[nx][ny] = visited[x][y]
                    q.appendleft((nx, ny))
                else:
                    visited[nx][ny] = visited[x][y]+1
                    q.append((nx, ny))

bfs(0, 0)