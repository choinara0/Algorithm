import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
graph = [[]*(N+1) for i in range(N+1)]
visited = [0] * (N+1)
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[b].append(a)
X = int(sys.stdin.readline())

def bfs(x):
    cnt = 0
    q = deque()
    q.append(x)
    visited[x] = 1

    while q:
        x = q.popleft()
        for node in graph[x]:
            if not visited[node]:
                q.append(node)
                visited[node] = 1
                cnt += 1

    return cnt


print(bfs(X))