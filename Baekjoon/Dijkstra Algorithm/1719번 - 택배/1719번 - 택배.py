import sys
import heapq

def dijkstra(start):
    heap = []
    heapq.heappush(heap, [0, start])
    dp = [sys.maxsize for _ in range(n+1)]
    dp[start] = 0
    while heap:
        current_cost, current_node = heapq.heappop(heap)
        if dp[current_node] < current_cost:
            continue
        for next_cost, next_node in graph[current_node]:
            if dp[next_node] > next_cost + current_cost:
                dp[next_node] = next_cost + current_cost
                heapq.heappush(heap, [dp[next_node], next_node])
                dist[next_node][start] = current_node
    return

n, m = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
dist = [[sys.maxsize] * (n+1) for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append([c, b])
    graph[b].append([c, a])

for i in range(1, n+1):
    dijkstra(i)

for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j:
            print('-', end = ' ')
        else:
            print(dist[i][j], end = ' ')
    print()