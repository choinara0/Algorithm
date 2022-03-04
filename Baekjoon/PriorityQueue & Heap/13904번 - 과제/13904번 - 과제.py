import sys, heapq

N = int(sys.stdin.readline())
my_heap = []

for _ in range(N):
    d, w = map(int, sys.stdin.readline().split())
    heapq.heappush(my_heap, [-d, -w])

answer = 0
day = abs(my_heap[0][0])
can_task = []

while day:
    while my_heap and abs(my_heap[0][0]) >= day:
        temp = heapq.heappop(my_heap)
        heapq.heappush(can_task, temp[1])
    day -= 1
    if can_task:
        answer += abs(heapq.heappop(can_task))

print(answer)