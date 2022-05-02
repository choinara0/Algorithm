import sys
from collections import deque
input = sys.stdin.readline

def find_bfs(x, y):
    global count
    q = deque()
    q.append([x, y])
    visited[x][y] = 1
    arr[x][y] = count

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0<=nx<N and 0<=ny<N and arr[nx][ny] == 1 and not visited[nx][ny]:
                q.append([nx, ny])
                visited[nx][ny] = 1
                arr[nx][ny] = count

    return

def make_bfs(z):
    global answer
    dist = [[-1] * N for _ in range(N)]
    q = deque()

    for i in range(N):
        for j in range(N):
            if arr[i][j] == z:
                q.append([i, j])
                dist[i][j] = 0

    while q:
        x, y = q.popleft()
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]

            if nx < 0 or nx>=N or ny<0 or ny>=N:
                continue

            if arr[nx][ny] > 0 and arr[nx][ny] != z:
                answer = min(answer, dist[x][y])
                return

            if arr[nx][ny] == 0 and dist[nx][ny] == -1:
                dist[nx][ny] = dist[x][y] + 1
                q.append([nx, ny])
    return

dx, dy = [-1, 0, 0, 1], [0, -1, 1, 0]
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]
count = 1
answer = sys.maxsize

for i in range(N):
    for j in range(N):
        if arr[i][j] == 1 and not visited[i][j]:
            find_bfs(i, j)
            count += 1

for i in range(1, count):
    make_bfs(i)

print(answer)