# 트리의 가장 긴 지름을 구하는 방법 (귀류법)
# 아무 노드에서 가장 먼 곳을 찾는다. 그 곳에서 가장 먼 곳을 찾는다.
import sys
import heapq
input = sys.stdin.readline

def dijkstra(start):
    dist = [sys.maxsize] * (n+1)
    dist[start] = 0
    heap = []
    heapq.heappush(heap, [dist[start], start])

    while heap:
        current_cost, current_node = heapq.heappop(heap)

        for next_cost, next_node in graph[current_node]:
            sum_cost = current_cost + next_cost
            if dist[next_node] > sum_cost:
                dist[next_node] = sum_cost
                heapq.heappush(heap, [sum_cost, next_node])

    return dist[1:]

n = int(input())
graph = [[] for _ in range(n+1)]

for _ in range(n-1):
    a, b, c = map(int, input().split())
    graph[a].append([c, b])
    graph[b].append([c, a])

arr = dijkstra(1)
idx = arr.index(max(arr)) + 1
print(max(dijkstra(idx)))