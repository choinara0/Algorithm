import sys

N = int(sys.stdin.readline())
graph = [list(map(int, sys.stdin.readline().split())) for i in range(N)]
visited = [0 for i in range(N)]

def dfs(v):
    for i in range(N):
        if not visited[i] and graph[v][i]:
            visited[i] = 1
            dfs(i)

for i in range(N):
    dfs(i)
    for j in range(N):
        if visited[j] == 1:
            print(1, end=' ')
        else:
            print(0, end=' ')
    print()
    visited = [0 for i in range(N)]