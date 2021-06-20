import sys



def dfs(v, visited, adjs, N):
    visited[v] = 1
    for i in adjs[v]:
        if visited[i] == 0:
            dfs(i, visited, adjs, N)

N, M = map(int, sys.stdin.readline().split())
visited = [0 for i in range(N+1)]
adjs = [[] for i in range(N+1)]
cnt = 0

for i in range(M):
    v1, v2 = map(int, sys.stdin.readline().split())
    adjs[v1].append(v2)
    adjs[v2].append(v1)


for j in range(1, N+1):
    if visited[j] == 0 :
        cnt += 1
        dfs(j, visited, adjs, N)

print(cnt)



