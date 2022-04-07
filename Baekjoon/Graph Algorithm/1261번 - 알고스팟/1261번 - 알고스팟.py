import sys
from collections import deque

def bfs():
    q = deque()
    q.append([0, 0])
    dist[0][0] = 0

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0<=nx<N and 0<=ny<M:
                if dist[nx][ny] == -1:
                    if arr[nx][ny] == 0:
                        dist[nx][ny] = dist[x][y]
                        q.appendleft([nx, ny])
                    else:
                        dist[nx][ny] = dist[x][y] + 1
                        q.append([nx, ny])

    return dist[N-1][M-1]


M, N = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]
dist = [[-1] * M for _ in range(N)]
dx, dy = [-1, 0, 0, 1], [0, -1, 1, 0]

print(bfs())