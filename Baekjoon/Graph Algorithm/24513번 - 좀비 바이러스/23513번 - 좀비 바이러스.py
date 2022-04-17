import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
dx, dy = [-1, 0, 0, 1], [0, -1, 1, 0]
q = deque()
for i in range(N):
    for j in range(M):
        if board[i][j] == 1:
            q.append((i, j, 1, 0))
        elif board[i][j] == 2:
            q.append((i, j, 2, 0))

while q:
    x, y, v, t = q.popleft()
    if board[x][y] != 3:
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx<0 or nx>=N or ny<0 or ny>=M:
                continue
            if board[nx][ny] == 0:
                board[nx][ny] = v
                visited[nx][ny] = t + 1
                q.append((nx, ny, v, t+1))
            elif board[nx][ny] != -1 and board[nx][ny] != v:
                if visited[nx][ny] == t+1:
                    board[nx][ny] = 3

v1_cnt, v2_cnt, v3_cnt = 0, 0, 0
for i in range(N):
    for j in range(M):
        if board[i][j] == 1:
            v1_cnt += 1
        elif board[i][j] == 2:
            v2_cnt += 1
        elif board[i][j] == 3:
            v3_cnt += 1

print(v1_cnt, v2_cnt, v3_cnt)