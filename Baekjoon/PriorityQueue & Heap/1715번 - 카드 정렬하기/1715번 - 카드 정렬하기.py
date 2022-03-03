import sys
from queue import PriorityQueue

N = int(sys.stdin.readline())
result = 0
priorityQueue = PriorityQueue(maxsize=N)

for i in range(N):
    priorityQueue.put(int(sys.stdin.readline()))

while(priorityQueue.qsize()>1):
    temp1 = priorityQueue.get()
    temp2 = priorityQueue.get()
    result += temp1 + temp2
    priorityQueue.put(temp1+temp2)

print(result)
sys.exit()