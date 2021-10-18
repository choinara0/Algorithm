import sys
import heapq

N = int(sys.stdin.readline())
gift = []

for i in range(N):
    a = list(map(int, sys.stdin.readline().split()))

    if a[0] == 0 and len(gift) == 0:
        print(-1)
    elif a[0] == 0 and len(gift) != 0:
        print(-1 * heapq.heappop(gift))
    else:
        for i in a[1:]:
            heapq.heappush(gift, -1 * i)


