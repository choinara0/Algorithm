import sys
sys.setrecursionlimit(10**6)
def dfs(x):
    visited[x] = 1
    for nx in graph[x]:
        if not visited[nx]:
            dfs(nx)
            visited[x] += visited[nx]

input = sys.stdin.readline
N, R, Q = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    U, V = map(int, input().split())
    graph[U].append(V)
    graph[V].append(U)

visited = [0] * (N+1)
dfs(R)

U = [int(input()) for _ in range(Q)]
for u in U:
    print(visited[u])