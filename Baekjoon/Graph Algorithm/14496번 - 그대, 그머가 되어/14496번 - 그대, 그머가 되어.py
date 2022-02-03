import sys
from collections import deque

a, b = map(int, sys.stdin.readline().split())
N, M = map(int, sys.stdin.readline().split())
visited = [0] * (N+1)
graph = [[] for i in range(N+1)]
for _ in range(M):
    x, y = map(int, sys.stdin.readline().split())
    graph[x].append(y)
    graph[y].append(x)

def bfs(a, b):
    q = deque()
    q.append((a, 0))
    visited[a] = 1
    while q:
        x, cnt = q.popleft()
        if x == b:
            return cnt
        for node in graph[x]:
            if not visited[node]:
                q.append((node, cnt+1))
                visited[node] = 1
    return -1

print(bfs(a, b))