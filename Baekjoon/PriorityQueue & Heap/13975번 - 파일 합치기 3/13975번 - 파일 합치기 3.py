import sys
import heapq

T = int(sys.stdin.readline())

for t in range(T):
    queue = []
    result = 0
    N = int(sys.stdin.readline())
    files = sorted(list(map(int, sys.stdin.readline().split())))

    for f in files:
        heapq.heappush(queue, f)

    while len(queue) > 1:
        cost1 = heapq.heappop(queue)
        cost2 = heapq.heappop(queue)
        costSum = cost1 + cost2
        result += costSum
        heapq.heappush(queue, costSum)

    print(result)