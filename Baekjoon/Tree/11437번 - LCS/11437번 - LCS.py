# LCS 알고리즘 공부
import sys
sys.setrecursionlimit(10**6)

N = int(sys.stdin.readline()) # node의 수
parent = [0] * (N+1) # 각 node의 parent
depth_arr = [0] * (N+1) # 각 node의 깊이
visited = [0] * (N+1)
graph = [[] for _ in range(N+1)]

# 간선 정보 입력
for _ in range(N-1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

# 각 node의 루트 노드로부터 깊이 구하기 / 각 node의 parent 구하기
def dfs(n, depth):
    visited[n] = 1
    depth_arr[n] = depth

    for node in graph[n]:
        if visited[node]:
            continue
        parent[node] = n
        dfs(node, depth + 1)

dfs(1, 0)

# 최소 공통 조상 찾기
def lcs(a, b):
    # 깊이 맞추기
    while depth_arr[a] != depth_arr[b]:
        if depth_arr[a] > depth_arr[b]:
            a = parent[a]
        else:
            b = parent[b]
    # 노드 맞추기
    while a != b:
        a = parent[a]
        b = parent[b]

    return a

M = int(sys.stdin.readline())

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    print(lcs(a, b))