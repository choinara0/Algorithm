import sys
import heapq

N = int(sys.stdin.readline())
maxQueue, minQueue = [], []

for i in range(N):
    temp = int(sys.stdin.readline())

    if i % 2 ==0:
        heapq.heappush(maxQueue, -1 * temp)
    else:
        heapq.heappush(minQueue, temp)

    if maxQueue and minQueue and -1 * maxQueue[0] > minQueue[0]:
        X = heapq.heappop(maxQueue) * -1
        heapq.heappush(maxQueue, heapq.heappop(minQueue) * -1)
        heapq.heappush(minQueue, X)

    print(maxQueue[0] * -1)

