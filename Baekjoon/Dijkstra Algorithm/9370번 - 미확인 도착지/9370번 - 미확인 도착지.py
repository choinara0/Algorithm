import sys
import heapq
input = sys.stdin.readline

def dijkstra(start):
    dist = [float('Inf')] * (n+1)
    dist[start] = 0
    heap = []
    heapq.heappush(heap, [0, start])

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

T = int(input())
for case in range(T):
    n, m, t = map(int, input().split())
    s, g, h = map(int, input().split())
    graph = [[] for _ in range(n+1)]

    for _ in range(m):
        a, b, d = map(int, input().split())
        if (a == g and b == h) or (a == h and b == g):
            d -= 0.1
        graph[a].append([d, b])
        graph[b].append([d, a])

    destination = []
    for x in range(t):
        destination.append(int(input()))
    destination.sort()

    dist = dijkstra(s)

    for x in destination:
        if dist[x] != float('Inf') and type(dist[x]) == float:
            print(x, end=' ')
    print()