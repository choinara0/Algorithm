import sys
import heapq

def dijkstra(start):
    dist = [sys.maxsize] * (N+1)
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
                heapq.heappush(heap, [dist[next_node], next_node])

    return dist[1:]

T = int(sys.stdin.readline())

for _ in range(T):
    N, M = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(N+1)]

    for _ in range(M):
        a, b, c = map(int, sys.stdin.readline().split())
        graph[a].append([c, b])
        graph[b].append([c, a])

    K = int(sys.stdin.readline())
    friend_location = list(map(int, sys.stdin.readline().split()))
    answer = [0] * N

    for k in friend_location:
        temp = dijkstra(k)
        for i in range(len(temp)):
            answer[i] += temp[i]

    print(answer.index(min(answer)) + 1)