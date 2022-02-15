import sys
sys.setrecursionlimit(10**5)

N, M, R = map(int, sys.stdin.readline().split())
graph = [[]*(N+1) for _ in range(N+1)]
visited = [0] * (N+1)

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(x, c):
    visited[x] = c
    for nx in sorted(graph[x]):
        if not visited[nx]:
            c += 1
            visited[nx] = c
            dfs(nx, c)

dfs(R, 1)

for _ in range(1, N+1):
    print(visited[_])