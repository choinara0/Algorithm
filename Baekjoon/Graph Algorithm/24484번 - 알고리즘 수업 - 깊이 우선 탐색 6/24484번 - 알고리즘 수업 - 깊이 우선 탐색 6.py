import sys
sys.setrecursionlimit(10**6)
N, M, R = map(int, sys.stdin.readline().split())
graph = [[]*(N+1) for _ in range(N+1)]
visited = [0] * (N+1)
depth = [-1] * (N+1)
cnt = 1
answer = 0

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(bx, x):
    global cnt
    visited[x] = cnt
    cnt += 1
    depth[x] = depth[bx] + 1
    for nx in sorted(graph[x], reverse=True):
        if not visited[nx]:
            dfs(x, nx)

dfs(R, R)
for i in range(1, N+1):
    answer += visited[i] * depth[i]
print(answer)