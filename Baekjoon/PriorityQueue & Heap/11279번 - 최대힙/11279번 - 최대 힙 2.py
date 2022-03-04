# heapq 사용
import sys, heapq

heap = []
N = int(sys.stdin.readline())

for _ in range(N):
    x = int(sys.stdin.readline())
    if x == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(abs(heapq.heappop(heap)))
    else:
        heapq.heappush(heap, -x)