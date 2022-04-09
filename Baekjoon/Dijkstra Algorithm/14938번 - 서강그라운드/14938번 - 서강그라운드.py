import sys
import heapq

def dijkstra(start):
    dist = [sys.maxsize] * (n+1)
    dist[start] = 0
    item_cnt = 0
    heap = []
    heapq.heappush(heap, [dist[start], start])

    while heap:
        current_cost, current_node = heapq.heappop(heap)

        if dist[current_node] < current_cost:
            continue

        for next_cost, next_node in graph[current_node]:
            if dist[next_node] > current_cost + next_cost:
                dist[next_node] = current_cost + next_cost
                heapq.heappush(heap, [dist[next_node], next_node])

    for i in range(1, n+1):
        if dist[i] <= m:
            item_cnt += item[i]

    return item_cnt

n, m, r = map(int, sys.stdin.readline().split())
item = [0] + list(map(int, sys.stdin.readline().split()))
graph = [[] for _ in range(n+1)]
answer = 0

for _ in range(r):
    a, b, l = map(int, sys.stdin.readline().split())
    graph[a].append([l, b])
    graph[b].append([l, a])

for i in range(1, n+1):
    answer = max(answer, dijkstra(i))

print(answer)