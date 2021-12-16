import sys
from collections import deque

N, K = map(int ,sys.stdin.readline().split())
board = []
virus = []
for i in range(N):
    board.append(list(map(int, sys.stdin.readline().split())))
    for j in range(N):
        if board[i][j] != 0:
            virus.append((board[i][j], i, j))
virus.sort()
S, X, Y = map(int, sys.stdin.readline().split())
dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

def bfs(s, X, Y):
    q = deque(virus)
    time = 0

    while q:
        if time == s:
            break
        for _ in range(len(q)):
            prev, x, y = q.popleft()
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0<=nx<N and 0<=ny<N and board[nx][ny] == 0:
                    board[nx][ny] = board[x][y]
                    q.append((prev, nx, ny))
        time += 1
    return board[X-1][Y-1]

print(bfs(S, X, Y))