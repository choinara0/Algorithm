import sys
from collections import deque

N, M, R = map(int, sys.stdin.readline().split())
graph = [[] * (N+1) for _ in range(N+1)]
visited = [0] * (N+1)
depth = [-1] * (N+1)
answer = 0

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(x):
    q = deque()
    q.append(x)
    visited[x] = 1
    depth[x] = 0
    cnt = 1
    while q:
        x = q.popleft()
        for nx in sorted(graph[x]):
            if not visited[nx]:
                cnt += 1
                visited[nx] = cnt
                depth[nx] = depth[x] + 1
                q.append(nx)

bfs(R)
for _ in range(1, N+1):
    answer += visited[_] * depth[_]
print(answer)