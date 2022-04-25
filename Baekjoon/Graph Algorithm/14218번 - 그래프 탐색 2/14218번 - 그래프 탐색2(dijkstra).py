import sys
import heapq

def dijkstra():
    dist = [sys.maxsize] * (n+1)
    dist[1] = 0
    heap = []
    heapq.heappush(heap, [dist[1], 1])

    while heap:
        current_cost, current_node = heapq.heappop(heap)

        for next_cost, next_node in graph[current_node]:
            sum_cost = next_cost + current_cost
            if dist[next_node] > sum_cost:
                dist[next_node] = sum_cost
                heapq.heappush(heap, [sum_cost, next_node])

    for d in range(len(dist)):
        if dist[d] == sys.maxsize:
            dist[d] = -1
    return dist[1:]

input = sys.stdin.readline
n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append([1, b])
    graph[b].append([1, a])

q = int(input())

for _ in range(q):
    i, j = map(int, input().split())
    graph[i].append([1, j])
    graph[j].append([1, i])

    arr = dijkstra()
    print(' '.join(map(str, arr)))