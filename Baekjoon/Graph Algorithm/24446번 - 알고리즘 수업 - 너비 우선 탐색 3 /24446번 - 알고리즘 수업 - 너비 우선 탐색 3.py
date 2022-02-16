import sys
from collections import deque

N, M, R = map(int, sys.stdin.readline().split())
graph = [[] * (N+1) for _ in range(N+1)]
visited = [0] * (N+1)
depth = [-1] * (N+1)

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(x):
    q = deque()
    q.append(x)
    visited[x] = 1
    depth[x] = 0
    while q:
        x = q.popleft()
        for nx in sorted(graph[x]):
            if not visited[nx]:
                visited[nx] = 1
                depth[nx] = depth[x] + 1
                q.append(nx)

bfs(R)
for i in range(1, N+1):
    print(depth[i])