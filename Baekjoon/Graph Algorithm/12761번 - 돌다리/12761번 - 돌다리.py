import sys
from collections import deque

A, B, N, M = map(int, sys.stdin.readline().split())
visited = [0] * 100001

def bfs(a, b, n, m):
    visited[n] = 0
    q = deque()
    q.append((n, m))

    while q:
        x, y = q.popleft()
        if x == y:
            return visited[x]
        for i in range(8):
            if i == 0: nx = x + 1
            elif i == 1: nx = x -1
            elif i == 2: nx = x + a
            elif i == 3: nx = x - a
            elif i == 4: nx = x + b
            elif i == 5: nx = x - b
            elif i == 6: nx = x * a
            elif i == 7: nx = x * b

            if 0<=nx<100001 and not visited[nx]:
                q.append((nx, y))
                visited[nx] = visited[x] + 1


print(bfs(A, B, N, M))