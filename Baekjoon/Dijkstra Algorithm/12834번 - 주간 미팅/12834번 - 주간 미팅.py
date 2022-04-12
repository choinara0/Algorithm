import sys
import heapq

def dijkstra(start):
    dist = [sys.maxsize] * (V+1)
    dist[start] = 0
    heap = []
    heapq.heappush(heap, [dist[start], start])

    while heap:
        current_cost, current_node = heapq.heappop(heap)

        if dist[current_node] < current_cost:
            continue

        for next_cost, next_node in graph[current_node]:
            sum_cost = next_cost + current_cost
            if dist[next_node] > sum_cost:
                dist[next_node] = sum_cost
                heapq.heappush(heap, [sum_cost, next_node])

    return dist


N, V, E = map(int, sys.stdin.readline().split())
A, B = map(int, sys.stdin.readline().split())
H = list(map(int, sys.stdin.readline().split()))
graph = [[] for _ in range(V+1)]
answer = 0

for _ in range(E):
    a, b, l = map(int, sys.stdin.readline().split())
    graph[a].append([l, b])
    graph[b].append([l, a])

for h in H:
    distance = dijkstra(h)
    if distance[A] == sys.maxsize:
        distance[A] = -1
    if distance[B] == sys.maxsize:
        distance[B] = -1
    answer += distance[A]
    answer += distance[B]

print(answer)