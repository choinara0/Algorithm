import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
graph = [[] * (N+1) for i in range(N+1)]

for _ in range(N-1):
    a, b, d = map(int, sys.stdin.readline().split())
    graph[a].append([b, d])
    graph[b].append([a, d])

def bfs(x, y):
    visited = [0] * (N+1)
    visited[x] = 1
    q = deque()
    q.append((x, 0))

    while q:
        x, dist = q.popleft()

        if x == y:
            return dist

        for node in graph[x]:
            if not visited[node[0]]:
                q.append((node[0], dist + node[1]))
                visited[node[0]] = 1
    return

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    print(bfs(a, b))