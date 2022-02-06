import sys
from collections import deque

dx = [-1,1,0,0,0,0]
dy = [0,0,-1,1,0,0]
dz = [0,0,0,0,-1,1]

def bfs(z, x, y):
    q = deque()
    q.append((z, x, y))
    visited[z][x][y] = 0

    while q:
        z, x, y = q.popleft()
        for i in range(6):
            nz, nx, ny = z + dz[i], x + dx[i], y + dy[i]
            if 0<=nz<L and 0<=nx<R and 0<=ny<C:
                if building[nz][nx][ny] == 'E':
                    print('Escaped in {} minute(s).'.format(visited[z][x][y] + 1))
                    return
                if visited[nz][nx][ny] == -1 and building[nz][nx][ny] == '.':
                    q.append((nz, nx, ny))
                    visited[nz][nx][ny] = visited[z][x][y] + 1

    print('Trapped!')
    return

while True:
    L, R, C = map(int, sys.stdin.readline().split())
    if L == 0 and R == 0 and C == 0:
        break

    building = [[[] * C for i in range(R)] for j in range(L)]
    visited = [[[-1] * C for i in range(R)] for j in range(L)]

    for l in range(L):
        building[l] = [list(map(str, sys.stdin.readline().strip())) for i in range(R)]
        input()

    for l in range(L):
        for r in range(R):
            for c in range(C):
                if building[l][r][c] == 'S':
                    bfs(l, r, c)
                    break