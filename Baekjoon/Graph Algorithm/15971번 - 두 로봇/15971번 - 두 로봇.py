import sys
from collections import deque
input = sys.stdin.readline

def bfs(a, b):
    visited = [0] * (N+1)
    visited[a] = 1
    q = deque()
    q.append([a, 0, 0])

    while q:
        now, total, max_cost = q.pop()
        if now == b:
            print(total-max_cost)
            return
        for next_cost, next_node in graph[now]:
            if not visited[next_node]:
                visited[next_node] = 1
                q.appendleft([next_node, total+next_cost, max(max_cost, next_cost)])

N, A, B = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b, c = map(int, input().split())
    graph[a].append([c, b])
    graph[b].append([c, a])

bfs(A, B)