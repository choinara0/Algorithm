import sys
import heapq

def dijkstra(start):
    dist = [sys.maxsize] * (N + 1)
    dist[start] = 0
    heap = []
    heapq.heappush(heap, [start, 0])

    while heap:
        current_node, current_cost = heapq.heappop(heap)

        for next_node, next_cost in graph[current_node]:
            if dist[next_node] > next_cost + current_cost:
                dist[next_node] = next_cost + current_cost
                heapq.heappush(heap, [next_node, dist[next_node]])
    return dist

N, M = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append([b, c])
    graph[b].append([a, c])

v1, v2 = map(int, sys.stdin.readline().split())

one = dijkstra(1)
v_1 = dijkstra(v1)
v_2 = dijkstra(v2)

answer = min(one[v1] + v_1[v2] + v_2[N], one[v2] + v_2[v1] + v_1[N])
print(answer if answer < sys.maxsize else -1)