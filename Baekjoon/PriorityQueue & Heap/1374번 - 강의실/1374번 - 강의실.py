import sys
import heapq

N = int(sys.stdin.readline())
queue = []
timeTable = [list(map(int, sys.stdin.readline().split())) for i in range(N)]
timeTable.sort(key=lambda x:x[1])
heapq.heappush(queue, timeTable[0][2])

for i in range(1, N):
    if queue[0] > timeTable[i][1]:
        heapq.heappush(queue, timeTable[i][2])
    else:
        heapq.heappop(queue)
        heapq.heappush(queue, timeTable[i][2])

print(len(queue))
