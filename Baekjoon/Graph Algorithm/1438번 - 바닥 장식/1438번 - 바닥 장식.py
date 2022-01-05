import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
home = [list(map(str, sys.stdin.readline().strip())) for i in range(N)]
dx = [-1, 1]
visited = [[0 for i in range(M)] for j in range(N)]
boardCnt = 0

def bfs(x, y, type):
    visited[x][y] = 1
    q = deque()
    q.append((x, y))
    rowIsTrue = False

    if type == '-':
        rowIsTrue = True

    if rowIsTrue:
        while q:
            x, y = q.popleft()
            for i in range(2):
                nx, ny = x, y + dx[i]
                if 0 <= nx < N and 0 <= ny < M and home[nx][ny] == type and not visited[nx][ny]:
                    q.append((nx, ny))
                    visited[nx][ny] = 1
    else:
        while q:
            x, y = q.popleft()
            for i in range(2):
                nx, ny = x + dx[i], y
                if 0 <= nx < N and 0 <= ny < M and home[nx][ny] == type and not visited[nx][ny]:
                    q.append((nx, ny))
                    visited[nx][ny] = 1


for i in range(N):
    for j in range(M):
        if not visited[i][j]:
            bfs(i, j, home[i][j])
            boardCnt += 1

print(boardCnt)