import heapq

def dijkstra(start, end, n, graph):
    dist = [int(1e9)] * (n+1)
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

    return dist[end]

def solution(n, s, a, b, fares):
    answer = int(1e9)
    graph = [[] for _ in range(n+1)]
    for fare in fares:
        start, end, cost = fare
        graph[start].append([cost, end])
        graph[end].append([cost, start])
    for i in range(1, n+1):
        answer = min(answer, dijkstra(s, i, n, graph) + dijkstra(i, a, n, graph) + dijkstra(i, b, n, graph))

    return answer

solution(6, 4, 6, 2, [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]) # 82
solution(7, 3, 4, 1, [[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]) # 14
solution(6, 4, 5, 6, [[2,6,6], [6,3,7], [4,6,7], [6,5,11], [2,5,12], [5,3,20], [2,4,8], [4,3,9]]) #18