import sys
import heapq

def dijkstra(start):
    dist[start] = 0
    heap = []
    heapq.heappush(heap, [0, 0])

    while heap:
        current_node, current_cost = heapq.heappop(heap)
        if dist[current_node] < current_cost:
            continue
        for next_node, next_cost in graph[current_node]:
            if dist[next_node] > current_cost + next_cost:
                dist[next_node] = current_cost + next_cost
                heapq.heappush(heap, [next_node, dist[next_node]])

    return

N, D = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(D+1)]
dist = [sys.maxsize] * (D+1)

for i in range(D):
    graph[i].append([i+1, 1])

for _ in range(N):
    info = list(map(int, sys.stdin.readline().split()))
    if info[1] > D:
        continue
    graph[info[0]].append([info[1], info[2]])
dijkstra(0)
print(dist[D])