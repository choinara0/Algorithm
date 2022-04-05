import sys
import heapq

def dijkstra(start):
    dist = [sys.maxsize] * (N+1)
    dist[start] = 0
    heap = []
    heapq.heappush(heap, [dist[start], start])

    while heap:
        current_cost, current_node = heapq.heappop(heap)

        for next_node, next_cost in graph[current_node]:
            if dist[next_node] > current_cost + next_cost:
                dist[next_node] = current_cost + next_cost
                heapq.heappush(heap, [dist[next_node], next_node])
    return dist

N, M, X = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]
answer = 0

for _ in range(M):
    a, b, t = map(int, sys.stdin.readline().split())
    graph[a].append([b, t])

for i in range(1, N+1):
    if i == X:
        continue
    answer = max(answer, (dijkstra(i)[X] + dijkstra(X)[i]))

print(answer)