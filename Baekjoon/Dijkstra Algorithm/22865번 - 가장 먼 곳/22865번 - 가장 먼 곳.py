import sys
import heapq

def dijkstra(start):
    dist = [sys.maxsize] * (N+1)
    dist[start] = 0
    heap = []
    heapq.heappush(heap, (0, start))

    while heap:
        current_cost, current_node = heapq.heappop(heap)

        if dist[current_node] < current_cost:
            continue

        for next_cost, next_node in graph[current_node]:
            sum_cost = next_cost + current_cost
            if dist[next_node] > sum_cost:
                dist[next_node] = sum_cost
                heapq.heappush(heap, (sum_cost, next_node))

    return dist
input = sys.stdin.readline
N = int(input())
A, B, C = map(int, input().split())
M = int(input())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    D, E, L = map(int, input().split())
    graph[D].append([L, E])
    graph[E].append([L, D])

a_arr = dijkstra(A)
b_arr = dijkstra(B)
c_arr = dijkstra(C)
max_size = 0
answer = 0

for i in range(1, N+1):
    temp = min(a_arr[i], b_arr[i], c_arr[i])
    if max_size < temp:
        max_size = temp
        answer = i

print(answer)