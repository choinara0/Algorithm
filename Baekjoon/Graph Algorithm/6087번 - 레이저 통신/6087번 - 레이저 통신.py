import sys
from collections import deque

def bfs(x, y):
    visited = [[sys.maxsize] * W for _ in range(H)]
    visited[x][y] = 0
    q = deque()
    q.append((x, y))

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            while True:
                if not (0<=nx<H and 0<=ny<W):
                    break
                if graph[nx][ny] == '*':
                    break
                if visited[nx][ny] < visited[x][y] + 1:
                    break
                q.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1
                nx = nx + dx[i]
                ny = ny + dy[i]

    return visited

W, H = map(int, sys.stdin.readline().split())
graph = [list(map(str, sys.stdin.readline().strip())) for _ in range(H)]
dx, dy = [-1, 0, 0, 1], [0, -1, 1, 0]
C = []
for i in range(H):
    for j in range(W):
        if graph[i][j] == 'C':
            C.append([i, j])
[start_x, start_y], [end_x, end_y] = C
answer = bfs(start_x, start_y)
print(answer[end_x][end_y] - 1)
print(answer)