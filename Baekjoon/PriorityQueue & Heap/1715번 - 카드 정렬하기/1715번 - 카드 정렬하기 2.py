# heapq 사용
import sys, heapq

N = int(sys.stdin.readline())
my_heap = []
answer = 0

for _ in range(N):
    heapq.heappush(my_heap, int(sys.stdin.readline()))

while len(my_heap) > 1:
    temp1 = heapq.heappop(my_heap)
    temp2 = heapq.heappop(my_heap)
    answer += temp1 + temp2
    heapq.heappush(my_heap, temp1+temp2)

print(answer)