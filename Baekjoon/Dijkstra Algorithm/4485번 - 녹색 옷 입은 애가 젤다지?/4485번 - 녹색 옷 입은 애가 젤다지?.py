import sys
import heapq

def dijkstra(start):
    dist = [[sys.maxsize] * N for _ in range(N)]
    dist[start][start] = arr[start][start]
    heap = []
    heapq.heappush(heap, [dist[start][start], start, start])

    while heap:
        current_cost, current_node_x, current_node_y = heapq.heappop(heap)

        for i in range(4):
            next_node_x, next_node_y = current_node_x + dx[i], current_node_y + dy[i]
            if 0<=next_node_x<N and 0<=next_node_y<N:
                if dist[next_node_x][next_node_y] > current_cost + arr[next_node_x][next_node_y]:
                    dist[next_node_x][next_node_y] = current_cost + arr[next_node_x][next_node_y]
                    heapq.heappush(heap, [dist[next_node_x][next_node_y], next_node_x, next_node_y])

    return dist[N-1][N-1]
test_cnt = 1
while True:
    N = int(sys.stdin.readline())
    if N == 0:
        break
    arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    dx, dy = [-1, 0, 0, 1], [0, -1, 1, 0]
    answer = dijkstra(0)
    print("Problem {0}: {1}".format(test_cnt, answer))
    test_cnt += 1