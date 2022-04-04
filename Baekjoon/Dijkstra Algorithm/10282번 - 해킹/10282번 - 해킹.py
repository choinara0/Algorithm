import sys
import heapq

T = int(sys.stdin.readline())

def dijkstra(start):
    dist = [sys.maxsize] * (n + 1)
    dist[start] = 0
    heap = []
    heapq.heappush(heap, [dist[start], start])

    while heap:
        current_cost, current_node = heapq.heappop(heap)
        for next_node, next_cost in graph[current_node]:
            if dist[next_node] > next_cost + current_cost:
                dist[next_node] = next_cost + current_cost
                heapq.heappush(heap, [dist[next_node], next_node])

    return dist

for _ in range(T):
    n, d, c = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(n+1)]
    for _ in range(d):
        a, b, s = map(int, sys.stdin.readline().split())
        graph[b].append([a, s])

    arr = dijkstra(c)
    computer_cnt, time = 0, 0

    for i in arr:
        if i != sys.maxsize:
            if time < i:
                time = i
            computer_cnt += 1

    print(computer_cnt, time)
