import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
S, E = map(int, sys.stdin.readline().split())
graph = [[]*(N+1) for i in range(N+1)]
visited = [-1] * (N+1)
dx = [-1, 1]

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(x, y):
    q = deque()
    q. append(x)
    visited[x] = 0

    while q:
        x = q.popleft()
        if x == y:
            return visited[y]
        for _ in range(2):
            nx = x + dx[_]
            if 0<=nx<=N and visited[nx] == -1:
                q.append(nx)
                visited[nx] = visited[x] + 1
        for node in graph[x]:
            if visited[node] == -1:
                q.append(node)
                visited[node] = visited[x] + 1

    print(visited)
    return

print(bfs(S, E))