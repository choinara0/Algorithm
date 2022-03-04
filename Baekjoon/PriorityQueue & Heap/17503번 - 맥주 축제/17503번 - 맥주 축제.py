import sys, heapq

N, M, K = map(int, sys.stdin.readline().split())
bear = [list(map(int, sys.stdin.readline().split())) for _ in range(K)]
bear.sort(key=lambda x:x[1])
heap = []
check = False
answer = 0

for i in range(K):
    favor, alcohol = bear[i]
    heapq.heappush(heap, favor)
    answer += favor

    if len(heap) > N:
        answer -= heapq.heappop(heap)
    if len(heap) == N and answer >= M:
        check = True
        print(alcohol)
        break

if not check:
    print(-1)