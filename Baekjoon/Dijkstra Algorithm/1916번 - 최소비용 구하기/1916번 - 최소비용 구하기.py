import sys
import heapq

def dijkstra(start_node):
    dist[start_node] = 0
    heap = []
    heapq.heappush(heap, [start_node, 0])

    while heap:
        current_node, current_cost = heapq.heappop(heap)
        if dist[current_node] < current_cost:
            continue
        for next_node, next_cost in graph[current_node]:
            if dist[next_node] > current_cost + next_cost:
                dist[next_node] = current_cost + next_cost
                heapq.heappush(heap, [next_node, dist[next_node]])
    return dist[target]

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
graph = [[] for _ in range(N+1)]
dist = [100000000 for _ in range(N+1)]
for i in range(M):
    info = list(map(int, sys.stdin.readline().split()))
    graph[info[0]].append([info[1], info[2]])
start, target = map(int, sys.stdin.readline().split())
dijkstra(start)
print(dist[target])