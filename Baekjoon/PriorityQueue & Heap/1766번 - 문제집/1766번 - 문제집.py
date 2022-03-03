import sys
import heapq

N, M = map(int, sys.stdin.readline().split())
indegree = [0] * (N+1)
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    indegree[b] += 1
    graph[a].append(b)

queue = []
for i in range(1, N+1):
    if indegree[i] == 0:
        heapq.heappush(queue, i)
result = []

while queue:
    now = heapq.heappop(queue)
    result.append(now)
    for i in graph[now]:
        indegree[i] -= 1
        if indegree[i] == 0:
            heapq.heappush(queue, i)

print(*result)