# dijkstra algorithm
import heapq

def dijkstra(start, n, graph):
    dist = [float('Inf')] * (n+1)
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
    return dist[1:]

def solution(n, edge):
    answer = 0
    graph = [[] for _ in range(n+1)]
    for info in edge:
        node1, node2 = info
        graph[node1].append([1, node2])
        graph[node2].append([1, node1])

    arr = dijkstra(1, n, graph)
    max_dist = max(arr)

    for i in arr:
        if i == max_dist:
            answer += 1

    return answer
solution(6,	[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]) # 3