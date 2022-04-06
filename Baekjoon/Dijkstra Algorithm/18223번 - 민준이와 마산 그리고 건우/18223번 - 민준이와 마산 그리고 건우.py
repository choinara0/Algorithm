import sys
import heapq

def dijkstra(start, end):
    dist = [sys.maxsize] * (V+1)
    dist[start]= 0
    heap = []
    heapq.heappush(heap, [dist[start], start])
    while heap:
        current_cost, current_node = heapq.heappop(heap)
        for next_cost, next_node in graph[current_node]:
            if dist[next_node] > next_cost + current_cost:
                dist[next_node] = next_cost + current_cost
                heapq.heappush(heap, [dist[next_node], next_node])
    return dist[end]

V, E, P = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(V+1)]
for edge in range(E):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append([c, b])
    graph[b].append([c, a])


if dijkstra(1, V) == dijkstra(1, P) + dijkstra(P, V):
    print("SAVE HIM")
else:
    print("GOOD BYE")