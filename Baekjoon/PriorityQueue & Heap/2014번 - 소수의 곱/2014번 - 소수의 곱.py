import sys
import heapq

K, N = map(int, sys.stdin.readline().split())
primeNumList = list(map(int, sys.stdin.readline().split()))
primeQueue = []
for i in primeNumList:
    heapq.heappush(primeQueue, i)
for i in range(N):
    n = heapq.heappop(primeQueue)
    for j in range(K):
        newN = n * primeNumList[j]
        heapq.heappush(primeQueue, newN)

        if n % primeNumList[j] == 0:
            break


print(n)

