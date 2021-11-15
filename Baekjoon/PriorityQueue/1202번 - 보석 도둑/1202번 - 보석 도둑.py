import sys
import heapq

N, K = map(int, sys.stdin.readline().split())
jewel = []
for i in range(N):
    w, v = map(int, sys.stdin.readline().split())
    heapq.heappush(jewel, [w, v])
bag = []
for i in range(K):
    c = int(sys.stdin.readline())
    heapq.heappush(bag, c)

answer = 0
temp = []
for i in range(K):
    cap = heapq.heappop(bag)
    while jewel and cap >= jewel[0][0]:
        [weight, value] = heapq.heappop(jewel)
        heapq.heappush(temp, -value)
    if temp:
        answer += -(heapq.heappop(temp))

print(answer)

