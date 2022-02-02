import sys
from collections import deque
sys.setrecursionlimit(10**5)

LOG = 21
N = int(sys.stdin.readline())
parent = [[0] * LOG for i in range(N+1)]
visited = [0] * (N+1)
depth_arr = [0] * (N+1)
graph = [[] for _ in range(N+1)]

for _ in range(N-1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)


def bfs(n):
    q = deque()
    q.append(n)
    while q:
        now = q.popleft()
        visited[now] = 1
        for node in graph[now]:
            if not visited[node]:
                q.append(node)
                parent[node][0] = now
                depth_arr[node] = depth_arr[now] + 1

def set_parent():
    for i in range(1, LOG):
        for j in range(1, N+1):
            parent[j][i] = parent[parent[j][i-1]][i-1]

bfs(1)
set_parent()
M = int(sys.stdin.readline())

def lcs(a, b):
    if depth_arr[a] > depth_arr[b]:
        a, b = b, a
    for i in range(LOG-1, -1, -1):
        if depth_arr[b] - depth_arr[a] >= (2**i):
            b = parent[b][i]

    if a == b:
        return a

    for i in range(LOG-1, -1, -1):
        if parent[a][i] != parent[b][i]:
            a = parent[a][i]
            b = parent[b][i]

    return parent[a][0]

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    print(lcs(a, b))