import sys
from collections import deque
from itertools import combinations

def bfs(virus):
    visited = [[-1] * N for _ in range(N)]
    q = deque()
    max_dist = 0
    for v in virus:
        q.append(v)
        visited[v[0]][v[1]] = 0

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0<=nx<N and 0<=ny<N and board[nx][ny] != 1 and visited[nx][ny] == -1:
                visited[nx][ny] = visited[x][y] + 1
                if board[nx][ny] == 0:
                    max_dist = max(max_dist, visited[nx][ny])
                q.append((nx, ny))
    a = list(sum(visited, []))
    if a.count(-1) == list(sum(board, [])).count(1):
        answer.append(max_dist)

dx, dy = [-1, 0, 0, 1], [0, -1, 1, 0]
answer = []
N, M = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
virus_list = []
for i in range(N):
    for j in range(N):
        if board[i][j] == 2:
            virus_list.append([i, j])

for comb in combinations(virus_list, M):
    bfs(comb)

if answer:
    print(min(answer))
else:
    print(-1)