import sys
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]
def bfs(x, y):
    q.append((x, y))
    visited[x][y] = cnt
    while (q):
        x, y = q.popleft()

        for j in range(4):
            new_x = x + dx[j]
            new_y = y + dy[j]

            if (0 <= new_x < N and 0 <= new_y < N) and matrix[x][y] == matrix[new_x][new_y] and visited[new_x][new_y] == 0:
                q.append((new_x, new_y))
                visited[new_x][new_y] = 1
N = int(sys.stdin.readline())
matrix = []
for i in range(N):
    matrix.append(list(sys.stdin.readline()))
cnt = 0
visited = [[0]*N for i in range(N)]
q = deque()

for i in range(N):
    for j in range(N):
        if visited[i][j] == 0:
            bfs(i, j)
            cnt += 1
print(cnt, end=' ')

for i in range(N):
    for j in range(N):
        if matrix[i][j] == 'R':
            matrix[i][j] = 'G'
visited = [[0]*N for i in range(N)]
cnt = 0
for i in range(N):
    for j in range(N):
        if visited[i][j] == 0:
            bfs(i, j)
            cnt += 1

print(cnt)





# 5
# RRRBB
# GGBBB
# BBBRR
# BBRRR
# RRRRR
