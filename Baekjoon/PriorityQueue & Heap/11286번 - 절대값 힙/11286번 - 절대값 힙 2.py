# heapq 사용
import sys, heapq

N = int(sys.stdin.readline())
my_heap = []

for _ in range(N):
    x = int(sys.stdin.readline())
    if x == 0:
        if len(my_heap) == 0:
            print(0)
        else:
            print(heapq.heappop(my_heap)[1])
    else:
        heapq.heappush(my_heap, [abs(x), x])