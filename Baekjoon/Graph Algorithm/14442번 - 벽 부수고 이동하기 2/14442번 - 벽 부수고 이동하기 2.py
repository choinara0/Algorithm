import sys
from collections import deque

N, M, K = map(int, sys.stdin.readline().split())
matrix = [list(map(int, sys.stdin.readline().strip())) for i in range(N)]
countMatrix = [[-1]*M for i in range(N)]
dx, dy = [-1, 0, 0, 1], [0, -1, 1, 0]

def bfs(x,y):
    q = deque()
    q.append([x,y,0])
    visited = [[[0]*(K+1) for _ in range(M)] for _ in range(N)]
    visited[x][y][0] = 1
    while q:
        x,y,cnt = q.popleft()
        if x == N-1 and y == M-1:
            return visited[x][y][cnt]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<N and 0<=ny<M:
                if not visited[nx][ny][cnt]:
                    if matrix[nx][ny] and cnt < K:
                        visited[nx][ny][cnt+1] = visited[x][y][cnt]+1
                        q.append([nx,ny,cnt+1])
                    elif not matrix[nx][ny]:
                        visited[nx][ny][cnt] = visited[x][y][cnt]+1
                        q.append([nx,ny,cnt])

    return -1


print(bfs(0, 0))