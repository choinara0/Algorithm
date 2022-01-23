import sys

T = int(sys.stdin.readline())

def dfs(node, cnt):
    visited[node] = 1
    for n in tree[node]:
        if visited[n] == 0:
            cnt = dfs(n, cnt+1)
    return cnt

for _ in range(T):
    N, M = map(int, sys.stdin.readline().split())
    tree = [[] for i in range(N+1)]
    for i in range(M):
        a, b = map(int, sys.stdin.readline().split())
        tree[a].append(b)
        tree[b].append(a)
    visited = [0] * (N+1)
    print(dfs(1, 0))