import sys
from collections import deque

K = int(sys.stdin.readline())
W, H = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for i in range(H)]
dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]
hdx = [-2, -2, -1, -1, 1, 1, 2, 2]
hdy = [-1, 1, -2, 2, -2, 2, -1, 1]

def bfs():
    q = deque()
    q.append((0, 0, 0))
    visited = [[[0 for i in range(31)] for i in range(W)] for i in range(H)]

    while q:
        x, y, z = q.popleft()
        if x == H-1 and y == W-1:
            return visited[x][y][z]
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < H and 0 <= ny < W and board[nx][ny] == 0 and visited[nx][ny][z] == 0:
                q.append((nx, ny, z))
                visited[nx][ny][z] = visited[x][y][z] + 1
        if z < K:
            for i in range(8):
                nx, ny = x + hdx[i], y + hdy[i]
                if 0 <= nx < H and 0 <= ny < W and board[nx][ny] == 0 and visited[nx][ny][z+1] == 0:
                    q.append((nx, ny, z+1))
                    visited[nx][ny][z+1] = visited[x][y][z] + 1

    return -1

print(bfs())
