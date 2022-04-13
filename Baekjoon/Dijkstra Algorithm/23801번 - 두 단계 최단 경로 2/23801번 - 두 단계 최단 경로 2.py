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

        for next_cost, next_node in graph[current_cost]:
            sum_cost = next_cost + current_cost
            if dist[next_node] > sum_cost:
                dist[next_node] = sum_cost
                heapq.heappush(heap, [sum_cost, next_node])

    return dist

input = sys.stdin.readline
N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    u, v, w = map(int, input().split())
    graph[u].append([w, v])
    graph[v].append([w, u])
X, Z = map(int, input().split())
P = int(input())
Y = list(map(int, input().split()))

x_arr = dijkstra(X)
print(x_arr)
p_arr = []
for i in Y:
    p_arr.append(dijkstra(i))
print(p_arr)