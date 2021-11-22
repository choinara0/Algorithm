import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
graph = [[] for i in range(N)]
for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
visited = [0] * (N)

def dfs(x, cnt):
    if cnt >= 4:
        print(1)
        sys.exit()
    for i in graph[x]:
        if not visited[i]:
            visited[i] = 1
            dfs(i, cnt+1)
            visited[i] = 0

    return False

for i in range(N):
    visited[i] = 1
    dfs(i, 0)
    visited[i] = 0

print(0)