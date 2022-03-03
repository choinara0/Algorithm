import sys
import heapq

N = int(sys.stdin.readline())
timeTable = []
for i in range(N):
    heapq.heappush(timeTable, list(map(int, sys.stdin.readline().split())))

computer = [[0, 0] for i in range(N)]
count = 0
while timeTable:
    [start, end] = heapq.heappop(timeTable)
    for j in range(len(computer)):
        if computer[j][0] <= start:
            if computer[j][0] == 0:
                count += 1
            computer[j][0] = end
            computer[j][1] += 1
            break
print(count)
for i in computer:
    if i[1] != 0:
        print(i[1], end=" ")

## 시간 초과로 인해 재풀이 필요