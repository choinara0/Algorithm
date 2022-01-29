import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
board = [[0]*N for i in range(N)]
visited = [[-1]*N for i in range(N)]
knight_x, knight_y = map(int, sys.stdin.readline().split())
enemy_list = [list(map(int, sys.stdin.readline().split())) for i in range(M)]
dx, dy = [-2, -2, -1, -1, 1, 1, 2, 2], [-1, 1, -2, 2, -2, 2, -1, 1]

def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = 0

    while q:
        x, y = q.popleft()
        for i in range(8):
            nx, ny = x + dx[i], y + dy[i]
            if 0<=nx<N and 0<=ny<N and visited[nx][ny] == -1:
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx, ny))

    for x, y in enemy_list:
        print(visited[x-1][y-1], end=' ')
    return

bfs(knight_x-1, knight_y-1)