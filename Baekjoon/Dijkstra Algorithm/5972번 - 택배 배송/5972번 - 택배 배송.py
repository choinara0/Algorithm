import sys
import heapq

def dijkstra(start):
    dist[start] = 0
    heap = []
    heapq.heappush(heap, [1, 0])

    while heap:
        current_node, current_cost = heapq.heappop(heap)

        for next_node, next_cost in graph[current_node]:
            if dist[next_node] > current_cost + next_cost:
                dist[next_node] = current_cost + next_cost
                heapq.heappush(heap, [next_node, current_cost + next_cost])
    return

N, M = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]
dist = [sys.maxsize] * (N+1)

for _ in range(M):
    A, B, C = map(int, sys.stdin.readline().split())
    graph[A].append([B, C])
    graph[B].append([A, C])

dijkstra(1)
print(dist[N])