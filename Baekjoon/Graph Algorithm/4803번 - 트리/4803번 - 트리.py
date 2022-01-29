import sys

case_num = 0

def dfs(prev, node):
    visited[node] = True
    for n in graph[node]:
        if n == prev:
            continue
        if visited[n]:
            return False
        if not dfs(node, n):
            return False
    return True

while True:
    case_num += 1
    N, M = map(int, sys.stdin.readline().split())
    if N == 0 and M == 0 : break
    graph = [[] for i in range(N+1)]
    visited = [False] * (N+1)
    for _ in range(M):
        a, b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)

    tree_cnt = 0
    for v in range(1, N+1):
        if not visited[v]:
            if dfs(0, v):
                tree_cnt += 1
    if tree_cnt == 0:
        print("Case {}: No trees.".format(case_num))
    elif tree_cnt == 1:
        print("Case {}: There is one tree.".format(case_num))
    else:
        print("Case {}: A forest of {} trees.".format(case_num, tree_cnt))