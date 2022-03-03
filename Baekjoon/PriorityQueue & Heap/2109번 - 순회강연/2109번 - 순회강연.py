import sys
import heapq

N = int(sys.stdin.readline())
lectureRequest = [list(map(int, sys.stdin.readline().split())) for i in range(N)]
lectureRequest.sort(key=lambda x:x[1])
cost = []

for l in lectureRequest:
    heapq.heappush(cost, l[0])

    if len(cost) > l[1] :
        heapq.heappop(cost)

print(sum(cost))

