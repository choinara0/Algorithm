import sys
from collections import deque

M, N = map(int, sys.stdin.readline().split())
matrix = [list(map(int, sys.stdin.readline().strip())) for i in range(M)]
visited = [[0]*N for i in range(M)]
dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

def bfs(y):
    q = deque()
    q.append((0,y))
    visited[0][y] = 1

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < M and 0 <= ny < N and not visited[nx][ny] and not matrix[nx][ny]:
                q.append((nx, ny))
                visited[nx][ny] = 1


for i in range(N):
    if matrix[0][i] == 0 and not visited[0][i]:
        bfs(i)

if 1 in visited[M-1]:
    print('YES')
else:
    print('NO')
'''
8 8
11000111
01100000
00011001
11001000
10001001
10111100
01010000
00001011
'''