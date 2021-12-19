import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for i in range(N)]
dx, dy = [-1, 0, 0, 1], [0, -1, 1, 0]
time = 0

while True:
    q = deque()
    q.append((0, 0))
    visited = [[0]*M for i in range(N)]
    visited[0][0] = 1

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0<=nx<N and 0<=ny<M and not visited[nx][ny]:
                if board[nx][ny]:
                    board[nx][ny] += 1
                else:
                    visited[nx][ny] = 1
                    q.append((nx, ny))
    flag = 0
    for i in range(N):
        for j in range(M):
            if board[i][j] >= 3:
                board[i][j] = 0
            elif 0 < board[i][j]:
                flag = 1
                board[i][j] = 1

    time += 1
    if not flag:
        print(time)
        break