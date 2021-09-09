import sys
import collections
import heapq

V, E = map(int, sys.stdin.readline().split())
start_v = int(sys.stdin.readline())
graph = collections.defaultdict(list)

for i in range(E):
    u, v, w = map(int, sys.stdin.readline().split())
    graph[u].append((v, w))

def daikstra(graph, V, start_v):
    q = [(0, start_v)]
    distance = collections.defaultdict(int)

    while q:
        dist, node = heapq.heappop(q)
        if node not in distance:
            distance[node] = dist
            for v, w in graph[node]:
                update = dist + w
                heapq.heappush(q, (update, v))
    for i in range(1, V+1):
        if i==start_v:
            print('0')
        elif not distance[i]:
            print('INF')
        else:
            print(distance[i])

daikstra(graph, V, start_v)