import sys

def dfs(x):
    if visited[x]:
        if visited[x] == 1:
            return True
        return False
    visited[x] = 1
    for nx in graph[x]:
        if dfs(nx):
            return True
    visited[x] = 2
    return False

N = int(sys.stdin.readline())
graph = [[]*(N+1) for i in range(N+1)]
visited = [0] * (N+1)

for _ in range(1, N):
    i = int(sys.stdin.readline())
    M = list(map(int, sys.stdin.readline().split()))
    for m in M:
        graph[_].append(m)

if dfs(1):
    print('CYCLE')
else:
    print('NO CYCLE')