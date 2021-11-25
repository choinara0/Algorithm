import sys
from collections import deque

T = int(sys.stdin.readline())
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def bfs():
    cnt = 0
    while q:
        cnt += 1
        while fire and fire[0][2] < cnt:
            x, y, time = fire.popleft()
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < h and 0 <= ny < w:
                    if matrix[nx][ny] == '.' or matrix[nx][ny] == '@':
                        matrix[nx][ny] = '*'
                        fire.append((nx, ny, time+1))

        while q and q[0][2] < cnt:
            x, y, time = q.popleft()
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < h and 0 <= ny < w :
                    if matrix[nx][ny] == '.' and not visited[nx][ny]:
                        visited[nx][ny] = 1
                        q.append((nx, ny, time+1))
                else:
                    return cnt
    return 'IMPOSSIBLE'

for t in range(T):
    w, h = map(int, sys.stdin.readline().split())
    matrix = []
    q = deque()
    fire = deque()
    visited = [[0]*w for i in range(h)]
    for j in range(h):
        matrix.append(list(map(str, sys.stdin.readline().strip())))
        for k in range(w):
            if matrix[j][k] == '@':
                q.append((j, k, 0))
                visited[j][k] = 1
            elif matrix[j][k] == '*':
                fire.append((j, k, 0))
    print(bfs())
