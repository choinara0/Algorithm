import sys
N = int(sys.stdin.readline())
men1, men2 = map(int, sys.stdin.readline().split())
M = int(sys.stdin.readline())
familyTree = [[] for i in range(N+1)]
visited = [0] * (N+1)

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    familyTree[a].append(b)
    familyTree[b].append(a)

def dfs(m):
    global familyTree, visited, men1, men2
    for men in familyTree[m]:
        if men != men1 and visited[men] == 0:
            visited[men] = visited[m] + 1
            dfs(men)

dfs(men1)

if visited[men2] == 0:
    print(-1)
else:
    print(visited[men2])
