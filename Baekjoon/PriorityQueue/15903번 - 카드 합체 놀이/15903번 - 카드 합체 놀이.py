import sys
from queue import PriorityQueue

N, M = map(int, sys.stdin.readline().split())
num = list(map(int, sys.stdin.readline().split()))
priorityQueue = PriorityQueue()
result = 0
for i in range(N):
    priorityQueue.put(num[i])

for j in range(M):
    temp1 = priorityQueue.get()
    temp2 = priorityQueue.get()
    sumTemp = temp1 + temp2
    priorityQueue.put(sumTemp)
    priorityQueue.put(sumTemp)

for i in range(priorityQueue.qsize()):
    result += priorityQueue.get()

print(result)
