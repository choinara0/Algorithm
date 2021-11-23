import sys
from collections import deque

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
graph = [list(map(int, sys.stdin.readline().split())) for i in range(N)]
dist = list(map(int, sys.stdin.readline().split()))
visited = [0] * (N + 1)

def bfs(x):
    global visited, graph
    visited[x] = 1
    q = deque()
    q.append(x)

    while q:
        x = q.popleft()
        for idx, item in enumerate(graph[x]):
            if item and not visited[idx]:
                visited[idx] = 1
                q.append(idx)


bfs(dist[0]-1)
for i in dist:
    if not visited[i-1]:
        print('NO')
        sys.exit()
print('YES')