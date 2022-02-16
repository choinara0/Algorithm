import sys
from collections import deque

N, M, R = map(int, sys.stdin.readline().split())
graph = [[] * (N+1) for _ in range(N+1)]
visited = [0] * (N+1)

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
def bfs(x):
    q = deque()
    q.append(x)
    visited[x] = 1
    cnt = 1

    while q:
        x = q.popleft()
        for nx in sorted(graph[x], reverse=True):
            if not visited[nx]:
                cnt += 1
                q.append(nx)
                visited[nx] = cnt
    return

bfs(R)

for _ in range(1, N+1):
    print(visited[_])