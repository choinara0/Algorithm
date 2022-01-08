import sys
from collections import deque

N, M, T = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for i in range(N)]
visited = [[0 for i in range(M)] for i in range(N)]
dx, dy = [-1, 0, 0, 1], [0, -1, 1, 0]
sword = 10000

def bfs():
    global sword
    q = deque()
    q.append((0, 0))
    visited[0][0] = 1

    while q:
        x, y = q.popleft()
        if board[x][y] == 2:
            sword = N-1-x + M-1-y + visited[x][y]-1
        if x == N-1 and y == M-1:
            return min(visited[x][y]-1, sword)
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0<=nx<N and 0<=ny<M and not visited[nx][ny] and board[nx][ny] != 1:
                q.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1

    return sword

answer = bfs()
print("Fail" if answer>T else answer)