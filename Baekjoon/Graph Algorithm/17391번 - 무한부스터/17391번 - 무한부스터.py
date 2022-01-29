import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for i in range(N)]
visited = [[0] * M for i in range(N)]
dx, dy = [1, 0], [0, 1]

def bfs():
    q = deque()
    q.append((0, 0))
    while q:
        x, y = q.popleft()
        for i in range(2):
            nx, ny = x, y
            for j in range(board[x][y]):
                nx, ny = nx + dx[i], ny + dy[i]
                if 0<=nx<N and 0<=ny<M and not visited[nx][ny]:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx, ny))

    return visited[-1][-1]

print(bfs())