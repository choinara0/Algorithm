import sys
import heapq

def dijkstra(start):
    dist = [sys.maxsize] * N
    dist[start] = 0
    heap = []
    heapq.heappush(heap, [dist[start], start])

    while heap:
        current_cost, current_node = heapq.heappop(heap)

        if dist[current_node] < current_cost:
            continue

        for next_cost, next_node in graph[current_node]:
            if sight[next_node] == 0:
                if dist[next_node] > next_cost + current_cost:
                    dist[next_node] = next_cost + current_cost
                    heapq.heappush(heap, [dist[next_node], next_node])

    return dist[N-1]

N, M = map(int, sys.stdin.readline().split())
sight = list(map(int, sys.stdin.readline().split()))
sight[N-1] = 0
graph = [[] for _ in range(N)]

for _ in range(M):
    a, b, t = map(int, sys.stdin.readline().split())
    graph[a].append([t, b])
    graph[b].append([t, a])

answer = dijkstra(0)
print(-1 if answer == sys.maxsize else answer)