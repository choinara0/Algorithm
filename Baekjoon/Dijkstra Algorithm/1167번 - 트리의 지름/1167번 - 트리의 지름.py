import sys
import heapq
input = sys.stdin.readline

def dijkstra(start):
    dist = [sys.maxsize] * (V+1)
    dist[start] = 0
    heap = []
    heapq.heappush(heap, [dist[start], start])

    while heap:
        current_cost, current_node = heapq.heappop(heap)

        for next_cost, next_node in graph[current_node]:
            sum_cost = current_cost + next_cost
            if dist[next_node] > sum_cost:
                dist[next_node] = sum_cost
                heapq.heappush(heap, [sum_cost, next_node])

    return dist[1:]

V = int(input())
graph = [[] for _ in range(V+1)]

for _ in range(V):
    c = list(map(int, input().split()))
    for e in range(1, len(c) - 2, 2):
        graph[c[0]].append([c[e+1], c[e]])

arr = dijkstra(1)
idx = arr.index(max(arr)) + 1
print(max(dijkstra(idx)))
