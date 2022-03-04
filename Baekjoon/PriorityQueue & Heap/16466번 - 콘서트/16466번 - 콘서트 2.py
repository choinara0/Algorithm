# heapq 사용
import sys, heapq

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
heapq.heapify(A)
answer = 1

for _ in range(N):
    x = heapq.heappop(A)
    if answer == x:
        answer += 1
    else:
        break

print(answer)