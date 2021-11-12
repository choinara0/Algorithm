import sys
from collections import deque
from itertools import combinations

N, M = map(int, sys.stdin.readline().split())
matrix = []
virus = []
wall = 0
dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

for i in range(N):
    matrix.append(list(map(int, sys.stdin.readline().split())))

for i in range(N):
    for j in range(N):
        if matrix[i][j] == 2:
            virus.append((i, j))
        elif matrix[i][j] == 1:
            wall += 1



def bfs(q):
    visited = [[0]*N for i in range(N)]
    for a, b in q:
        visited[a][b] = 1
    time = -1
    cnt = len(q)

    while q:
        for _ in range(len(q)):
            x, y = q.popleft()
            for i in range(4):
                nx, ny = x+dx[i], y+dy[i]
                if 0<=nx<N and 0<=ny<N and not visited[nx][ny] and not matrix[nx][ny] ==1:
                    visited[nx][ny] = 1
                    cnt += 1
                    q.append((nx, ny))
        time += 1

    return cnt, time

answer = float('inf')
for c in combinations(virus, M):
    q = deque()
    for v in c:
        q.append(v)
    cnt, time = bfs(q)
    if cnt + wall == N**2:
        answer = min(answer, time)

if answer == float('inf'):
    print(-1)
else:
    print(answer)

