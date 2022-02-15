import sys
sys.setrecursionlimit(10**6)

N, M, R = map(int, sys.stdin.readline().split())
graph = [[]*(N+1) for _ in range(N+1)]
visited = [0] * (N+1)
cnt = 1

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(x):
    global cnt
    visited[x] = cnt
    cnt += 1
    for nx in sorted(graph[x]):
        if not visited[nx]:
            dfs(nx)

dfs(R)

print(*[visited[x] for x in range(1, N+1)], sep='\n')