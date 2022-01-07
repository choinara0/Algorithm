import sys
sys.setrecursionlimit(10**5)

N = int(sys.stdin.readline())
adj = [[] for i in range(N+1)]

for i in range(N-1):
    n1, n2 = map(int, sys.stdin.readline().split())
    adj[n1].append(n2)
    adj[n2].append(n1)

depth = 0
visited = [0] * (N+1)

def dfs(start, hei, visited, arr):
    global depth
    visited[start] = 1
    isLeaf = True

    for i in adj[start]:
        if not visited[i]:
            isLeaf = False
            dfs(i, hei+1, visited, arr)
    if isLeaf:
        depth += hei

dfs(1, 0, visited, adj)
if depth%2 == 0:
    print("No")
else:
    print("Yes")