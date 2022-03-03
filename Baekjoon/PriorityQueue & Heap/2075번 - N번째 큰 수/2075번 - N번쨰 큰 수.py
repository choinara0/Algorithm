import sys
import heapq

N = int(sys.stdin.readline())
h = []

for i in range(N):
    num = list(map(int, sys.stdin.readline().split()))
    if len(h) < N:
        for n in num:
            heapq.heappush(h, n)
    else:
        for n in num:
            heapq.heappush(h, n)
            heapq.heappop(h)

print(heapq.heappop(h))
