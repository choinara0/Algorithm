import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for i in range(n)]
dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]
answer = []
time = 0

def bfs():
    q = deque()
    q.append((0, 0))
    visited[0][0] = 0
    cnt = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0<=nx<n and 0<=ny<m and visited[nx][ny] == 0:
                if board[nx][ny] == 0:
                    visited[nx][ny] = 1
                    q.append((nx, ny))
                else:
                    board[nx][ny] = 0
                    visited[nx][ny] = 1
                    cnt += 1
    answer.append(cnt)
    return cnt

while True:
    time += 1
    visited = [[0]*m for i in range(n)]
    cnt = bfs()
    if cnt == 0:
        break

print(time-1)
print(answer[-2])