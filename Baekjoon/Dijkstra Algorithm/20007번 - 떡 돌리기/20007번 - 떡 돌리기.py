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
            sum_cost = next_cost + current_cost
            if dist[next_node] > sum_cost:
                dist[next_node] = sum_cost
                heapq.heappush(heap, [sum_cost, next_node])

    return dist

N, M, X, Y = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N)]
for _ in range(M):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append([c, b])
    graph[b].append([c, a])

distance = dijkstra(Y)
distance.sort()
idx = 0
day = 0

while idx < len(distance):
    if distance[idx] * 2 > X:
        day = -1
        break

    temp = X

    for i in range(idx, len(distance)):
        if distance[i]*2 <= temp:
            temp -= distance[i]*2
            idx = i+1
        else:
            break

    day += 1

print(day)
