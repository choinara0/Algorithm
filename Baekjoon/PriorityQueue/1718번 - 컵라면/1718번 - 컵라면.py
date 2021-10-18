import sys
import heapq

N = int(sys.stdin.readline())
cupTable = sorted([list(map(int, sys.stdin.readline().split())) for i in range(N)], key=lambda x:x[0])
cupSum = []

for i in cupTable:
    heapq.heappush(cupSum, i[1])

    if len(cupSum) > i[0]:
        heapq.heappop(cupSum)

print(sum(cupSum))