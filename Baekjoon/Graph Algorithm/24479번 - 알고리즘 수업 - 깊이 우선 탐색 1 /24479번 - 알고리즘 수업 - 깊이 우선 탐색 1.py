import sys
sys.setrecursionlimit(10**5)
N, M, R = map(int, sys.stdin.readline().split())
graph = [[]*(N+1) for _ in range(N+1)]
visited = [0] * (N+1)
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(bx, x):
    visited[x] = visited[bx] + 1
    for nx in sorted(graph[x]):
        if not visited[nx]:
            dfs(x, nx)
    return

dfs(R, R)
for i in range(1, N+1):
    print(visited[i])