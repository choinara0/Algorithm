import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
mountain_peak_cnt = 0
dx, dy = [-1, -1, 0, 1, 1, 1, 0, -1], [0, 1, 1, 1, 0, -1, -1, -1]

def bfs(x, y):
    global mountain_peak_flag
    q = deque()
    q.append((x, y))
    visited[x][y] = 1
    while q:
        x, y = q.popleft()
        for i in range(8):
            nx, ny = x + dx[i], y + dy[i]
            if 0<=nx<N and 0<=ny<M:
                if board[nx][ny] > board[x][y]:
                    mountain_peak_flag = False
                if board[nx][ny] == board[x][y] and not visited[nx][ny]:
                    q.append((nx, ny))
                    visited[nx][ny] = 1


for i in range(N):
    for j in range(M):
        if board[i][j] > 0 and not visited[i][j]:
            mountain_peak_flag = True
            bfs(i, j)
            if mountain_peak_flag:
                mountain_peak_cnt += 1

print(mountain_peak_cnt)