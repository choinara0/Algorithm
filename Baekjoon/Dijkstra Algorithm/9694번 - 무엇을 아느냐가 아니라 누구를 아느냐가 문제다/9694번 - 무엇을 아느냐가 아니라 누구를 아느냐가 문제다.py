import sys
import heapq

def dijkstra(start):
    pre_node = [-1] * M
    dist = [sys.maxsize] * (M)
    dist[start] = 0
    heap = []
    heapq.heappush(heap, [0, 0])

    while heap:
        current_cost, current_node = heapq.heappop(heap)

        for next_cost, next_node in graph[current_node]:
            sum_cost = next_cost + current_cost
            if dist[next_node] > sum_cost:
                pre_node[next_node] = current_node
                dist[next_node] = sum_cost
                heapq.heappush(heap, [sum_cost, next_node])

    return dist, pre_node

def print_result(node_list, n):

    result = [M-1]
    idx = M-1

    while node_list[idx] != -1:
        idx = node_list[idx]
        result.append(idx)

    result.reverse()
    if len(result) == 1:
        result = [-1]

    print("Case #{}:".format(n+1), *result)

    return

input = sys.stdin.readline
T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    graph = [[] for _ in range(M)]

    for n in range(N):
        x, y, z = map(int, input().split())
        graph[x].append([z, y])
        graph[y].append([z, x])

    arr, arr2 = dijkstra(0)
    print_result(arr2, t)