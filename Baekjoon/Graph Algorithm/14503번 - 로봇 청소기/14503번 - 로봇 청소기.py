import sys
from collections import deque

def bfs(x, y, d):
    q = deque()
    q.append((x, y, d))
    visited = [[0] * M for _ in range(N)]
    visited[x][y] = 1
    count = 1

    while q:
        x, y, d = q.popleft()
        nd = d
        flag = 0
        for i in range(4):
            nd -= 1
            if nd < 0:
                nd = 3
            nx, ny = x + dx[nd], y + dy[nd]
            if 0<=nx<N and 0<=ny<M and not visited[nx][ny]:
                if board[nx][ny] == 0:
                    visited[nx][ny] = 1
                    q.append((nx, ny, nd))
                    count += 1
                    flag = 1
                    break

        if flag == 1:
            continue
        else:
            nx, ny = x - dx[nd], y - dy[nd]
            if 0<=nx<N and 0<=ny<M:
                if board[nx][ny] == 0:
                    q.append((nx, ny, nd))

    return count

N, M = map(int, sys.stdin.readline().split())
r, c, d = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
print(bfs(r, c, d))