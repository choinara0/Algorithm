import sys
import heapq

def dijkstra(x):
    dist = [sys.maxsize] * (n+1)
    dist[x] = 0
    path = [[] for _ in range(n+1)]
    heap = []
    heapq.heappush(heap, [0, start, [start]])

    while heap:
        current_cost, current_city, p = heapq.heappop(heap)

        if current_cost > dist[current_city]:
            continue

        for next_cost, next_city in graph[current_city]:
            if dist[next_city] > next_cost + current_cost:
                dist[next_city] = next_cost + current_cost
                path[next_city] = p + [next_city]
                heapq.heappush(heap, [dist[next_city], next_city, path[next_city]])

    return dist, path


n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append([c, b])
start, end = map(int, sys.stdin.readline().split())

dist, path = dijkstra(start)
print(dist[end])
print(len(path[end]))
print(' '.join(map(str, path[end])))