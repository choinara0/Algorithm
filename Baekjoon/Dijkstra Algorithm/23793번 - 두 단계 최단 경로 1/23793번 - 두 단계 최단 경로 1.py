import sys
import heapq

input = sys.stdin.readline


def dijkstra_1(start):
    dist = [float('inf')] * (N + 1)
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


def dijkstra_2(start):
    dist = [float('inf')] * (N + 1)
    dist[start] = 0
    heap = []
    heapq.heappush(heap, [dist[start], start])

    while heap:
        current_cost, current_node = heapq.heappop(heap)

        if dist[current_node] < current_cost:
            continue

        for next_cost, next_node in graph[current_node]:
            if next_node == Y:
                continue
            sum_cost = next_cost + current_cost
            if dist[next_node] > sum_cost:
                dist[next_node] = sum_cost
                heapq.heappush(heap, [sum_cost, next_node])

    return dist


N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    u, v, w = map(int, input().split())
    graph[u].append([w, v])
X, Y, Z = map(int, input().split())
x_arr1 = dijkstra_1(X)
y_arr1 = dijkstra_1(Y)
x_arr2 = dijkstra_2(X)

answer_1 = (x_arr1[Y] + y_arr1[Z]) if (x_arr1[Y] + y_arr1[Z]) != float('inf') else -1
answer_2 = x_arr2[Z] if x_arr2[Z] != float('inf') else -1
print(answer_1, answer_2)