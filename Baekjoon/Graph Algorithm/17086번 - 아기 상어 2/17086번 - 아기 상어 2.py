import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for i in range(N)]
dx = [-1, 0, 1, -1, 1, -1, 0, 1]
dy = [1, 1, 1, 0, 0, -1, -1, -1]
answer = 0

def bfs(x, y):
    q = deque()
    q.append((x, y))
    while q:
        x, y = q.popleft()
        for i in range(8):
            nx, ny = x + dx[i], y + dy[i]
            if 0<=nx<N and 0<=ny<M:
                if board[nx][ny] == 0:
                    q.append((nx, ny))
                    board[nx][ny] = board[x][y] + 1
                elif board[nx][ny] != 0 and board[x][y] + 1 < board[nx][ny]:
                    q.append((nx, ny))
                    board[nx][ny] = board[x][y] + 1

for i in range(N):
    for j in range(M):
        if board[i][j] == 1:
            bfs(i, j)

for i in range(N):
    answer = max(answer, max(board[i]))
print(answer-1)