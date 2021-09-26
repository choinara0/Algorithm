import sys
sys.setrecursionlimit(10**9)
N = int(sys.stdin.readline())
Tree = [[] for i in range(N+1)]
Parent = [0 for _ in range(N+1)]

for i in range(N-1):
    a, b = map(int, sys.stdin.readline().split())
    Tree[a].append(b)
    Tree[b].append(a)

def dfs(start, Tree, Parent):
    for i in Tree[start]:
        if Parent[i] == 0:
            Parent[i] = start
            dfs(i, Tree, Parent)

dfs(1,Tree,Parent)

for i in range(2, N+1):
    print(Parent[i])

